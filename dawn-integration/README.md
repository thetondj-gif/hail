# DAWN Outreach Command — Capability Foundry Wave 1

## Status

`CAPABILITY_RESEARCH_COMPLETE`

Live email, SMS and voice operations remain disabled.

## Objective

Prepare a compliance-gated communications adapter that can later execute only approved outreach contracts through Hail's service boundary.

## Required future authorisation inputs

- approved campaign ID;
- approved recipient and lawful contact basis;
- suppression and opt-out result;
- approved message or script;
- allowed communication channel;
- geographic and time-window restrictions;
- per-contact and campaign cost ceiling;
- evidence and retention policy;
- accountable approver.

## First implementation slice

1. Reconcile the fork with the latest approved upstream multilingual and call-API changes.
2. Complete AGPL and commercial-deployment analysis.
3. Define campaign, recipient, suppression and channel schemas.
4. Build dry-run payload generation only.
5. Add tests proving live sends, calls and suppression bypass are refused.
6. Produce provider-neutral evidence and cost estimates through DAWN's standard response envelope.

## Wave 1 boundary

No provider credentials, live calls, live SMS, live email, webhook exposure, permanent listener, automatic recipient enrichment or DAWN runtime connection is permitted.

## Connection gate

Connection readiness requires licence disposition, lawful-use controls, suppression enforcement, cost ceilings, dry-run tests, security review and exact disable/rollback procedures.
