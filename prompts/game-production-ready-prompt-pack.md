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

## Strict One-Phase Execution Rule

Do not ask Codex to run all production prompts in one message.

One prompt should have one job, one output, and one verification target. Run a phase, review the result, then run the next phase. This is slower than one giant prompt, but it produces better games because Codex is not trying to fix gameplay, UI, sound, content, ads, screenshots, and release risk at the same time.

Recommended six assigned tasks:

| Task | Owner Prompt | Job | Do Not Mix With |
| --- | --- | --- | --- |
| 1 | P1 | Audit, scope, blockers, ASO/package decision | Code edits |
| 2 | P2 | Core gameplay, controls, architecture blockers, main flow | Ads, store assets |
| 3 | P2B | Professional hub/dashboard, visual feel, sound triggers, replay hook | Content bulk, ads |
| 4 | P3 | Content, missions, rounds, progression, replay goals | UI redesign, ads |
| 5 | P2C | Visual gameplay iteration using screenshots, recording, or manual play notes | New features, ads |
| 6 | P4 then P5/P6 | AdMob, analytics, store asset readiness, release gate | Gameplay redesign |

If Task 5 proves the game still feels weak, go back to Task 3 or Task 4 instead of moving to ads or store assets.

## 95% Game Feel Gate

Use this gate when the goal is a professional game with high confidence.

Codex may not claim "95%+ real game feel" from code inspection alone. A 95% score requires evidence from at least one of these:

- Real screenshots from the app.
- A 15-30 second gameplay recording.
- Live app output inspected by Codex.
- Manual play notes from the owner after playing the game.

Score the game out of 100:

| Area | Points |
| --- | ---: |
| First 10 seconds are clear and compelling | 15 |
| Professional visual UI, home/dashboard, HUD, and result screens | 20 |
| Controls, touch feedback, input tolerance, and small-screen usability | 15 |
| Core gameplay fun, challenge, replay hook, and progression motivation | 20 |
| Sound/haptic feedback triggers during real gameplay and respects settings | 10 |
| Content/modes/progression feel sufficient for v1 | 10 |
| Screenshot readiness and store-facing presentation | 10 |

Decision:

- `95-100`: pass; move to AdMob/store/release checks.
- `85-94`: not enough; run one more P2C iteration or go back to P2B/P3 for targeted fixes.
- `<85`: rescue required; go back to P2B before content, ads, or store assets.
- `N/A`: no real visual/play evidence; do not claim 95% confidence.

## Production V1 Standard

Every game must reach this standard before publishing:

- Core loop is playable and understandable.
- UI is polished enough for real users.
- The game looks like a serious mobile game, not a generic template or unfinished demo.
- Home/dashboard flow is useful and game-specific, not just a weak menu or forced level list.
- Controls are discoverable, responsive, forgiving, and comfortable on small screens.
- Animations improve clarity and game feel without delaying play.
- Lightweight feedback sounds and haptics are triggered during important gameplay moments, not only exposed as settings.
- The first-time user can understand what to do without reading long instructions.
- Progression, challenge, reward, or replay hooks make the game interesting enough to keep playing.
- At least one visual/gameplay iteration has been completed using screenshots, screen recording, manual play notes, or explicit skipped-check risks.
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
- Store listing screenshots, icon, feature graphic, and video package are created or explicitly blocked with exact missing inputs.
- Release checklist is completed before Play Store upload.

## Naming and Package Convention

Use this convention for every new game unless an existing published package name must be preserved:

- Store/display name: ASO-friendly, human-readable, truthful, and not keyword-stuffed.
- Keep the display name short: usually 2-5 words and under 30 characters where practical.
- Avoid long colon-heavy names unless the subtitle clearly improves search and readability.
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

## Professional Game Quality Standard

Do not accept a game that feels like a class project, template clone, or raw prototype.

- Define a clear art direction before editing: color palette, typography, shape language, icon style, motion style, and screen density.
- The first screen should feel like a real game hub: Continue/Play, mode or mission entry, rewards/progress, settings, help, and any useful stats/history.
- Do not force every game into a generic "levels" section. Use the right structure for the genre: quick play, missions, worlds, challenges, waves, rounds, practice, daily/local challenge, campaign, or endless mode.
- Every visible dashboard button must do something useful. No dead cards, placeholder counters, fake rewards, or decorative-only feature panels.
- Gameplay should have at least one engagement hook: combo, streak, target score, star rating, unlock, mission goal, achievement, high score, collection, upgrade, or escalating challenge.
- Result screens should create the next play impulse: retry, next challenge, improve score, unlock reward, continue streak, or change mode.
- Sound/haptic feedback must be wired into actual gameplay actions. Do not claim sound is done if only toggles or service stubs exist.
- If built-in `SystemSound` is not reliable for the target platform, use the smallest practical reliable audio approach and report the choice.
- Store screenshots should have screenshot-ready game states. If actual captures are not available, do not fake them; create exact capture steps or approved production templates.

## Iteration and Visual Gameplay Checking Standard

Code inspection alone cannot prove that a game feels good.

- After P2/P2B and P3, complete at least one visual/gameplay feedback loop before moving to ads or store assets.
- Best inputs are real screenshots, a 15-30 second screen recording, or direct manual play notes from the owner.
- If no screenshots, recording, emulator, or manual play notes are available, mark visual/gameplay feel as not verified. Do not claim the game has real commercial feel.
- Use a tight loop: observe the actual screen/play evidence, list the top feel problems, fix the highest-impact 3-5 issues, then define what must be checked again.
- Check the first 10 seconds, first run/round/level, win state, loss state, retry/next flow, pause/settings, sound toggle, and one small-screen layout.
- Sound and haptics must be checked by triggering real gameplay events, not just by reading service code.
- If visual capture or gameplay verification requires `flutter run`, emulator, device capture, or build commands, run only the smallest practical command needed.
- If heavy checks are skipped, list the exact visual/gameplay risks that remain.

## Game Feel and UX Standard

Every game should feel good before adding ads or store assets.

- First useful action should be obvious within 3-5 seconds.
- Main menu should get the player into gameplay in 1-2 taps.
- Home/dashboard should be genre-specific and useful, not a generic grid of menu cards.
- Level selection should exist only when it improves the game. For arcade, board, sports, endless, party, or farming games, prefer mode selection, missions, challenges, rounds, upgrades, or continue/play flows where better.
- Core controls should be large enough for touch and forgiving of small mistakes.
- Touch/drag/tap feedback should be immediate.
- Important actions need clear visual feedback: valid move, invalid move, score, win, loss, reward, error, retry.
- Important gameplay moments need lightweight sound/haptic feedback: tap/select, valid action, invalid action, score/capture/reward, win, and loss.
- Use built-in or system feedback first, such as Flutter `SystemSound` and `HapticFeedback`, or an existing local feedback helper.
- Avoid custom audio assets, sound packs, background music, and new audio dependencies unless they are needed for reliable gameplay feedback.
- Animations should be short, meaningful, and consistent. Avoid slow decorative animation that blocks repeated play.
- Gameplay should include satisfying micro-rewards such as punchy transitions, score bursts, combo/streak feedback, unlock feedback, or clear progress movement.
- Result screens should make the next action obvious: retry, next level, continue, home.
- Tutorial/onboarding should be minimal, skippable where practical, and available again from settings/help.
- UI text must fit on small screens and not overlap gameplay.
- Sound and haptics should default to sensible feedback during play, respect toggles/mute behavior, and never block gameplay if feedback fails.
- Color should not be the only way to understand state.
- Ad placements must never break the rhythm of a turn, level, move, shot, spin, reveal, or active session.

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

## Fast Execution and Verification Rule

Do not run slow or environment-changing commands by default, but run the smallest essential command when implementation or verification genuinely requires it. Standing authority is already granted for all work within the approved production v1 scope; do not pause to ask for approval.

For planning and review, inspect files only.

Skip these by default unless the task cannot be completed or verified without them:

- `flutter pub get`
- `dart pub get`
- `flutter run`
- `flutter build`
- `flutter install`
- `flutter analyze`
- full `flutter test`
- Gradle build tasks
- Android/iOS release packaging
- emulator/device launch
- dependency upgrade commands
- generated asset recapture that requires running the app

Allowed lightweight checks:

- Static file inspection with `rg`, `Get-Content`, and targeted reads.
- Formatting only changed files when practical.
- Targeted unit tests only when dependencies are already available and the test is important for modified game logic.
- Lightweight code or config validation that does not download dependencies or launch a device.

If a skipped heavy command would improve confidence, list it under `Skipped heavy checks` with the exact command and why it was skipped.

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
4. Define whether the home/dashboard currently feels professional or amateur.
5. Define the correct genre-specific progression structure. Do not default to a level list.
6. Define required animation, control, sound, and game-feel fixes.
7. Define required gameplay and engagement-loop fixes before release.
8. Define required content, modes, missions, waves, rounds, challenges, or levels.
9. Define required AdMob and analytics work.
10. Propose 3-5 short ASO-friendly display name options.
11. Propose the final package name using `com.childhood.<game_slug>`.
12. Define required store asset work, including screenshot generation or capture blockers.
13. Define release blockers.
14. Create a small production v1 scope.
15. Create implementation order.

Rules:
- Keep version 1 small but complete.
- Do not add unrelated features.
- Do not add online multiplayer, login, live events, complex shop, or cloud sync unless essential to the documented production v1 scope.
- Ads must not interrupt active gameplay.
- User trust and Play policy safety come before revenue.
- Display name must be short, truthful, ASO-friendly, and not keyword-stuffed.
- Package name must be stable, lowercase, and follow `com.childhood.<game_slug>` unless an existing published package name must be preserved.
- Do not run `flutter pub get`, `dart pub get`, `flutter run`, `flutter build`, full `flutter analyze`, full `flutter test`, Gradle, install, emulator, or release packaging unless essential.
- This prompt is audit-only. Proceed to P2 without requesting approval once it has produced the scope.

Expected output:
- Production v1 scope.
- Required content target.
- Polished UI checklist.
- Professional game quality checklist.
- Game feel and animation checklist.
- Genre-specific progression recommendation.
- ASO name options.
- Recommended package name.
- AdMob and analytics checklist.
- Store asset checklist.
- Release blocker list.
- Implementation order.
- Skipped heavy checks.
```

## Prompt P2: Production UI, Animation, and Game Feel Implementation

Use this after approving the production v1 scope.

```text
You are implementing production UI, animation, game feel, and gameplay polish for the current Flutter game.

Use the production v1 scope from this task. All scope items needed for production v1 are already authorized.

What I want from you:
1. Re-read relevant UI, game, state, audio, settings, and asset files.
2. Create a short UX/game-feel checklist before editing.
3. Improve only approved UI, animation, control, and gameplay polish items.
4. Make the main flow user-friendly: open app, start game, understand goal, act, retry/next/home.
5. Replace weak dashboard/menu UX with a professional game hub that fits this genre.
6. Avoid generic level-list UX unless the game truly needs it; choose mode, mission, challenge, world, endless, rounds, or continue/play flow where better.
7. Improve controls, tap targets, drag areas, hit testing, input tolerance, and invalid-action feedback.
8. Improve meaningful animations for core actions, movement, scoring, win/loss, rewards, errors, and transitions.
9. Add replay motivation through small hooks such as score chase, combo/streak, missions, stars, achievements, unlocks, upgrades, or escalating challenge.
10. Add or improve main menu, game screen, pause/restart, settings/help, result screen, and empty/error states where needed.
11. Add lightweight built-in feedback sounds and haptics for core gameplay moments without custom audio assets or new audio dependencies.
12. Improve visual hierarchy, HUD readability, contrast, spacing, and small-screen layout.
13. Add simple onboarding, tooltips, first-run hints, or help screen where the game is not self-explanatory.
14. Add or improve sound/haptic toggles in settings, and make sure feedback respects them.
15. Add focused tests where practical.
16. Follow the Fast Execution and Verification Rule.

Rules:
- Do not change unrelated files.
- Avoid new visual systems or dependencies unless they are needed to complete production v1.
- Do not add monetization in this prompt; P4 owns monetization.
- Preserve existing game behavior unless fixing production v1 issues.
- Do not ship a childish, template-like, or placeholder-looking UI.
- Do not use a generic level screen for every game.
- Do not add slow decorative animation that blocks repeated play.
- Avoid custom audio assets, sound packs, background music, or new audio dependencies unless needed for reliable gameplay feedback.
- Use Flutter/platform feedback first, such as `SystemSound` and `HapticFeedback`, or the repository's existing feedback service.
- Do not hide essential controls or make the user guess what to do.
- Do not let text, buttons, ads, HUD, or dialogs overlap active gameplay.
- Keep gameplay rhythm more important than visual decoration.
- Do not run `flutter pub get`, `flutter run`, `flutter build`, full `flutter analyze`, full `flutter test`, Gradle, install, emulator, or release packaging unless essential.

Expected output:
- UX/game-feel checklist.
- Professional UI and hub changes.
- Polish implemented.
- Animation and feedback changes.
- Feedback sound/haptic coverage.
- Engagement/replay hook changes.
- Files changed.
- Tests or checks run.
- Skipped heavy checks.
- Manual QA checklist.
- Remaining risks.
```

## Prompt P2B: Professional Game Vibe Rescue Pass

Use this if Prompt P2 was implemented but the game still feels amateur, boring, or not screenshot-ready.

```text
You are doing a professional game vibe rescue pass for the current Flutter game.

The previous implementation still feels too generic, childish, boring, or prototype-like. Inspect the current repository directly and fix only production v1 polish and gameplay issues. All required changes are authorized.

What I want from you:
1. Identify the top 10 reasons the game does not feel like a real mobile game yet.
2. Fix the home/dashboard so it feels useful, polished, and genre-specific.
3. Remove or replace generic "levels" UX where a better mode, mission, challenge, round, endless, campaign, or continue flow fits the game.
4. Improve the core gameplay loop so the player has a reason to keep playing.
5. Add or improve small reward loops: combo, streak, score chase, stars, missions, achievements, unlocks, progression, or high-score goals where appropriate.
6. Make controls and touch feedback feel immediate and forgiving.
7. Wire lightweight sound/haptic feedback into real gameplay events and settings.
8. Improve result screens so retry/next/continue feels natural.
9. Make at least 4 screenshot-ready moments or screens exist in the app.
10. Keep changes small enough for one developer to review.
11. Follow the Fast Execution and Verification Rule.

Rules:
- Do not add AdMob in this prompt.
- Do not add login, online multiplayer, complex backend, cloud sync, or heavy economy systems.
- Do not add fake rewards, fake rankings, fake online opponents, or unavailable store claims.
- If sound cannot work reliably with built-in feedback, add the smallest practical local audio approach and report it.
- Do not touch unrelated files.
- Do not run `flutter pub get`, `flutter run`, `flutter build`, full `flutter analyze`, full `flutter test`, Gradle, install, emulator, or release packaging unless essential.

Expected output:
- Top 10 amateur-feel causes found.
- Professional hub/dashboard changes.
- Gameplay engagement changes.
- Sound/haptic trigger coverage.
- Screenshot-ready screens created or improved.
- Files changed.
- Tests or checks run.
- Skipped heavy checks.
- Remaining risks.
```

## Prompt P2C: Visual Gameplay Iteration and Feel Check

Use this after P2 or P2B when the game must be judged by actual user-facing feel, not code completion.

```text
You are doing a visual gameplay iteration and feel check for the current Flutter game.

Use the current repository plus any screenshots, screen recording, manual play notes, QA notes, or previous findings in this task.

If screenshots, recording, or manual play notes are available, use them as the highest-priority evidence. If none are available, run the smallest practical visual check when possible; otherwise continue with code/UI inspection and clearly mark visual gameplay feel as not verified.

What I want from you:
1. Review the first 10 seconds of the player experience from available evidence.
2. Review the home/dashboard, first play entry, core gameplay screen, pause/settings, result screen, and retry/next flow.
3. Judge whether the game looks professional, fun, readable, and screenshot-ready.
4. Check whether gameplay has a clear reason to continue: score chase, combo, streak, mission, stars, unlock, achievement, progression, or escalating challenge.
5. Check whether sounds and haptics trigger from real gameplay events and respect settings.
6. Score the game using the 95% Game Feel Gate.
7. Identify the top 5-10 visual/gameplay feel problems.
8. Fix the highest-impact 3-5 issues only.
9. Create a before/after verification checklist for the owner to manually check.
10. Stop after one focused iteration and report the next targeted iteration if the score is still below 95.
11. Follow the Fast Execution and Verification Rule.

Rules:
- Do not claim real game feel is verified unless you inspected screenshots, recording, live app output, or manual play evidence.
- Do not claim a 95%+ score unless real visual/play evidence was used.
- Do not run `flutter pub get`, `flutter run`, `flutter build`, full `flutter analyze`, full `flutter test`, Gradle, install, emulator, or device capture unless essential.
- When visual capture is essential, run only the smallest practical command needed to capture evidence.
- Do not add AdMob, new monetization, login, cloud sync, fake online features, or unrelated systems.
- Add a minimal local audio dependency only when built-in feedback cannot provide reliable gameplay sound; report the change.
- Keep changes focused and reviewable.

Expected output:
- Evidence used: screenshots, recording, manual notes, live run, or code-only.
- Visual/gameplay feel verdict.
- 95% Game Feel Gate score and pass/iterate/rescue decision.
- Top feel problems found.
- Fixes implemented this iteration.
- Sound/haptic verification status.
- Screenshot-readiness status.
- Files changed.
- Tests or checks run.
- Skipped heavy checks.
- Next manual play checklist.
- Remaining risks.
```

## Prompt P3: Production Content and Level Implementation

Use this to add enough content for release.

```text
You are implementing production v1 content for the current Flutter game.

Use the production v1 content target from this task. The required content work is authorized.

What I want from you:
1. Re-read level, content, progression, save, and game logic files.
2. Add enough genre-appropriate content: levels, waves, missions, rounds, boards, AI modes, crops, progression steps, challenges, achievements, or equivalent content for version 1.
3. Keep content original and consistent with the game theme.
4. Make sure content difficulty ramps gradually.
5. Add replayable goals where appropriate so the game is not only a one-time content list.
6. Add validation or tests where practical.
7. Do not add monetization in this prompt; P4 owns monetization.
8. Follow the Fast Execution and Verification Rule.

Rules:
- Do not copy levels, maps, layouts, tile sets, waves, or progression from other games.
- Do not force a visible level section if the game is better with quick play, missions, rounds, waves, challenges, endless mode, or progression.
- Do not add content that the UI cannot explain.
- Do not add too many systems at once.
- Prefer shippable content over experimental complexity.
- Do not run `flutter pub get`, `flutter run`, `flutter build`, full `flutter analyze`, full `flutter test`, Gradle, install, emulator, or release packaging unless essential.

Expected output:
- Content added.
- Content count.
- Difficulty progression summary.
- Replay/progression summary.
- Files changed.
- Tests or checks run.
- Skipped heavy checks.
- Manual QA checklist.
- Remaining risks.
```

## Prompt P4: AdMob and Analytics Implementation

Use this only after the core game and content are stable enough for monetization.

```text
You are implementing production-safe AdMob and analytics for the current Flutter game.

Use the production v1 monetization and analytics scope from this task. All safe in-repository implementation work is authorized.

What I want from you:
1. Re-read ad, analytics, app config, game flow, settings, and result screen files.
2. Implement AdMob only in user-friendly, policy-safe placements documented in the scope.
3. Keep test ads and production ads safely separated.
4. Add frequency caps before interstitials.
5. Make ad loading failure non-blocking.
6. Add analytics events needed to measure gameplay, level/content difficulty, retention, and ad impact.
7. Add privacy/Data safety notes if repo has release docs.
8. Follow the Fast Execution and Verification Rule.

Rules:
- Do not show ads during active gameplay.
- Do not encourage ad clicks.
- Do not reward ad clicks.
- Rewarded ads may reward optional value such as continue, hint, extra moves, bonus coins, revive, or speed-up only when documented and policy-safe.
- Interstitial ads may appear only at natural transitions such as level end, game over, or session break.
- User experience and policy safety come before revenue.
- Never invent production ad IDs or signing credentials. Preserve existing production IDs and release configuration; use safe test/configuration paths where values are unavailable.
- Do not run `flutter pub get`, `flutter run`, `flutter build`, full `flutter analyze`, full `flutter test`, Gradle, install, emulator, or release packaging unless essential.

Expected output:
- AdMob implemented.
- Analytics implemented.
- Ad placements.
- Frequency caps.
- Files changed.
- Tests or checks run.
- Skipped heavy checks.
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
2. Select and confirm an ASO-friendly display name.
3. Confirm the final package name follows `com.childhood.<game_slug>`.
4. Create or update store listing copy.
5. Create screenshot storyboard based on real gameplay.
6. Create final screenshot assets when real UI evidence can be captured; otherwise create source templates and report the exact capture blocker.
7. Create feature graphic brief or asset.
8. Create app icon brief or asset.
9. Create preview video script or production package.
10. Prepare final Play Console upload checklist.

Rules:
- Do not fake gameplay.
- Do not show unavailable features.
- Do not use fake rankings, fake awards, fake reviews, fake downloads, or fake earnings.
- Do not keyword-stuff the app name or descriptions.
- Do not use unauthorized real brands, official teams, copyrighted characters, or misleading affiliation claims.
- Keep claims truthful and policy-safe.
- Do not silently skip screenshots. Either create assets, create source templates, or list the exact screenshot capture blocker.
- Do not run `flutter pub get`, `flutter run`, `flutter build`, install, emulator, or device screenshot capture unless essential.
- Do not publish anything.

Expected output:
- Selected display name.
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
4. Review display name and package name readiness.
5. Review AdMob and analytics readiness.
6. Review privacy, permissions, and Data safety impact.
7. Review store listing assets readiness.
8. Review the latest P2C 95% Game Feel Gate score and evidence.
9. Review tests and verification status.
10. Identify release blockers.
11. Recommend internal test, closed test, delay, or production submission.

Rules:
- Do not claim release readiness if required checks were not run.
- Do not recommend store asset production, AdMob rollout, or release if the latest real-evidence game feel score is below 95.
- Mark skipped checks and remaining risk clearly.
- Prefer internal or closed testing if risk is unclear.
- Do not run `flutter pub get`, `flutter run`, `flutter build`, full `flutter analyze`, full `flutter test`, Gradle, install, emulator, or release packaging unless essential.
- Do not publish anything.

Expected output:
- Release readiness report.
- Latest 95% Game Feel Gate score and evidence.
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

After P1 completes:

```text
Run Prompt P2 from `prompts/game-production-ready-prompt-pack.md` for the current repository, using the P1 production v1 scope. All required production v1 work is already authorized.
```

If the game still feels amateur after P2:

```text
Run Prompt P2B from `prompts/game-production-ready-prompt-pack.md` for the current repository. The current result still feels amateur; fix professional hub/dashboard UX, game feel, replay hooks, sound triggers, and screenshot-ready screens.
```

```text
Run Prompt P3 from `prompts/game-production-ready-prompt-pack.md` for the current repository, using the P1 content target. All required production v1 work is already authorized.
```

After P2/P2B and P3, use actual screenshots, recording, or manual play notes for one feel iteration:

```text
Run Prompt P2C from `prompts/game-production-ready-prompt-pack.md` for the current repository. Use available screenshots, screen recording, or my manual play notes to do one visual gameplay feel iteration. If no visual evidence is available, mark real game feel as not verified and list exact manual checks.
```

```text
Run Prompt P4 from `prompts/game-production-ready-prompt-pack.md` for the current repository, using the P1 AdMob and analytics scope. All safe in-repository work is already authorized.
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
- UI feels polished, commercial, and game-specific.
- Home/dashboard is useful and not a generic placeholder menu.
- Controls are user-friendly.
- Animations and feedback make gameplay easier to understand.
- Sound/haptic feedback is triggered during real play and respects settings.
- The game has replay motivation, not only a static level/content list.
- A visual/gameplay iteration used real screenshots, recording, live app output, or manual play notes.
- The latest 95% Game Feel Gate score is 95 or higher, or the remaining risk is explicitly accepted before ads/store/release.
- Enough content exists for version 1.
- ASO-friendly display name is approved.
- Package name follows `com.childhood.<game_slug>` before publishing.
- AdMob and analytics are implemented safely.
- Ads do not harm active gameplay.
- Store screenshots/assets are truthful, generated or captured where approved, and based on real gameplay.
- Release checklist is complete.
- Internal or closed testing plan is ready.
