# Football Game Prompt Process

Use this prompt process to plan and build an original football / soccer game for Flutter.

The goal is not to clone FIFA, EA SPORTS FC, eFootball, Dream League Soccer, Score Hero, Soccer Stars, or any other existing football game. The goal is to create a small, original, finishable football game with its own controls, visual style, match rules, progression, and monetization.

## Purpose

Guide a football game from rough idea to first playable prototype, then toward challenges, modes, polish, monetization, store assets, testing, and release.

This process is designed for a solo Flutter developer. It favors one polished core mode before trying to build a full 11v11 simulation, real teams, online multiplayer, leagues, transfer systems, or complex physics.

## When to Use

Use this process when:

- You want to create a new football / soccer game.
- You want an offline casual sports game that can be finished and released.
- You want Codex to help with planning, architecture, prototype, review, monetization, and release.
- You want the game to become a polished Play Store product, not only a prototype.

Good version 1 directions include:

- Penalty shootout.
- Free kick challenge.
- Goalkeeper save challenge.
- Dribble runner.
- One-touch passing and shooting puzzle.
- Simple 1v1 or 2v2 arcade match.

Do not use this process to copy another game's name, UI, kits, badges, clubs, leagues, players, stadiums, commentary, animations, screenshots, icons, sounds, monetization tricks, or branding.

## Core Rules

- Keep version 1 offline.
- Choose one core mode before adding multiple modes.
- Build aiming, kicking, ball movement, goal detection, score, miss/save logic, restart, and result screen before shops, leagues, teams, online play, or events.
- Do not use real club names, player names, league names, official badges, kits, stadiums, or tournament branding unless you have rights.
- Keep controls readable and mobile-friendly.
- Make failure fair: the player should understand why a shot missed or was saved.
- Do not show ads during active aiming, kicking, ball movement, or save attempts.
- Prefer rewarded ads only for optional continues, extra attempts, cosmetic unlocks, or bonus challenges.
- Use interstitials only at natural challenge-end, match-end, or session-break transitions, with frequency caps.
- Keep the first prototype small enough to finish and test.

## Recommended Flow

1. Prompt FB1: Original game concept and MVP plan.
2. Prompt FB2: Game design document.
3. Prompt FB3: Flutter technical architecture.
4. Prompt FB4: First playable prototype.
5. Prompt FB5: Prototype fun and quality review.
6. Prompt FB6: Challenges, modes, and progression plan.
7. Prompt FB7: Monetization and analytics plan.
8. Prompt FB8: Store listing and creative asset plan.
9. Prompt FB9: Closed testing and release readiness.
10. Prompt FB10: Post-release improvement plan.

## Production V1 Requirement

Do not publish after only the first playable prototype. For a release-ready version 1, use `prompts/game-production-ready-prompt-pack.md` after the prototype review.

Production v1 should include polished UI, satisfying ball feel, fair challenge rules, enough levels or missions, production-safe AdMob, analytics, truthful store assets, and release QA.

Suggested content target: one polished core mode plus 30-50 challenges, levels, missions, or shot scenarios. If the game uses endless play, include best score, difficulty ramp, and 20-30 achievement-style goals.

Run production prompts in this order:

1. `P1` production scope lock.
2. `P2` UI and gameplay polish.
3. `P3` challenge, mode, and content implementation.
4. `P4` AdMob and analytics implementation.
5. `P5` store assets and listing production.
6. `P6` production release readiness.

## Prompt FB1: Original Game Concept and MVP Plan

Use this before writing code.

```text
You are helping me plan an original Flutter football / soccer game.

Do not write code yet.

The game should be original. Do not copy names, art, UI, assets, exact branding, kits, badges, clubs, leagues, players, stadiums, shot patterns, levels, monetization, or progression from FIFA, EA SPORTS FC, eFootball, Dream League Soccer, Score Hero, Soccer Stars, or any other football game.

What I want from you:
1. Recommend one practical football game direction for version 1.
2. Define the core game idea in one sentence.
3. Define the target player.
4. Define the core loop.
5. Define what makes this game different.
6. Define the smallest playable MVP.
7. Define the first screen flow.
8. Define controls.
9. Define player, ball, goal, keeper, obstacle, score, win, lose, and restart rules.
10. Define the first challenge or scenario set.
11. Define 3 possible visual themes and recommend one.
12. Define what should not be built in version 1.
13. Define a user-friendly monetization direction.
14. Define the first prototype task.

Rules:
- Keep MVP small enough for a solo developer.
- Prefer one mode for version 1.
- Prefer penalty, free kick, save challenge, dribble runner, or shot puzzle before full match simulation.
- Do not add ads before the core loop is fun.
- Do not add official teams, real players, real leagues, online multiplayer, betting-like mechanics, login, cloud sync, complex shop, or live events.

Expected output:
- Recommended football game direction.
- One-sentence concept.
- Target player.
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

## Prompt FB2: Game Design Document

Use this after the concept is clear.

```text
You are creating a game design document for my original Flutter football MVP.

Do not write code yet.

Use the approved concept from this task. If no concept exists, create a small original concept first and ask me to approve it before continuing.

What I want from you:
1. Game summary.
2. Core loop.
3. Session length target.
4. MVP game mode.
5. Win, lose, restart, and scoring conditions.
6. Input and control rules.
7. Ball movement rules.
8. Shot, pass, dribble, save, or collision rules based on the chosen mode.
9. Goalkeeper or obstacle behavior, if included.
10. First 10 challenge or scenario guidelines.
11. Difficulty progression.
12. UI screens and HUD.
13. Sound, haptics, and visual feedback.
14. Analytics events.
15. Ad placement rules for later.
16. Done criteria for the first playable prototype.

Rules:
- Keep version 1 simple.
- Avoid full 11v11 simulation, real teams, real leagues, rosters, transfers, online play, and complex economy in MVP.
- Make rules precise enough for implementation.
- Keep monetization out of active gameplay.
- Make every miss, save, goal, and retry understandable.

Expected output:
- Complete MVP game design document.
- Rule tables where useful.
- First 10 challenge guidelines.
- Prototype done criteria.
- Risks and open questions.
```

## Prompt FB3: Flutter Technical Architecture

Use this before implementation.

```text
You are designing the Flutter technical architecture for my original football game.

Use Flame if it is the best fit for game loop, ball movement, collision, camera, particles, and animation. If plain Flutter is better for this scope, explain why.

Do not write code yet.

What I want from you:
1. Recommend Flame or plain Flutter.
2. Define folder structure.
3. Define game loop architecture.
4. Define entity model: player, ball, goal, keeper, obstacle, field, challenge, result.
5. Define coordinate system and screen scaling.
6. Define input handling.
7. Define ball movement and physics approximation.
8. Define collision and goal detection.
9. Define challenge/scenario system.
10. Define score and game state.
11. Define local save data.
12. Define analytics event names.
13. Define future AdMob integration points.
14. Define test strategy.
15. Define the first implementation slice.

Rules:
- Follow the existing project architecture if this is inside an existing repo.
- Keep the first implementation slice small.
- Do not add Firebase, AdMob, purchases, leaderboard, real teams, real players, or online play yet unless explicitly approved.
- Avoid overengineering.

Expected output:
- Architecture decision.
- Folder structure.
- Main classes or components.
- Coordinate, movement, and collision rules.
- Data flow.
- First implementation slice.
- Test plan.
```

## Prompt FB4: First Playable Prototype

Use this to implement the first playable version.

```text
You are implementing the first playable prototype of my original Flutter football game.

Use the approved game design and technical architecture from this task. If no approved scope exists, create a small prototype scope and ask me to approve it before editing.

Scope:
- Main menu.
- One playable mode.
- Player input.
- Ball movement.
- Goal or target.
- Keeper or obstacle only if approved.
- Score or challenge progress.
- Goal/miss/save result.
- Restart.
- Basic HUD.
- No ads.
- No real teams.
- No online play.
- No shop.
- No leaderboard.

What I want from you:
1. Inspect the repository first.
2. Implement only the first playable prototype.
3. Keep code small and reviewable.
4. Follow existing project patterns.
5. Add minimal tests where useful.
6. Use lightweight verification unless a build is essential.
7. Explain how to run and manually test the prototype.

Rules:
- Do not add monetization yet.
- Do not add unrelated features.
- Do not introduce large dependencies unless approved.
- Do not copy UI, sounds, kits, characters, stadiums, levels, shot patterns, or assets from existing games.
- If using placeholder visuals, label them as placeholders.

Expected output:
- Files changed.
- Prototype behavior.
- Manual test steps.
- Checks run or skipped.
- Remaining risks.
- Next recommended improvement.
```

## Prompt FB5: Prototype Fun and Quality Review

Use this after the first playable prototype exists.

```text
You are reviewing the first playable prototype of my original football game.

Inspect the repository and prototype implementation. Do not edit files.

What I want from you:
1. Review whether controls feel likely to be responsive and fun.
2. Review whether ball movement feels understandable.
3. Review whether goals, misses, saves, and retries are clear.
4. Review whether challenge difficulty is too easy, too hard, or okay.
5. Review whether the game feels fair on small screens.
6. Review UI polish and readability.
7. Review performance risks.
8. Review code quality risks.
9. Identify the top 3 fixes before adding features.
10. Identify what should not be added yet.
11. Create a small improvement scope.

Rules:
- Do not change code.
- Do not add ads yet.
- Prioritize control feel, fairness, readability, and feedback before monetization.
- Keep recommendations practical.

Expected output:
- Fun review.
- Quality review.
- Top 3 fixes.
- Not-now list.
- Small improvement scope.
```

## Prompt FB6: Challenges, Modes, and Progression Plan

Use this after the core prototype is playable.

```text
You are planning challenges, modes, progression, and replay value for my original football game.

Do not write code yet.

Use the current prototype and game design. Keep changes small enough for one update.

What I want from you:
1. Define production v1 game modes.
2. Define 30-50 challenges, levels, missions, or shot scenarios.
3. Define difficulty progression.
4. Define optional obstacles, keeper behavior, field layouts, or targets.
5. Define local best scores or progress tracking.
6. Define optional cosmetic ideas.
7. Score each idea by user value, effort, risk, monetization fit, and policy risk.
8. Recommend only the best next additions.
9. Define implementation order.

Rules:
- Prefer replayable offline modes over complex leagues.
- Do not add official teams, rosters, live events, login, cloud sync, or online play in early versions.
- Do not create features only to force more ad impressions.
- Keep challenges fair and readable.

Expected output:
- Mode plan.
- Challenge/scenario list.
- Optional feature score table.
- Recommended next additions.
- Implementation order.
```

## Prompt FB7: Monetization and Analytics Plan

Use this only after the game loop is fun enough.

```text
You are planning user-friendly monetization and analytics for my original football game.

Do not write code yet.

What I want from you:
1. Decide whether the game is ready for ads.
2. Define whether banner ads are appropriate.
3. Define whether interstitial ads are appropriate.
4. Define rewarded ad opportunities, if any.
5. Define frequency caps.
6. Define where ads must never appear.
7. Define analytics events needed to measure challenge starts, challenge finishes, goals, misses, saves, retries, session length, retention, and ad impact.
8. Define Play policy, official-brand, and invalid traffic risks.
9. Create a safe implementation scope.

Rules:
- User experience comes before revenue.
- Policy compliance comes before revenue.
- Do not show ads during active aiming, kicking, ball movement, or save attempts.
- Do not encourage ad clicks.
- Do not reward ad clicks.
- Use interstitials only after challenge end, match end, or clear session breaks.
- Add frequency caps before scaling ads.
- Do not imply affiliation with official football clubs, leagues, players, or tournaments.

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

## Prompt FB8: Store Listing and Creative Asset Plan

Use this when the game has enough real visuals for store assets.

```text
You are planning Google Play store listing assets for my original football game.

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
- Do not copy names, visuals, kits, badges, clubs, leagues, players, stadiums, screenshots, UI, or branding from other games or real football brands.
- Do not imply official club, league, tournament, or player affiliation.
- Do not show unavailable modes, teams, tournaments, rewards, stadiums, or features.
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

## Prompt FB9: Closed Testing and Release Readiness

Use this before Play Store testing or release.

```text
You are checking closed testing and release readiness for my original Flutter football game.

Use the repository and release checklist. Do not publish anything.

What I want from you:
1. Review build and version readiness.
2. Review gameplay readiness.
3. Review challenge/content readiness.
4. Review crash and performance risks.
5. Review ads and analytics readiness.
6. Review official-brand, permissions, and privacy risk.
7. Review Data safety impact.
8. Review store listing readiness.
9. Create a manual QA checklist.
10. Recommend internal test, closed test, delay, or release.

Rules:
- Do not claim release readiness if checks were not run.
- Keep unknowns clear.
- Prefer internal or closed testing if risk is unclear.
- Do not run heavy build/install/emulator unless explicitly approved.
- Block release if store assets or in-game content imply unauthorized official affiliation.

Expected output:
- Release readiness summary.
- Blockers.
- Manual QA checklist.
- Play Console checklist.
- Recommendation.
```

## Prompt FB10: Post-Release Improvement Plan

Use this after testing or release.

```text
You are helping me improve my original football game after testing or release.

Use available tester feedback, reviews, analytics, Crashlytics, Android vitals, and AdMob data. If external data is missing, mark it as unknown.

What I want from you:
1. Summarize release health.
2. Identify gameplay or control issues.
3. Identify challenge difficulty issues.
4. Identify crash or performance issues.
5. Identify ad experience issues.
6. Identify mode popularity, session length, or retention issues.
7. Recommend the next small update.
8. Identify what should not be built yet.
9. Create a learning note.

Rules:
- Fix crashes, control problems, unfair difficulty, and serious gameplay frustration before adding new features.
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
Run Prompt FB1 from `prompts/football-game-prompt-process.md`.
```

Then:

```text
Run Prompt FB2 from `prompts/football-game-prompt-process.md` using the approved concept from this task.
```

Then:

```text
Run Prompt FB3 from `prompts/football-game-prompt-process.md` using the approved game design from this task.
```

Only after approving architecture:

```text
Run Prompt FB4 from `prompts/football-game-prompt-process.md` using the approved prototype scope from this task.
```

After the prototype is playable and reviewed:

```text
Run Prompt P1 from `prompts/game-production-ready-prompt-pack.md` for the current repository.
```

## Done Criteria

The game process is working when:

- The game has an original concept.
- The first prototype is playable.
- Controls, ball movement, score, result, restart, and win/loss logic work.
- Goals, misses, saves, and retries are readable.
- UI is clear and polished enough for casual players.
- One core mode is strong enough for version 1.
- 30-50 challenges, missions, or equivalent replayable goals are planned or implemented for production v1.
- Ads never interrupt active gameplay.
- Store assets show real gameplay.
- Testing produces a learning note before the next update.
