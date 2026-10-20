# CI Workflow Usage and Optimization — Proposed Changes Only

**Status:** Documentation / proposal. **Nothing described here has been applied to the workflow.**  
**Date:** 2026-10-20  
**Workflow:** [.github/workflows/tests.yml](../.github/workflows/tests.yml)

## Current behavior

The **Cuspell tests** GitHub Actions workflow runs when a pull request is opened or updated, and when commits are pushed to the main branch. Each run launches two separate **ubuntu-latest** jobs — one with **Python 3.11**, another with **Python 3.12** — each executing the same unittest suite.

### Observed October 2026 usage

As of October 20, the repository's October 1–20 Actions history showed **312 runs**, all occurring October 1–5:

| Source | Workflow runs | Normally resulting jobs |
| --- | ---: | ---: |
| Pull requests | 244 | 488 |
| Pushes to main | 68 | 136 |
| **Total** | **312** | **624** |

The account's billing screenshot showed **626 / 2,000 included Actions minutes**, **$3.76 gross usage**, **$3.76 discounts**, and **$0 actually billed**. Since GitHub rounds each job's billable execution time up to a whole minute, 624 expected matrix jobs explain nearly all of the recorded usage. The remaining difference has not been traced to individual jobs; this comparison is an estimate, not a billing audit.

**Finding:** The main source of minutes is the two-job test matrix running repeatedly as pull requests are updated. Both successful and failing jobs consume minutes. There is no current overage.

## Recommendations, in priority order

### 1. Cancel obsolete runs for the *same* pull request — recommended first

When multiple commits arrive rapidly on the same PR, older checks may still be running even though newer checks will replace them. Consider adding **workflow-level concurrency** so only the most recent PR check is active.

**Illustrative snippet only; not applied:**

~~~yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.run_id }}
  cancel-in-progress: ${{ github.event_name == 'pull_request' }}
~~~

Replace each ${{ marker with the GitHub expression opening token (a dollar sign followed by two opening braces) when implementing.

- The stable PR number groups runs belonging to the **same PR**.
- Main pushes use a unique run ID, so this rule does **not** cancel a main run.
- Different PRs do not cancel one another.
- The latest PR check must still complete and pass.

**Expected benefit:** Fewer wasted *overlapping* runs. This will not save completed jobs' minutes, and the current roughly one-minute jobs may finish before a newer run can cancel them. Do not promise a particular percentage saving.

**Acceptance criteria:** Rapid successive PR updates cancel the old PR check; a new PR check completes for both Python versions; unrelated PRs and main runs remain unaffected.

### 2. Reduce matrix jobs on PRs — optional, larger potential saving but less coverage

Consider running **Python 3.12 on PRs**, and **both 3.11 and 3.12 after merging to main**. This would cut the routine PR checks from two jobs to one.

At the October run counts, this would mean about **380 jobs rather than 624**, or **244 fewer jobs (about 39%)**, assuming identical run frequency and no material runtime changes. Because the jobs are short, that might translate to a similar reduction in rounded billable minutes, but real results require measurement.

**Important downside:** Python 3.11 regressions would sometimes be discovered **after** the merge. Since Cuspell supports both versions, retaining full pre-merge coverage is preferable unless the maintainer explicitly accepts this trade-off. If adopting this option, provide a way to run the full matrix *before merging* when needed. Check required CI status names if matrix construction changes.

**Recommendation:** Keep both versions on PRs by default; only consider this if minute usage becomes a problem.

### 3. Exclude documentation-only edits — optional, with required-check caveat

Workflow path filters could skip some documentation-only changes, which would reduce unneeded runs. First determine which inputs can affect program behavior and tests. Changes to source code, test data, registry/world data, tooling, Python project configuration, and the workflow itself should remain covered.

**Important:** If a GitHub Actions workflow is skipped by a path filter or skip-commit instruction, GitHub can leave its **required PR status check pending**, preventing merging. Check branch protection and rulesets first; do not blindly apply paths-ignore to the current required test workflow. A lightweight always-present required status may be needed if this option is pursued.

**Recommendation:** Low priority unless documentation edits account for significant usage.

### 4. Optimize runners or caching only after measurement

The current workflow uses standard 2-core Linux runners. Smaller or different runners might alter dollar pricing, but do not inherently reduce the **minutes** consumed. They may have different tool availability or run more slowly. For this small test suite, caching or complex setup changes may offer no benefit and could introduce overhead.

**Recommendation:** Not a first step.

## What not to do

- Do **not** disable all PR checks merely to save minutes.
- Do **not** remove main-branch CI without a separate decision.
- Do **not** treat skipped or canceled checks as passing.
- Do **not** drop Python 3.11 support silently.
- Do **not** make multiple CI optimizations simultaneously; measure them separately.

## Suggested implementation and verification plan (for a future approved change)

1. Record baseline workflow-run counts, PR and main triggers, actual per-job **billable** minutes, and failure rates.
2. Introduce only recommendation **1** in a separate, reviewed change.
3. Test two rapid pushes to the same PR, then different PRs, then a main push. Ensure correct cancellation, final success, and both Python versions.
4. Check rulesets, branch-protection requirements, and the set of required status checks.
5. Compare Actions usage after a representative period; note that GitHub rounds job minutes up, so faster checks might not reduce billable minutes.
6. If the savings are insufficient, separately decide whether recommendation **2** justifies reducing pre-merge compatibility testing.
7. Revert if latest checks are lost, unrelated runs cancel, checks become stuck, or compatibility coverage changes unexpectedly.

## GitHub references

- [Cuspell Actions run history](https://github.com/MartinApostolov/Cuspell/actions)
- [GitHub Actions runner pricing](https://docs.github.com/en/billing/reference/actions-runner-pricing)
- [Viewing job execution time](https://docs.github.com/en/actions/how-tos/monitor-workflows/view-job-execution-time)
- [Controlling workflow concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency)
- [Workflow triggers and path filters](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow)
- [Skipping runs and required-check caveats](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/skip-workflow-runs)

**Decision pending:** Whether and when to optimize CI. This document is an informational reference, not permission to change workflows.
