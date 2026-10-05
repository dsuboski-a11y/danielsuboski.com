# Daniel Job Dashboard — Project Plan

Target: https://danielsuboski.com/jobs/

Source of truth: Daniel Life OS Master Opportunity & Action Tracker → Job Pipeline / Completed Roster.

## Goal
Show a simple, mobile-readable status board for Daniel's active job search without exposing private application documents, sensitive personal data, or credentials.

## Status colors
- GREEN — verified submitted/complete, or no Daniel action required.
- YELLOW — useful optional action / packet work in progress.
- ORANGE — strong ready opportunity or browser execution available soon.
- RED — genuine blocker, hard deadline, or human-only gate.
- GREY — closed, superseded, stale, or intentionally not pursued.

## Each job card
Employer; role; requisition/ID; fit score; salary/range if public; location/work mode; deadline; posting-live status; resume state; cover-letter state; Work state; blocker; next action; submission-proof status; last checked timestamp.

## Privacy
GitHub Pages is public. jobs/status.json must contain sanitized status only. Never publish resume/cover-letter contents, private Drive links, application IDs unless intentionally public, email addresses, phone numbers, credentials, medical/legal information, or private qualification notes. If Daniel later wants a private dashboard, move the authenticated/private layer off public GitHub Pages.

## Data pipeline
1. JB audits the canonical Job Pipeline.
2. Chat/JB verifies public posting state and prepares packets.
3. Work performs authenticated last-mile submission only.
4. Submission proof updates Job Pipeline / Completed Roster.
5. A sanitizer exports public-safe dashboard fields to jobs/status.json.
6. jobs/index.html renders the status board and shows source timestamp / stale-data warning.

## Credit policy
Work should preserve roughly one-third of the weekly included allowance unless a hard deadline or expiring banked reset justifies using more. Work checks Settings → Usage before a large run and reports remaining allowance, reset timing, and any saved reset expiry. No paid reset or credit purchase without Daniel approval.

## Acceptance
- One page shows READY / WORKING / BLOCKED / SUBMITTED.
- No stale status is shown as live.
- Every submitted job has durable proof in private canonical records.
- Dashboard exposes no private application materials.
- Work does not spend allowance on research/drafting Chat/JB can do.