# Game Production Ready Prompt Pack

Use this prompt pack after a game-specific prompt process has produced a playable prototype.

This pack turns a prototype into a small, polished, production-ready version 1: enough content, polished UI, AdMob, analytics, store assets, release QA, and post-release monitoring.

## Purpose

Create publishable Flutter games without overbuilding.

The goal is not a huge game. The goal is a complete version 1 that feels intentional, works reliably, has enough content for real users, uses ads safely, and is ready for Play Store testing.

## When to Use

Use this after the game-specific process has completed:

- Concept.
- Game design.
- Technical architecture.
- First playable prototype.
- Prototype quality review.

Do not use this before the core game loop is playable.

## Production V1 Standard

Every game must reach this standard before publishing:

- Core loop is playable and understandable.
- UI is polished enough for real users.
- Navigation, restart, pause/settings, sound/haptics toggles, and basic accessibility are handled.
- Game logic is tested where practical.
- Enough content exists for a real first release.
- AdMob is implemented with test/prod separation.
- Ads never interrupt active gameplay.
- Frequency caps exist before interstitial ads are used.
- Firebase Analytics or equivalent event tracking is implemented if the app uses analytics.
- Crash monitoring is planned or implemented before production release.
- ASO-friendly app display name is chosen before store asset production.
- Final package name follows the approved `com.childhood.<game_slug>` convention before Play Store upload.
- Store listing assets show real gameplay.
- Release checklist is completed before Play Store upload.

## Naming and Package Convention

Use this convention for every new game unless explicitly approved otherwise:

- Store/display name: ASO-friendly, human-readable, truthful, and not keyword-stuffed.
- Package name/application ID: `com.childhood.<game_slug>`.
- `<game_slug>` should be lowercase ASCII, start with a letter, and use letters/numbers only where practical.
- Do not use spaces, hyphens, emojis, punctuation, or generic words alone in the package slug.
- Do not use real brands, official team names, copyrighted characters, or misleading keywords in the name or package.
- Keep display name and package name separate. The display name can be keyword-friendly; the package name should be stable and clean.
- Treat the package name as permanent after Play Store publishing. Changing it later normally means creating a new app listing.

Examples:

| Game | ASO-friendly display name idea | Package name |
| --- | --- | --- |
| Pen Cricket | Pen Cricket: Spin & Score | `com.childhood.pencricket` |
| Emoji Chor-Police | Emoji Chor Police Party Game | `com.childhood.emojichorpolice` |
| Sholo Guti | Sholo Guti: 16 Beads Game | `com.childhood.shologuti` |
| Dots and Boxes | Dots and Boxes: Board Game | `com.childhood.dotsandboxes` |
| Water Sort | Water Sort Puzzle Game | `com.childhood.watersort` |

## Suggested Minimum Content Targets

Use these as practical release targets, not permanent limits:

- Tic tac toe: local two-player, one AI mode, polished UI, score/session history, and at least one optional variant or difficulty improvement.
- Water sort puzzle: 50-100 solvable levels.
- Triple tile match: 50-100 solvable levels.
- Bubble shooter: 40-80 playable levels.
- Match puzzle: 40-80 playable levels.
- Crowd-control arcade: 30-50 playable levels.
- Space shooter: survival mode plus 20-30 waves or equivalent mission content.
- Snake arena: offline bot arena plus 20-30 missions, objectives, or difficulty milestones.
- Farming life: 30 progression steps, 6-10 crops, save/restore, and at least one meaningful upgrade path.
- Emoji Chor-Police: single-player vs 3 AI bots, 4-player pass-and-play, 5-10 round match presets, local score history, and 20-30 achievements or challenge goals.
- Sholo Guti: validated 37-node board graph, local two-player, player vs bot, move/capture validation tests, match history, and optional hints or undo.
- Dots and Boxes: local two-player, player vs bot, 3-4 grid presets, line/box/extra-turn validation tests, match history, and optional hints or undo.
- Arrow puzzle or other simple puzzle: 50-100 levels depending on level length.

If the game is unusually complex, reduce content count but increase polish and QA. If the game is very simple, increase content count or add one small replayable mode.

## Performance Rule

Do not run heavy commands by default.

- For planning and review: inspect files only.
- For implementation: run formatter on changed files and targeted tests where practical.
- Run full analysis, Gradle, build, install, emulator, or release packaging only when explicitly requested or required for release readiness.
- If a heavy check is skipped, explain the remaining risk.

## Prompt P1: Production V1 Scope Lock

Use this after the first playable prototype and prototype review.

```text
You are turning the current Flutter game prototype into a production-ready version 1.

Use the game-specific prompt process, current repository, prototype implementation, and prior review findings from this task.

Do not edit files yet.

What I want from you:
1. Identify the exact game type and current prototype status.
2. Define the production v1 content target.
3. Define the polished UI requirements.
4. Define required gameplay fixes before release.
5. Define required level/content work.
6. Define required AdMob and analytics work.
7. Propose 3-5 ASO-friendly display name options.
8. Propose the final package name using `com.childhood.<game_slug>`.
9. Define required store asset work.
10. Define release blockers.
11. Create a small production v1 scope.
12. Create implementation order.

Rules:
- Keep version 1 small but complete.
- Do not add unrelated features.
- Do not add online multiplayer, login, live events, complex shop, or cloud sync unless explicitly approved.
- Ads must not interrupt active gameplay.
- User trust and Play policy safety come before revenue.
- Display name must be truthful and not keyword-stuffed.
- Package name must be stable, lowercase, and follow `com.childhood.<game_slug>` unless I approve another convention.
- Wait for approval before implementation.

Expected output:
- Production v1 scope.
- Required content target.
- Polished UI checklist.
- ASO name options.
- Recommended package name.
- AdMob and analytics checklist.
- Store asset checklist.
- Release blocker list.
- Implementation order.
```

## Prompt P2: Production UI and Game Polish Implementation

Use this after approving the production v1 scope.

```text
You are implementing production UI and gameplay polish for the current Flutter game.

Use the approved production v1 scope from this task.

What I want from you:
1. Re-read relevant UI, game, state, audio, settings, and asset files.
2. Improve only approved UI and gameplay polish items.
3. Add or improve main menu, game screen, pause/restart, settings, result screen, and empty/error states where needed.
4. Add sound/haptic toggles if approved.
5. Improve visual feedback for core actions.
6. Improve small-screen readability.
7. Add focused tests where practical.
8. Follow the Performance Rule for verification.

Rules:
- Do not change unrelated files.
- Do not add new visual systems or dependencies unless approved.
- Do not add monetization in this prompt unless explicitly included in the approved scope.
- Preserve existing game behavior unless fixing approved issues.

Expected output:
- Polish implemented.
- Files changed.
- Tests or checks run.
- Manual QA checklist.
- Remaining risks.
```

## Prompt P3: Production Content and Level Implementation

Use this to add enough content for release.

```text
You are implementing production v1 content for the current Flutter game.

Use the approved production v1 content target from this task.

What I want from you:
1. Re-read level, content, progression, save, and game logic files.
2. Add enough levels, waves, missions, AI modes, crops, progression steps, or equivalent content for version 1.
3. Keep content original and consistent with the game theme.
4. Make sure content difficulty ramps gradually.
5. Add validation or tests where practical.
6. Do not add monetization in this prompt unless explicitly approved.
7. Follow the Performance Rule for verification.

Rules:
- Do not copy levels, maps, layouts, tile sets, waves, or progression from other games.
- Do not add content that the UI cannot explain.
- Do not add too many systems at once.
- Prefer shippable content over experimental complexity.

Expected output:
- Content added.
- Content count.
- Difficulty progression summary.
- Files changed.
- Tests or checks run.
- Manual QA checklist.
- Remaining risks.
```

## Prompt P4: AdMob and Analytics Implementation

Use this only after the core game and content are stable enough for monetization.

```text
You are implementing production-safe AdMob and analytics for the current Flutter game.

Use the approved monetization and analytics scope from this task.

What I want from you:
1. Re-read ad, analytics, app config, game flow, settings, and result screen files.
2. Implement AdMob only in approved placements.
3. Keep test ads and production ads safely separated.
4. Add frequency caps before interstitials.
5. Make ad loading failure non-blocking.
6. Add analytics events needed to measure gameplay, level/content difficulty, retention, and ad impact.
7. Add privacy/Data safety notes if repo has release docs.
8. Follow the Performance Rule for verification.

Rules:
- Do not show ads during active gameplay.
- Do not encourage ad clicks.
- Do not reward ad clicks.
- Rewarded ads may reward optional value such as continue, hint, extra moves, bonus coins, revive, or speed-up only when approved.
- Interstitial ads may appear only at natural transitions such as level end, game over, or session break.
- User experience and policy safety come before revenue.
- Do not change production IDs, signing, package name, or release config unless this is a new unpublished app and I explicitly approve it.

Expected output:
- AdMob implemented.
- Analytics implemented.
- Ad placements.
- Frequency caps.
- Files changed.
- Tests or checks run.
- Manual ad QA checklist.
- Data safety notes.
- Remaining risks.
```

## Prompt P5: Store Assets and Listing Production

Use this when the game has real visuals and content.

```text
You are preparing Play Store listing assets for the current production-ready Flutter game.

Use `prompts/play-store-creative-assets-prompt-pack.md` if available.

What I want from you:
1. Inspect the current game screens and real gameplay.
2. Confirm the approved ASO-friendly display name.
3. Confirm the final package name follows `com.childhood.<game_slug>`.
4. Create or update store listing copy.
5. Create screenshot storyboard based on real gameplay.
6. Create feature graphic brief or asset.
7. Create app icon brief or asset.
8. Create preview video script or production package.
9. Prepare final Play Console upload checklist.

Rules:
- Do not fake gameplay.
- Do not show unavailable features.
- Do not use fake rankings, fake awards, fake reviews, fake downloads, or fake earnings.
- Do not keyword-stuff the app name or descriptions.
- Do not use unauthorized real brands, official teams, copyrighted characters, or misleading affiliation claims.
- Keep claims truthful and policy-safe.
- Do not publish anything.

Expected output:
- Approved display name.
- Final package name.
- Store listing package.
- Screenshot plan or assets.
- Feature graphic plan or asset.
- App icon plan or asset.
- Preview video package.
- Upload checklist.
- Remaining risks.
```

## Prompt P6: Production Release Readiness

Use this before uploading to Play Console.

```text
You are checking production release readiness for the current Flutter game.

Use `checklists/play-store-release-checklist.md` if available.

What I want from you:
1. Review production v1 scope completion.
2. Review gameplay/content readiness.
3. Review UI polish readiness.
4. Review approved display name and package name readiness.
5. Review AdMob and analytics readiness.
6. Review privacy, permissions, and Data safety impact.
7. Review store listing assets readiness.
8. Review tests and verification status.
9. Identify release blockers.
10. Recommend internal test, closed test, delay, or production submission.

Rules:
- Do not claim release readiness if required checks were not run.
- Mark skipped checks and remaining risk clearly.
- Prefer internal or closed testing if risk is unclear.
- Do not publish anything.

Expected output:
- Release readiness report.
- Display name and package name check.
- Blocker list.
- Manual QA checklist.
- Play Console checklist.
- Final recommendation.
```

## Quick Copy-Paste Sequence

```text
Run Prompt P1 from `prompts/game-production-ready-prompt-pack.md` for the current repository.
```

After approving the production v1 scope:

```text
Run Prompt P2 from `prompts/game-production-ready-prompt-pack.md` for the current repository, using the approved production v1 scope.
```

```text
Run Prompt P3 from `prompts/game-production-ready-prompt-pack.md` for the current repository, using the approved content target.
```

```text
Run Prompt P4 from `prompts/game-production-ready-prompt-pack.md` for the current repository, using the approved AdMob and analytics scope.
```

```text
Run Prompt P5 from `prompts/game-production-ready-prompt-pack.md` for the current repository.
```

```text
Run Prompt P6 from `prompts/game-production-ready-prompt-pack.md` for the current repository.
```

## Done Criteria

The game is production-ready when:

- Core gameplay is complete.
- UI feels polished and consistent.
- Enough content exists for version 1.
- ASO-friendly display name is approved.
- Package name follows `com.childhood.<game_slug>` before publishing.
- AdMob and analytics are implemented safely.
- Ads do not harm active gameplay.
- Store assets are truthful and based on real gameplay.
- Release checklist is complete.
- Internal or closed testing plan is ready.
