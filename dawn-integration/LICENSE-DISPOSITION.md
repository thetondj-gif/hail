# Hail licence disposition

## Verified source licence

The repository licence is **GNU Affero General Public License version 3 (AGPL-3.0)**.

## Wave 1 decision

The DAWN integration work may proceed inside this fork as an isolated, disabled and reviewable adapter specification with offline acceptance tests.

No live network deployment, customer-facing hosted service, proprietary bundling decision or DAWN production connection is approved by this document.

## Required before deployment

A named owner must record a commercial and legal disposition covering:

1. whether Hail will remain a separately operated AGPL service;
2. how complete corresponding source will be offered to network users where required;
3. which DAWN components communicate across the service boundary;
4. whether any modifications to Hail will be distributed or offered over a network;
5. provider terms for email, SMS and voice services;
6. consent, suppression, privacy and retention controls;
7. customer contract language and support obligations.

Keeping Hail behind an API or process boundary does **not**, by itself, settle AGPL obligations. Legal review is required before a commercial customer deployment.

## Merge gate

The current PR may become technically merge-ready when its offline tests pass, because it sends nothing and binds no credentials. It must remain operationally disabled until the deployment disposition above is approved.
