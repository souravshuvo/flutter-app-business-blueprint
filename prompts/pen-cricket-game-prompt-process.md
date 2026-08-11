# Pen Cricket Game Prompt Process

Use this prompt process to plan and build an original Pen Cricket game for Flutter.

The goal is to recreate the nostalgic paper-and-pen cricket feeling in a digital format, without copying another app's name, UI, art, sound, monetization, or store assets. The game should feel simple, quick, polished, and easy to understand.

## Purpose

Guide a Pen Cricket game from idea to first playable prototype, then toward match modes, spinner polish, score history, monetization, store assets, testing, and release.

This process is designed for a solo Flutter developer. It favors a small, finished game with clear cricket rules, reliable scoring, satisfying spinner feedback, and a production-ready version 1 before adding complex leagues, online play, cloud sync, or heavy progression systems.

## When to Use

Use this process when:

- You want to create a Pen Cricket, paper cricket, spinner cricket, or casual cricket score game.
- You want an offline cricket game that can be finished and released.
- You want Codex to help with planning, architecture, prototype, review, monetization, and release.
- You want the game to become a polished Play Store product, not only a prototype.

Do not use this process to copy another game's name, UI, scorecard layout, spinner design, screenshots, icons, sounds, monetization tricks, or branding.

## Core Rules

- Keep version 1 offline.
- Build spinner, outcomes, score, wickets, balls, overs, innings end, target chase, restart, and match result before tournaments, online play, skins, shop, or leaderboards.
- Spinner behavior must feel fair, readable, and satisfying.
- Wide and no-ball must add extras without consuming legal deliveries.
- Match state must never become impossible or inconsistent.
- Do not show ads while the spinner is active or during a delivery result animation.
- Prefer interstitial ads only after match end or clear session breaks, with frequency caps.
- Prefer rewarded ads only for optional cosmetics, bonus challenge unlocks, or harmless extra content.
- Keep the first prototype small enough to finish and test.

## Recommended Flow

1. Prompt PC1: Original game concept and MVP plan.
2. Prompt PC2: Game design document.
3. Prompt PC3: Flutter technical architecture.
4. Prompt PC4: First playable prototype.
5. Prompt PC5: Prototype fun and quality review.
6. Prompt PC6: Match modes, challenges, and progression plan.
7. Prompt PC7: Monetization and analytics plan.
8. Prompt PC8: Store listing and creative asset plan.
9. Prompt PC9: Closed testing and release readiness.
10. Prompt PC10: Post-release improvement plan.

## Production V1 Requirement

Do not publish after only the first playable prototype. For a release-ready version 1, use `prompts/game-production-ready-prompt-pack.md` after the prototype review.

Production v1 should include polished UI, smooth spinner feedback, correct cricket scoring, at least practice and target-chase modes, production-safe AdMob, analytics, truthful store assets, and release QA.

Suggested content target: practice mode, target chase mode, 3-5 over presets, local best scores or match history, and 20-30 challenge targets or achievements.

Run production prompts in this order:

1. `P1` production scope lock.
2. `P2` UI and gameplay polish.
3. `P3` modes, challenges, and content implementation.
4. `P4` AdMob and analytics implementation.
5. `P5` store assets and listing production.
6. `P6` production release readiness.

## Prompt PC1: Original Game Concept and MVP Plan

Use this before writing code.

```text
You are helping me plan an original Flutter Pen Cricket game.

Do not write code yet.

The game should be original. Do not copy names, art, UI, assets, exact branding, spinner visuals, sounds, scorecard layouts, match modes, monetization, or progression from any existing Pen Cricket or cricket game.

What I want from you:
1. Define the core game idea in one sentence.
2. Define the target player.
3. Define the nostalgic hook.
4. Define the core loop.
5. Define what makes this game different.
6. Define the smallest playable MVP.
7. Define the first screen flow.
8. Define spinner controls.
9. Define run, out, wide, no-ball, delivery, over, wicket, innings, and target-chase rules.
10. Define 3 possible visual themes and recommend one.
11. Define what should not be built in version 1.
12. Define a user-friendly monetization direction.
13. Define the first prototype task.

Rules:
- Keep MVP small enough for a solo developer.
- Prefer offline practice and target chase before leagues or tournaments.
- Do not add ads before the core loop is fun and scoring is correct.
- Do not add login, cloud sync, online multiplayer, betting-like mechanics, complex shop, or live events.
- Keep the game family-friendly and policy-safe.

Expected output:
- One-sentence concept.
- Target player.
- Nostalgia hook.
- Core loop.
- Differentiation.
- MVP scope.
- First screen flow.
- Game rules.
- Theme recommendation.
- Not-now list.
- Monetization direction.
- First prototype task.
```

## Prompt PC2: Game Design Document

Use this after the concept is clear.

```text
You are creating a game design document for my original Flutter Pen Cricket MVP.

Do not write code yet.

Use the approved concept from this task. If no concept exists, create a small original concept first and ask me to approve it before continuing.

What I want from you:
1. Game summary.
2. Core loop.
3. Session length target.
4. Game modes for MVP.
5. Spinner start, stop, speed, randomness, and result rules.
6. Outcome table for 0, 1, 2, 3, 4, 6, Out, Wide, and No Ball.
7. Legal delivery and extras rules.
8. Over and wicket rules.
9. Innings end rules.
10. Target chase win and loss rules.
11. Scorecard and match result display.
12. UI screens and HUD.
13. Sound, haptics, and visual feedback.
14. Difficulty or challenge progression.
15. Analytics events.
16. Ad placement rules for later.
17. Done criteria for the first playable prototype.

Rules:
- Make cricket rules precise enough for implementation.
- Keep version 1 simple.
- Avoid tournaments, teams, player rosters, online play, cloud sync, and complex rewards in MVP.
- Keep monetization out of active gameplay.
- Make every result understandable to a casual user.

Expected output:
- Complete MVP game design document.
- Rules table.
- Screen flow.
- Prototype done criteria.
- Risks and open questions.
```

## Prompt PC3: Flutter Technical Architecture

Use this before implementation.

```text
You are designing the Flutter technical architecture for my original Pen Cricket game.

Use plain Flutter unless Flame or another game library is clearly justified. This game should usually work well with Flutter widgets, animations, state management, and pure Dart match logic.

Do not write code yet.

What I want from you:
1. Recommend plain Flutter or a game library.
2. Define folder structure.
3. Define domain model: match, innings, delivery, outcome, score, over, wicket, mode, result.
4. Define spinner state model.
5. Define random outcome generation or spinner result calculation.
6. Define match controller flow.
7. Define local save data for settings, best scores, and match history if included.
8. Define UI screens.
9. Define animation approach.
10. Define analytics event names.
11. Define future AdMob integration points.
12. Define test strategy.
13. Define the first implementation slice.

Rules:
- Follow the existing project architecture if this is inside an existing repo.
- Keep match rules in pure Dart where practical.
- Keep UI separate from match rules.
- Do not add Firebase, AdMob, purchases, leaderboard, online play, or complex progression yet unless explicitly approved.
- Avoid overengineering.

Expected output:
- Architecture decision.
- Folder structure.
- Main classes or components.
- Match state flow.
- Spinner state flow.
- Data flow.
- First implementation slice.
- Test plan.
```

## Prompt PC4: First Playable Prototype

Use this to implement the first playable version.

```text
You are implementing the first playable prototype of my original Flutter Pen Cricket game.

Use the approved game design and technical architecture from this task. If no approved scope exists, create a small prototype scope and ask me to approve it before editing.

Scope:
- Main menu.
- Practice innings mode.
- Target chase mode if small enough.
- Spinner screen with tap-to-spin and tap-to-stop.
- Outcome result display.
- Score, wickets, balls, and overs.
- Wide and no-ball extras.
- Innings end.
- Target chase result.
- Restart.
- Basic settings if simple.
- No ads.
- No online play.
- No shop.
- No leaderboard.

What I want from you:
1. Inspect the repository first.
2. Implement only the first playable prototype.
3. Keep code small and reviewable.
4. Follow existing project patterns.
5. Add unit tests for cricket scoring rules where practical.
6. Use lightweight verification unless a build is essential.
7. Explain how to run and manually test the prototype.

Rules:
- Do not add monetization yet.
- Do not add unrelated features.
- Do not introduce large dependencies unless approved.
- Do not copy UI, sounds, scorecards, spinner designs, icons, or assets from existing games.
- If using placeholder visuals, label them as placeholders.

Expected output:
- Files changed.
- Prototype behavior.
- Scoring rules covered.
- Manual test steps.
- Checks run or skipped.
- Remaining risks.
- Next recommended improvement.
```

## Prompt PC5: Prototype Fun and Quality Review

Use this after the first playable prototype exists.

```text
You are reviewing the first playable prototype of my original Pen Cricket game.

Inspect the repository and prototype implementation. Do not edit files.

What I want from you:
1. Review whether spinner interaction feels likely to be satisfying.
2. Review whether scoring rules are correct.
3. Review whether wides and no-balls are handled correctly.
4. Review whether innings and target-chase endings are correct.
5. Review whether screen flow is clear.
6. Review UI polish and readability.
7. Review performance risks.
8. Review code quality risks.
9. Identify the top 3 fixes before adding features.
10. Identify what should not be added yet.
11. Create a small improvement scope.

Rules:
- Do not change code.
- Do not add ads yet.
- Prioritize rule correctness, spinner feel, readability, and feedback before monetization.
- Keep recommendations practical.

Expected output:
- Fun review.
- Rule correctness review.
- Quality review.
- Top 3 fixes.
- Not-now list.
- Small improvement scope.
```

## Prompt PC6: Match Modes, Challenges, and Progression Plan

Use this after the core prototype is playable.

```text
You are planning match modes, challenge targets, score history, and progression for my original Pen Cricket game.

Do not write code yet.

Use the current prototype and game design. Keep changes small enough for one update.

What I want from you:
1. Define production v1 game modes.
2. Define 3-5 over presets or match presets.
3. Define 20-30 challenge targets or achievements.
4. Define local best scores or match history.
5. Define optional cosmetic or theme ideas.
6. Score each idea by user value, effort, risk, monetization fit, and policy risk.
7. Recommend only the best next additions.
8. Define implementation order.

Rules:
- Prefer replayable offline modes over complex tournaments.
- Do not add teams, rosters, live events, login, cloud sync, or online play in early versions.
- Do not create features only to force more ad impressions.
- Keep achievements family-friendly and simple.

Expected output:
- Mode plan.
- Challenge/achievement list.
- Optional feature score table.
- Recommended next additions.
- Implementation order.
```

## Prompt PC7: Monetization and Analytics Plan

Use this only after the game loop is fun enough and scoring is stable.

```text
You are planning user-friendly monetization and analytics for my original Pen Cricket game.

Do not write code yet.

What I want from you:
1. Decide whether the game is ready for ads.
2. Define whether banner ads are appropriate.
3. Define whether interstitial ads are appropriate.
4. Define rewarded ad opportunities, if any.
5. Define frequency caps.
6. Define where ads must never appear.
7. Define analytics events needed to measure match starts, match finishes, spinner use, session length, mode popularity, retention, and ad impact.
8. Define Play policy and invalid traffic risks.
9. Create a safe implementation scope.

Rules:
- User experience comes before revenue.
- Policy compliance comes before revenue.
- Do not show ads while spinner is active.
- Do not show ads during delivery result animation.
- Do not encourage ad clicks.
- Do not reward ad clicks.
- Use interstitials only after match end or clear session breaks.
- Add frequency caps before scaling ads.

Expected output:
- Monetization readiness decision.
- Banner plan, if appropriate.
- Interstitial plan, if appropriate.
- Rewarded ad plan, if appropriate.
- Frequency cap rules.
- Analytics event list.
- Policy risk review.
- Implementation scope.
```

## Prompt PC8: Store Listing and Creative Asset Plan

Use this when the game has enough real visuals for store assets.

```text
You are planning Google Play store listing assets for my original Pen Cricket game.

Use real game screens and actual gameplay. Do not fake gameplay.

What I want from you:
1. Store title ideas.
2. Short description ideas.
3. Full description outline.
4. Screenshot storyboard.
5. Feature graphic concept.
6. App icon concept.
7. Preview video script.
8. Policy and misleading-claim review.
9. Asset production checklist.

Rules:
- Do not copy names, visuals, scorecards, spinner designs, cricket branding, team names, logos, or assets from other games or real cricket brands.
- Do not imply official cricket league, team, or player affiliation.
- Do not show unavailable modes, rewards, tournaments, teams, or features.
- Do not use fake rankings, awards, downloads, reviews, or earnings.
- Keep screenshots based on actual gameplay.

Expected output:
- Store listing copy ideas.
- Screenshot plan.
- Feature graphic brief.
- Icon brief.
- Preview video script.
- Asset checklist.
```

## Prompt PC9: Closed Testing and Release Readiness

Use this before Play Store testing or release.

```text
You are checking closed testing and release readiness for my original Flutter Pen Cricket game.

Use the repository and release checklist. Do not publish anything.

What I want from you:
1. Review build and version readiness.
2. Review cricket rule readiness.
3. Review gameplay and spinner readiness.
4. Review crash and performance risks.
5. Review ads and analytics readiness.
6. Review permissions and privacy risk.
7. Review Data safety impact.
8. Review store listing readiness.
9. Create a manual QA checklist.
10. Recommend internal test, closed test, delay, or release.

Rules:
- Do not claim release readiness if checks were not run.
- Keep unknowns clear.
- Prefer internal or closed testing if risk is unclear.
- Do not run heavy build/install/emulator unless explicitly approved.

Expected output:
- Release readiness summary.
- Blockers.
- Manual QA checklist.
- Play Console checklist.
- Recommendation.
```

## Prompt PC10: Post-Release Improvement Plan

Use this after testing or release.

```text
You are helping me improve my original Pen Cricket game after testing or release.

Use available tester feedback, reviews, analytics, Crashlytics, Android vitals, and AdMob data. If external data is missing, mark it as unknown.

What I want from you:
1. Summarize release health.
2. Identify scoring or rule issues.
3. Identify gameplay or spinner feel issues.
4. Identify crash or performance issues.
5. Identify ad experience issues.
6. Identify mode popularity, session length, or retention issues.
7. Recommend the next small update.
8. Identify what should not be built yet.
9. Create a learning note.

Rules:
- Fix rule bugs, crashes, and serious gameplay frustration before adding new features.
- Do not overreact to tiny samples.
- Keep updates small.
- Preserve user trust.

Expected output:
- Release health summary.
- Top issues.
- Next update recommendation.
- Not-now list.
- Learning note.
```

## Quick Copy-Paste Sequence

Start with:

```text
Run Prompt PC1 from `prompts/pen-cricket-game-prompt-process.md`.
```

Then:

```text
Run Prompt PC2 from `prompts/pen-cricket-game-prompt-process.md` using the approved concept from this task.
```

Then:

```text
Run Prompt PC3 from `prompts/pen-cricket-game-prompt-process.md` using the approved game design from this task.
```

Only after approving architecture:

```text
Run Prompt PC4 from `prompts/pen-cricket-game-prompt-process.md` using the approved prototype scope from this task.
```

After the prototype is playable and reviewed:

```text
Run Prompt P1 from `prompts/game-production-ready-prompt-pack.md` for the current repository.
```

## Done Criteria

The game process is working when:

- The game has an original concept.
- The first prototype is playable.
- Spinner start/stop works.
- Runs, outs, wides, no-balls, legal deliveries, overs, wickets, innings end, and target chase work correctly.
- UI is clear and polished enough for casual players.
- Practice and target chase modes are available.
- Local best scores or match history add replay value.
- Ads never interrupt active spinner gameplay.
- Store assets show real gameplay.
- Testing produces a learning note before the next update.
