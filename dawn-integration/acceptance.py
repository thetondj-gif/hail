#!/usr/bin/env python3
"""Offline no-send acceptance for the DAWN Hail communications adapter."""
from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
CHANNELS = {"email", "sms", "voice"}
LAWFUL_BASES = {"consent", "contract", "legitimate-interest-reviewed", "existing-customer-service"}


def validate(request: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if request.get("schema_version") != 1:
        errors.append("schema_version")
    if request.get("dry_run") is not True:
        errors.append("dry_run_required")
    if request.get("provider_credentials_present") is not False:
        errors.append("credentials_prohibited_in_canary")
    for field in ("campaign_approved", "recipient_approved", "suppression_checked", "content_approved"):
        if request.get(field) is not True:
            errors.append(field)
    if request.get("suppressed") is not False:
        errors.append("recipient_suppressed")
    if request.get("channel") not in CHANNELS:
        errors.append("channel")
    if request.get("lawful_basis") not in LAWFUL_BASES:
        errors.append("lawful_basis")
    if not request.get("authority_evidence_ref"):
        errors.append("authority_evidence_ref")
    if not request.get("suppression_evidence_ref"):
        errors.append("suppression_evidence_ref")
    ceiling = request.get("cost_ceiling")
    if not isinstance(ceiling, (int, float)) or not 0 <= ceiling <= 5:
        errors.append("cost_ceiling")
    window = request.get("sending_window") if isinstance(request.get("sending_window"), dict) else {}
    try:
        start = datetime.fromisoformat(str(window.get("start")))
        end = datetime.fromisoformat(str(window.get("end")))
        if end <= start:
            errors.append("sending_window")
    except ValueError:
        errors.append("sending_window")
    return errors


def evaluate(request: dict[str, Any]) -> dict[str, Any]:
    errors = validate(request)
    return {
        "schema_version": 1,
        "capability": "dawn-governed-outreach",
        "operation": f"prepare-{request.get('channel', 'unknown')}",
        "status": "blocked" if errors else "success",
        "evidence": [ref for ref in (request.get("authority_evidence_ref"), request.get("suppression_evidence_ref")) if ref] if not errors else [],
        "data": {"payload_prepared": not errors, "message_sent": False, "call_started": False},
        "warnings": errors,
        "cost": {"currency": "USD", "estimated": 0},
        "external_actions_performed": False,
    }


def main() -> int:
    valid = json.loads((ROOT / "fixtures" / "valid-dry-run.json").read_text())
    invalid = json.loads((ROOT / "fixtures" / "invalid-live-send.json").read_text())
    accepted = evaluate(valid)
    refused = evaluate(invalid)
    assertions = [
        accepted["status"] == "success",
        accepted["data"]["message_sent"] is False,
        accepted["data"]["call_started"] is False,
        accepted["external_actions_performed"] is False,
        refused["status"] == "blocked",
        "dry_run_required" in refused["warnings"],
        "recipient_suppressed" in refused["warnings"],
        "lawful_basis" in refused["warnings"],
    ]
    report = {
        "capability": "dawn-governed-outreach",
        "status": "passed" if all(assertions) else "failed",
        "tests": len(assertions),
        "passed": sum(assertions),
        "network_used": False,
        "credentials_required": False,
        "messages_sent": 0,
        "calls_started": 0,
        "external_actions_performed": False,
    }
    print(json.dumps(report, indent=2))
    return 0 if all(assertions) else 1


if __name__ == "__main__":
    sys.exit(main())
