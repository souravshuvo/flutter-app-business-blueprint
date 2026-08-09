# Existing App Improvement Prompt Pack V2

Version: 2  
Default mode: fast repository audit with lightweight verification

Use this prompt pack to improve apps that are already live on Google Play.

This pack is designed for Codex repository workflow. You can copy and paste any prompt directly into a Codex task where the app repository is open. Codex should inspect the repository first, skip heavy commands by default, and only ask for external Play Console, AdMob, Crashlytics, Android vitals, review, or revenue data when that information is truly needed.

## Purpose

Create a repeatable improvement process for a portfolio of live Flutter apps and games.

The goal is to review each app like a small product: understand current value, find bugs, improve usefulness, check market fit, audit monetization, reduce policy risk, and ship focused updates.

## When to Use

Use this prompt pack when:

- An app is already published on Google Play.
- You want to review an existing codebase.
- You want to fix bugs and crashes.
- You want to improve user value.
- You want to check AdMob implementation and ad experience.
- You want to compare the app against the current market.
- You want a focused update plan instead of a large rewrite.
- You want to repeat the same process across many apps.

Do not use this pack to start a brand-new app. Use `prompts/new-app-planning-prompt.md` for new app ideas.

## Codex Repository Mode

When the app repository is already open in Codex, do not paste project structure, source files, dependency lists, routes, ad service code, Firebase setup, or local project paths.

Codex should inspect the repository first and discover:

- App name when available.
- Package name.
- Current version name and version code.
- Flutter dependencies.
- Main folders and architecture.
- State management.
- Routing.
- Firebase usage.
- AdMob usage.
- Permissions.
- Tests.
- Build configuration.

Only add information that is outside the repository, such as:

- Google Play URL.
- Main target user.
- Current ratings and review themes.
- Crashlytics or Android vitals summary.
- AdMob revenue or warning summary.
- Known bugs from users.
- Feature requests.
- Store listing notes.
- Play Console policy warnings.

If you do not have those details, paste the prompt anyway. Codex should continue with repository inspection and mark external data as unknown.

## Recommended Flow

For a single existing app, run these prompts in order:

1. One-app audit kickoff.
2. Codebase and architecture review.
3. Code review implementation, when fixes are approved.
4. Bug, crash, and performance triage.
5. Bug fix implementation, when fixes are approved.
6. AdMob, monetization, and analytics audit.
7. AdMob, monetization, and analytics implementation, when fixes are approved.
8. Store listing, market, and ASO review.
9. Store listing and ASO implementation, when changes are approved.
10. Usefulness and feature opportunity review.
11. Feature implementation, when features are approved.
12. Update scope decision.
13. Release scope implementation, when approved.
14. QA and release readiness.
15. Post-release monitoring.
16. Learning note.

Pattern:

- Numbered prompts inspect, audit, review, or plan.
- Matching `B` prompts solve approved findings.
- Do not run a `B` prompt until the matching numbered prompt has produced findings and you have approved the implementation scope.
- Prompt 9 is a general fallback implementation prompt when no specific `B` prompt fits.

## Performance and Verification Rule

Do not run `flutter pub get`, `flutter analyze`, `flutter test`, Gradle build, release build, install, emulator, device launch, or release packaging unless explicitly requested or the task cannot be verified without it.

For audit, review, planning, market, ASO, feature discovery, and monetization inspection:

- Inspect files only.
- Use fast search and file reads.
- Do not download dependencies.
- Do not run `flutter pub get`.
- Do not run `flutter analyze`.
- Do not run `flutter test`.
- Do not run Gradle.
- Do not build.
- Do not install.
- Do not launch emulator or device.
- Ignore generated and build folders such as `build/`, `.dart_tool/`, `.gradle/`, `android/build/`, `ios/Pods/`, and generated plugin registrant files unless the task specifically requires them.

For implementation prompts, prefer lightweight verification first:

1. Inspect the relevant files.
2. Run formatter only on changed files.
3. Run static analysis only when relevant and reasonably fast.
4. Run targeted tests if available.
5. Run full analysis, full tests, Gradle, or build only for release readiness, native Android changes, dependency changes, Firebase or AdMob initialization changes, permission changes, Gradle changes, signing or release config changes, or issues that cannot be verified otherwise.

If `pub get`, analysis, tests, build, install, emulator, or device run is skipped, explain why it was skipped and what risk remains.

For 15 apps, do not try to improve every app at once. First run the portfolio prompt, then improve the best candidates one by one.

## Prompt 1: Portfolio Inventory and Priority Ranking

Use this once before reviewing individual apps.

```text
You are helping me improve my portfolio of live Flutter apps using the Flutter App Business Blueprint process.

I have around 15 apps on Google Play. I want to improve them one by one instead of randomly changing code.

Create a portfolio improvement inventory and priority ranking.

First, inspect anything available in the current workspace or repository that helps identify apps. If the portfolio list is not available locally, ask me for only the app names or Play Store links needed to rank the portfolio.

What I want from you:
1. Create a simple portfolio table.
2. Group apps by priority: fix first, improve next, monitor only, or consider retiring.
3. Identify which apps need code review first.
4. Identify which apps need market or ASO review first.
5. Identify which apps need AdMob review first.
6. Identify which apps may have policy, privacy, or trust risk.
7. Recommend the first 3 apps to improve.
8. Explain why those 3 should come first.

Rules:
- Do not ask for codebase details that can be discovered from repositories.
- Prefer apps with real user value, revenue potential, or fixable issues.
- Do not recommend large rewrites unless an app is structurally broken.
- Separate urgent bugs from nice-to-have improvements.
- If data is missing, create a "needs data" column.
- Keep the recommendation practical for a solo developer.

Expected output:
- Portfolio table.
- Priority ranking.
- First 3 app recommendations.
- Missing external data list.
- Next prompt to run for the top app.
```

## Prompt 2: One-App Audit Kickoff

Use this at the start of each app review.

```text
You are reviewing the current Flutter repository as an existing app that is already published or intended to be maintained on Google Play.

Follow the Flutter App Business Blueprint process. Treat this as a product improvement cycle, not just a code cleanup.

First, inspect the current repository. Discover the app name, package name, version, dependencies, Firebase usage, AdMob usage, permissions, tests, and project structure from the files.

What I want from you:
1. Identify the app type and main user value.
2. Summarize the discovered app identity and configuration.
3. Summarize the codebase structure.
4. Identify architecture patterns used.
5. Identify risky areas to review first.
6. Identify what external dashboard or store data is still unknown.
7. Create a focused audit plan.
8. Do not change code yet unless I explicitly ask.

Rules:
- Read existing files before judging the code.
- Do not ask me for information that can be found in the repository.
- Do not assume this app should be rewritten.
- Protect existing working behavior.
- Focus on user value, stability, ads, privacy, and release readiness.

Expected output:
- Current app summary.
- Discovered package, version, Firebase, AdMob, and permission summary.
- Codebase structure summary.
- Main risks.
- Audit checklist.
- Missing external inputs.
- Recommended next prompt.
```

## Prompt 3: Codebase and Architecture Review

Use this to inspect the existing Flutter code before changing it.

```text
You are reviewing the current Flutter repository for maintainability, correctness, and future updates.

Inspect the repository directly. Do not ask me for local paths, package names, dependencies, file structure, or architecture details that can be found in the codebase.

What I want from you:
1. Inspect the project structure.
2. Identify state management, routing, data storage, Firebase, AdMob, and platform services.
3. Find risky patterns, dead code, duplication, fragile files, and likely behavioral problems.
4. Identify missing or weak tests.
5. Recommend small refactors only where they reduce real risk.
6. Produce a prioritized code review report with file references.

Rules:
- Use a code-review stance.
- Findings must come first and include file and line references.
- Do not change code yet.
- Do not rewrite unrelated code.
- Do not change architecture just for style.
- Prefer small fixes that improve stability and clarity.
- Respect existing user changes.

Expected output:
- Findings ordered by severity.
- File and line references.
- Risk explanation.
- Suggested fix for each issue.
- Test recommendations.
- Safe implementation order.
```

## Prompt 3B: Code Review Fix Implementation

Use this after Prompt 3 when you want Codex to solve approved code review findings.

```text
You are implementing approved code review fixes in the current Flutter repository.

Use the code review findings from this task. If no code review findings are available, first inspect the repository and create a tiny code-quality fix scope, then ask me to approve that scope before editing.

What I want from you:
1. Re-read the relevant files before editing.
2. Fix only the approved code review findings.
3. Keep changes small and reviewable.
4. Preserve existing behavior unless the approved finding is a behavior bug.
5. Prefer local patterns over new abstractions.
6. Add or update focused tests where useful.
7. Follow the Performance and Verification Rule for formatting, static analysis, tests, and builds.
8. Produce a short implementation summary and manual QA checklist.

Rules:
- Do not rewrite unrelated files.
- Do not change architecture just for style.
- Do not introduce new dependencies unless explicitly approved.
- Do not change app IDs, signing, production secrets, or release config unless explicitly approved.
- If a finding is too risky or too broad, leave it as a documented follow-up instead of guessing.
- Respect existing user changes.

Expected output:
- Approved findings fixed.
- Files changed.
- Tests or checks run.
- Manual QA steps.
- Findings intentionally left for later.
- Remaining risks.
```

## Prompt 4: Bug, Crash, and Performance Triage

Use this when the app has crashes, bad reviews, slow screens, or unknown quality problems. This prompt finds and prioritizes problems. Use Prompt 4B to fix the approved bugs.

```text
You are helping me triage bugs, crashes, ANRs, and performance issues in the current Flutter repository.

First, inspect the codebase, dependencies, platform config, tests, and any available logs or issue notes in the repository. If Crashlytics, Android vitals, Play reviews, or reproduction steps are not available locally, continue with code-based triage and list exactly what external data would improve confidence.

What I want from you:
1. Group likely issues by severity.
2. Identify likely root causes from code and available evidence.
3. Reproduce locally where practical.
4. Recommend high-confidence fixes first.
5. Prepare a focused bug-fix implementation scope.
6. Avoid broad refactors unless needed.
7. Produce a fix plan, ready-to-run Prompt 4B input, and verification checklist.

Rules:
- Do not guess silently. Mark assumptions clearly.
- Do not ask for codebase details that can be inspected directly.
- Do not change code in this prompt.
- Prioritize crashes, data loss, broken core flows, ad-blocking bugs, and release blockers.
- Keep fixes focused and reviewable.

Expected output:
- Issue grouping.
- Root-cause notes.
- Recommended fix order.
- External data that would help, if any.
- Test recommendations.
- Ready-to-run Prompt 4B input.
- Manual QA steps.
- Remaining risks.
```

## Prompt 4B: Bug Fix Implementation

Use this after Prompt 4 when you want Codex to solve the approved bugs.

```text
You are fixing approved bugs in the current Flutter repository.

Use the bug triage findings from this task. If no bug triage findings are available, first inspect the repository and create a tiny bug-fix scope, then ask me to approve that scope before editing.

What I want from you:
1. Re-read the relevant files before editing.
2. Fix only the approved high-confidence bugs.
3. Keep changes small and reviewable.
4. Preserve existing behavior outside the bug scope.
5. Add or update focused tests where useful.
6. Follow the Performance and Verification Rule for formatting, static analysis, tests, and builds.
7. Produce a short fix summary and manual QA checklist.

Rules:
- Do not rewrite unrelated files.
- Do not bundle feature work with bug fixes.
- Do not change app IDs, signing, production secrets, or release config unless the approved bug requires it.
- If a suspected bug is uncertain or risky to fix, leave it as a documented follow-up instead of guessing.
- Respect existing user changes.

Expected output:
- Bugs fixed.
- Files changed.
- Tests or checks run.
- Manual QA steps.
- Bugs intentionally left for later.
- Remaining risks.
```

## Prompt 5: AdMob, Monetization, and Analytics Audit

Use this for every monetized app before release. This prompt audits AdMob, monetization behavior, and ad-related Firebase Analytics. It should not change code.

```text
You are auditing AdMob, monetization, and ad-related analytics in the current Flutter repository.

Inspect the repository directly. Do not edit anything.

Discover whether the app uses banners, interstitials, rewarded ads, app-open ads, native ads, in-app purchases, subscriptions, or no monetization. Find ad unit configuration, test mode behavior, production mode behavior, ad placement code, frequency caps, failure handling, and Firebase Analytics events related to ads and user flow.

What I want from you:
1. Explain the current AdMob implementation.
2. Identify all ad formats used.
3. Identify where each ad appears in the user flow.
4. Confirm test ads and production ads are clearly separated.
5. Check whether ad placements are user-friendly.
6. Check whether interstitials appear only at natural transition points.
7. Check whether rewarded ads reward the correct action.
8. Check whether frequency caps exist.
9. Check whether ad loading failures block app usage.
10. Identify revenue bottlenecks visible from code.
11. Identify policy or invalid traffic risks.
12. Identify ad-related performance issues.
13. Review Firebase Analytics events related to AdMob optimization.
14. Recommend missing analytics events.
15. Create a prioritized fix plan.

Rules:
- Do not change code.
- Do not ask me where ads are implemented until you have searched the repository.
- User experience comes before revenue.
- Policy compliance comes before revenue.
- Do not encourage users to click ads.
- Do not reward ad clicks.
- Do not use real production ad clicks for testing.
- Mark AdMob dashboard-only items as unknown if not available.
- Use current official AdMob and Google Play policy guidance when making policy claims.
- Wait for approval before implementation.

Expected output:
- Current AdMob implementation summary.
- Ad format and placement review.
- Test mode and production mode review.
- Frequency cap review.
- Revenue bottlenecks.
- Policy risk review.
- Performance risk review.
- Missing analytics events.
- Required fixes.
- Optional revenue improvements.
- Test plan for ads.
```

## Prompt 5B: AdMob, Monetization, and Analytics Implementation

Use this after Prompt 5 when you want Codex to solve the approved AdMob, monetization, and ad-related analytics issues.

```text
You are implementing approved AdMob, monetization, and ad-related analytics fixes in the current Flutter repository.

Use the AdMob audit findings from this task. If no AdMob audit findings are available, first inspect the repository and create a tiny implementation scope, then ask me to approve that scope before editing.

What I want from you:
1. Re-read the relevant ad, monetization, analytics, configuration, and user-flow files before editing.
2. Fix only the approved policy risks, revenue bottlenecks, performance issues, and missing analytics events.
3. Keep changes minimal and reviewable.
4. Preserve existing app behavior outside the approved ad and analytics scope.
5. Keep test ads and production ads safely separated.
6. Add or update only necessary Firebase Analytics events for ad optimization and user-flow measurement.
7. Add or update focused tests where practical.
8. Follow the Performance and Verification Rule for formatting, static analysis, tests, and builds.
9. Produce a short implementation summary and manual QA checklist.

Rules:
- Do not touch unrelated files.
- Do not bundle unrelated feature work with monetization fixes.
- Do not change app ID, package name, signing, production secrets, or release config unless explicitly approved.
- Do not encourage ad clicks.
- Do not reward ad clicks.
- Do not make ad loading failure block core app usage.
- If a recommended revenue improvement conflicts with user experience or policy safety, skip it and document why.
- Respect existing user changes.

Expected output:
- Approved issues fixed.
- Files changed.
- Analytics events added or updated.
- Tests or checks run.
- Manual QA steps for ads and analytics.
- Issues intentionally left for later.
- Remaining risks.
```

## Prompt 6: Store Listing, Market, and ASO Review

Use this before deciding new features.

```text
You are reviewing the market position and Play Store listing for the current app.

First, inspect the repository to discover the app name, package name, category hints, core features, screenshots or assets, supported platforms, permissions, and monetization. Then search for the current Play Store listing and similar apps if network access is available. If the Play Store URL cannot be found, ask me only for the Play Store link.

What I want from you:
1. Summarize what problem this app appears to solve.
2. Identify the likely target user.
3. Compare the app against similar apps.
4. Identify missing user value.
5. Review title, short description, full description, and screenshots when available.
6. Suggest better keywords without keyword stuffing.
7. Suggest screenshot improvements.
8. Identify trust, policy, or misleading-claim risks.
9. Recommend 3 practical improvements that could increase usefulness or conversion.
10. Decide whether this app is worth improving now.

Rules:
- Use current information for market and policy claims.
- Do not ask for app identity data that can be discovered from the repo.
- Do not suggest fake claims, fake results, fake reviews, or misleading screenshots.
- Prefer useful differentiation over copying competitors.
- Keep recommendations realistic for a small update.

Expected output:
- Market summary.
- Competitor notes.
- Store listing issues.
- ASO improvement suggestions.
- Top 3 useful product improvements.
- Improve, monitor, or retire recommendation.
```

## Prompt 6B: Store Listing and ASO Implementation

Use this after Prompt 6 when you want Codex to solve approved store listing, ASO, screenshot, or positioning issues.

```text
You are implementing approved store listing and ASO improvements for the current Flutter app.

Use the market and ASO findings from this task. If no market or ASO findings are available, first inspect the repository and create a small store-listing improvement scope, then ask me to approve that scope before editing.

What I want from you:
1. Re-read the repository files, assets, screenshots, metadata, docs, or release notes that are relevant to store listing work.
2. Create improved title, short description, full description, and keyword strategy based on approved findings.
3. Create screenshot text or screenshot brief if screenshots need improvement.
4. Update repository files only when approved listing, metadata, docs, or asset source files exist in the repo.
5. Do not publish anything to Play Console.
6. Keep all claims truthful and supported by the actual app.
7. Produce a copy-ready Play Store update package and QA checklist.

Rules:
- Do not make fake claims, fake results, fake rankings, or fake review language.
- Do not keyword stuff.
- Do not promise features that the app does not actually have.
- Do not change code unless the approved ASO fix requires a small in-app text or asset update.
- Do not touch unrelated files.
- Mark anything that must be changed manually in Play Console.
- Respect existing user changes.

Expected output:
- Store listing copy created or updated.
- Repository files changed, if any.
- Screenshot improvement brief.
- Play Console manual update checklist.
- Policy or claim risks still remaining.
- Next recommended action.
```

## Prompt 7: Usefulness and Feature Opportunity Review

Use this after quality and monetization risks are understood.

```text
You are helping me decide useful new features for the current Flutter app.

First, inspect the repository and previous audit findings in this task. Infer the app's current user problem, main features, screens, data model, monetization, and codebase risks. If user reviews or market findings are not available, continue with repository-based product analysis and mark those inputs as unknown.

What I want from you:
1. Identify what makes the app useful today.
2. Identify where users may get stuck or disappointed.
3. Suggest 5-10 feature opportunities.
4. Score each feature by user value, effort, risk, monetization fit, and policy risk.
5. Choose the best 1-3 features for the next update.
6. Define what should not be built yet.
7. Create a small update scope.

Rules:
- Do not ask me to restate current features that are visible in the code.
- Prefer improvements that make the app genuinely more useful.
- Prefer simple features that can be tested and shipped.
- Do not add login, cloud sync, AI, subscriptions, or complex backend work unless the app truly needs it.
- Do not add features only to create more ad impressions.
- Keep the update realistic for one developer.

Expected output:
- Current usefulness summary.
- Feature opportunity table.
- Top 1-3 feature recommendations.
- Not-now list.
- Update scope.
- Acceptance criteria.
```

## Prompt 7B: Feature Implementation

Use this after Prompt 7 when you want Codex to implement approved useful features.

```text
You are implementing approved feature improvements in the current Flutter repository.

Use the feature opportunity findings and approved feature scope from this task. If no approved feature scope is available, first inspect the repository and create a tiny feature implementation proposal, then ask me to approve that scope before editing.

What I want from you:
1. Re-read the relevant feature, UI, state, data, analytics, and test files before editing.
2. Implement only the approved feature scope.
3. Keep the feature small enough for one focused app update.
4. Follow the existing architecture and visual style.
5. Add or update analytics only when the feature needs measurement.
6. Add or update focused tests where useful.
7. Follow the Performance and Verification Rule for formatting, static analysis, tests, and builds.
8. Produce a short implementation summary and manual QA checklist.

Rules:
- Do not add unrelated features.
- Do not introduce login, cloud sync, AI, subscriptions, or backend work unless explicitly approved.
- Do not add features only to create more ad impressions.
- Do not touch AdMob placement or frequency unless the approved feature scope includes it.
- Do not change app IDs, signing, production secrets, or release config unless explicitly approved.
- Respect existing user changes.

Expected output:
- Feature implemented.
- Files changed.
- Analytics events added or updated, if any.
- Tests or checks run.
- Manual QA steps.
- Out-of-scope feature ideas left for later.
- Remaining risks.
```

## Prompt 8: Update Scope Decision

Use this before implementation.

```text
You are helping me decide the exact next update scope for the current Flutter app.

Use the repository inspection and any previous audit, bug, AdMob, market, or feature findings from this task. If some findings are missing, inspect the repository and make clearly labeled assumptions instead of asking for repeat information.

Create a release-sized update plan.

What I want from you:
1. Separate must-fix, should-fix, and optional work.
2. Choose a small update goal.
3. Define user-facing changes.
4. Define technical changes.
5. Define ad and monetization changes.
6. Define analytics or Crashlytics changes.
7. Define tests and manual QA.
8. Define done criteria.
9. Create the first implementation task.

Rules:
- Keep the update small enough to finish.
- Fix serious bugs before adding new features.
- Do not mix too many unrelated changes.
- Prefer one clear product improvement per release.
- Do not ask for details already visible in the repository or previous outputs.

Expected output:
- Release goal.
- Scope list.
- Out-of-scope list.
- Implementation order.
- Test plan.
- Done criteria.
- First Codex implementation prompt.
```

## Prompt 8B: Release Scope Implementation

Use this after Prompt 8 when you want Codex to implement the approved release-sized update scope.

```text
You are implementing the approved release scope in the current Flutter repository.

Use the update scope decision from this task. If no approved release scope is available, first inspect the repository and create a small release-scope proposal, then ask me to approve that scope before editing.

What I want from you:
1. Re-read all files relevant to the approved release scope before editing.
2. Implement only the approved must-fix and should-fix items.
3. Keep optional items out unless explicitly approved.
4. Preserve existing behavior outside the release scope.
5. Keep changes small, reviewable, and release-oriented.
6. Add or update focused tests where useful.
7. Follow the Performance and Verification Rule for formatting, static analysis, tests, and builds.
8. Produce a short implementation summary and release QA checklist.

Rules:
- Do not rewrite unrelated files.
- Do not mix unrelated refactors into the release scope.
- Do not change app IDs, signing, production secrets, or release config unless explicitly approved.
- Keep AdMob test and production behavior safe.
- If an approved item becomes risky or larger than expected, stop and explain the tradeoff before continuing.
- Respect existing user changes.

Expected output:
- Approved release items implemented.
- Files changed.
- Tests or checks run.
- Manual release QA steps.
- Approved items deferred, if any.
- Remaining risks.
```

## Prompt 9: Focused Implementation Prompt

Use this only after the update scope is clear and no specific `B` prompt fits the work.

```text
You are implementing the approved focused update in the current Flutter repository.

First, inspect the relevant files. Use the update scope already agreed in this task. If the scope is not clear, create a short proposed scope from the latest audit findings and ask me to approve it before editing.

What I want from you:
1. Inspect the relevant files first.
2. Implement only the approved scope.
3. Follow the existing architecture and style.
4. Keep changes small and reviewable.
5. Add or update tests where useful.
6. Follow the Performance and Verification Rule for formatting, static analysis, tests, and builds.
7. Explain exactly what changed.

Rules:
- Do not rewrite unrelated files.
- Do not introduce new dependencies without a clear reason.
- Do not change app IDs, signing, production secrets, or release config unless explicitly requested.
- Keep AdMob test and production behavior safe.
- If verification cannot run, explain why.

Expected output:
- Files changed.
- Behavior changed.
- Tests or checks run.
- Manual QA steps.
- Remaining risks.
```

## Prompt 10: QA and Release Readiness

Use this after implementation and before uploading a build.

```text
You are checking release readiness for the current Flutter app after the latest changes.

Use `checklists/play-store-release-checklist.md` as the release gate. Inspect the repository directly to discover package name, version, build configuration, permissions, Firebase usage, AdMob usage, and test setup.

What I want from you:
1. Run or guide formatting, static analysis, and tests.
2. Confirm release versioning from the repository.
3. Review Firebase and AdMob configuration risk.
4. Review privacy, permissions, and Data safety impact.
5. Review store listing changes needed.
6. Create a manual QA checklist for this exact update.
7. Identify release blockers.
8. Recommend release, delay, or internal test first.

Rules:
- Do not ask for repository details that can be inspected directly.
- Do not claim release readiness if checks were not run.
- Mark unknowns clearly.
- Use current Google Play and AdMob requirements for policy-sensitive claims.
- Prefer internal or closed testing when risk is unclear.

Expected output:
- Checks run.
- Release blocker list.
- Manual QA checklist.
- Store listing update notes.
- Play Console notes.
- Release recommendation.
```

## Prompt 11: Post-Release Monitoring

Use this after an update goes live or enters testing.

```text
You are helping me monitor the current Flutter app after release or testing rollout.

First, inspect the repository and latest changes to identify the app, package, version, shipped changes, Firebase/Crashlytics setup, analytics setup, and AdMob setup. If release date, track, Crashlytics, Android vitals, Play reviews, analytics, or AdMob dashboard data is not available locally, ask only for those external monitoring summaries.

What I want from you:
1. Review stability signals.
2. Review user feedback.
3. Review ad health if monetized.
4. Identify whether rollout should continue, pause, or roll back.
5. Identify hotfix needs.
6. Create a 7-day monitoring checklist.
7. Recommend the next small improvement.

Rules:
- Do not ask for app identity details that can be found in the repository.
- Treat crashes, ANRs, policy warnings, and invalid traffic warnings as serious.
- Do not overreact to tiny data samples.
- Clearly separate facts from assumptions.
- Prefer measured next steps.

Expected output:
- Release health summary.
- Continue, pause, or hotfix recommendation.
- Missing external monitoring data, if any.
- 7-day monitoring checklist.
- Next improvement idea.
```

## Prompt 12: Learning Note

Use this after each update cycle.

```text
You are helping me write a learning note after improving the current Flutter app.

Use `templates/post-release-learning-note.md` if available. Inspect the repository, latest changes, version, release notes, and previous outputs in this task to infer what changed. If results, user feedback, revenue, or monitoring data are not available locally, ask only for those external results.

What I want from you:
1. Summarize what changed.
2. Summarize what improved.
3. Summarize what did not improve or is still unknown.
4. Capture mistakes to avoid next time.
5. Capture reusable code, process, or checklist lessons.
6. Recommend the next update or stop/monitor decision.

Rules:
- Do not ask for information already visible in the repository or previous task outputs.
- Be honest.
- Do not force a success story.
- Focus on lessons that help future apps.
- Keep it useful months later.

Expected output:
- A concise learning note.
- Reusable lessons.
- Missing external result data, if any.
- Next action recommendation.
```

## Quick Copy-Paste Commands

Use these when you do not want to paste the full prompt text:

```text
Run Prompt 2 from `prompts/existing-app-improvement-prompt-pack-v2.md` for the current repository.
```

```text
Run Prompt 3 from `prompts/existing-app-improvement-prompt-pack-v2.md` for the current repository.
```

```text
Run Prompt 3B from `prompts/existing-app-improvement-prompt-pack-v2.md` for the current repository, using the approved code review findings from this task.
```

```text
Run Prompt 4 from `prompts/existing-app-improvement-prompt-pack-v2.md` for the current repository.
```

```text
Run Prompt 4B from `prompts/existing-app-improvement-prompt-pack-v2.md` for the current repository, using the approved bug triage findings from this task.
```

```text
Run Prompt 5 from `prompts/existing-app-improvement-prompt-pack-v2.md` for the current repository.
```

```text
Run Prompt 5B from `prompts/existing-app-improvement-prompt-pack-v2.md` for the current repository, using the approved AdMob audit findings from this task.
```

```text
Run Prompt 6 from `prompts/existing-app-improvement-prompt-pack-v2.md` for the current repository.
```

```text
Run Prompt 6B from `prompts/existing-app-improvement-prompt-pack-v2.md` for the current repository, using the approved store listing and ASO findings from this task.
```

```text
Run Prompt 7 from `prompts/existing-app-improvement-prompt-pack-v2.md` for the current repository.
```

```text
Run Prompt 7B from `prompts/existing-app-improvement-prompt-pack-v2.md` for the current repository, using the approved feature scope from this task.
```

```text
Run Prompt 8 from `prompts/existing-app-improvement-prompt-pack-v2.md` for the current repository.
```

```text
Run Prompt 8B from `prompts/existing-app-improvement-prompt-pack-v2.md` for the current repository, using the approved release scope from this task.
```

```text
Run Prompt 9 from `prompts/existing-app-improvement-prompt-pack-v2.md` for the current repository, using the approved scope from this task, only if no specific B prompt fits the work.
```

## Portfolio Done Criteria

The portfolio improvement system is working when:

- Each app has a clear status.
- The best apps are improved first.
- Bugs and crashes are fixed before cosmetic changes.
- Ads are useful, safe, and policy-conscious.
- Each update has a small goal.
- Store listings match the real app.
- Data safety and privacy answers match actual behavior.
- Releases are tested before production.
- Every update creates a learning note.

## Common Mistakes

- Trying to fix all 15 apps at the same time.
- Adding features before reviewing crashes and reviews.
- Optimizing ad revenue before checking policy and user experience.
- Copying competitor features without understanding the user problem.
- Doing a full rewrite instead of a focused update.
- Shipping without checking release build behavior.
- Forgetting to update Data safety after SDK or data behavior changes.
- Ignoring post-release monitoring.
