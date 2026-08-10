# Rapid Jump Game Prompt Process

Use this prompt process to plan and build an original rapid jump / vertical arcade jumper game for Flutter.

The goal is not to clone Doodle Jump, Helix Jump, Stack Jump, Geometry Dash, or any other existing game. The goal is to create a small, original, finishable jump game with its own controls, character, obstacle language, progression, visuals, and monetization.

## Purpose

Guide a rapid jump game from rough idea to first playable prototype, then toward platform patterns, missions, polish, monetization, store assets, testing, and release.

This process is designed for a solo Flutter developer. It favors responsive controls, readable hazards, short sessions, strong game feel, and a small MVP before shops, online leaderboards, skins, seasons, or complex economies.

## When to Use

Use this process when:

- You want to create a new vertical jumper, bounce game, platform jump game, or one-touch jump arcade game.
- You want an offline casual game that can be finished and released.
- You want Codex to help with planning, architecture, prototype, review, monetization, and release.
- You want a repeatable process that can become a publishable Flutter game.

Do not use this process to copy another game's name, UI, art, character, platform layouts, obstacle patterns, sound, monetization tricks, or branding.

## Core Rules

- Do not copy existing game names, art, UI, icons, screenshots, characters, platforms, obstacles, music, maps, levels, or branding.
- Keep version 1 offline.
- Build jump physics, movement control, platforms, hazards, score, game over, restart, and best score before skins, shop, missions, or power-ups.
- Prefer one simple endless or level-based mode for MVP.
- Keep controls readable: tap, hold, drag, tilt, or left/right buttons, but avoid mixing too many control styles.
- Make hazards fair and visible before they can punish the player.
- Do not add ads during active gameplay.
- Prefer rewarded ads for optional revive, continue, or bonus reward only after the core loop is stable.
- Use interstitials only at natural game-over or session-break transitions, with frequency caps.
- Keep the first prototype small enough to finish and test.

## Recommended Flow

1. Prompt RJ1: Original game concept and MVP plan.
2. Prompt RJ2: Game design document.
3. Prompt RJ3: Flutter technical architecture.
4. Prompt RJ4: First playable prototype.
5. Prompt RJ5: Prototype fun and quality review.
6. Prompt RJ6: Platforms, hazards, missions, and progression plan.
7. Prompt RJ7: Monetization and analytics plan.
8. Prompt RJ8: Store listing and creative asset plan.
9. Prompt RJ9: Closed testing and release readiness.
10. Prompt RJ10: Post-release improvement plan.

## Production V1 Requirement

Do not publish after only the first playable prototype. For a release-ready version 1, use `prompts/game-production-ready-prompt-pack.md` after the prototype review.

Production v1 should include polished UI, responsive jump feel, fair hazards, enough missions or platform patterns, production-safe AdMob, analytics, truthful store assets, and release QA.

Suggested content target: one polished endless mode plus 30-50 missions, achievements, challenge steps, or equivalent replayable goals.

Run production prompts in this order:

1. `P1` production scope lock.
2. `P2` UI and gameplay polish.
3. `P3` content and mission implementation.
4. `P4` AdMob and analytics implementation.
5. `P5` store assets and listing production.
6. `P6` production release readiness.

## Prompt RJ1: Original Game Concept and MVP Plan

Use this before writing code.

```text
You are helping me plan an original Flutter rapid jump / vertical arcade jumper game.

Do not write code yet.

The game should be original. Do not copy names, art, UI, assets, exact branding, characters, platforms, obstacle patterns, levels, monetization, or progression from Doodle Jump, Helix Jump, Stack Jump, Geometry Dash, or any other existing game.

What I want from you:
1. Define the core game idea in one sentence.
2. Define the target player.
3. Define the core loop.
4. Define what makes this game different.
5. Define the smallest playable MVP.
6. Define the first screen flow.
7. Define controls.
8. Define character, jump, platform, hazard, score, win, and lose rules.
9. Define the first obstacle and platform pattern set.
10. Define 3 possible themes and recommend one.
11. Define what should not be built in version 1.
12. Define a user-friendly monetization direction.
13. Define the first prototype task.

Rules:
- Keep MVP small enough for a solo developer.
- Prefer one game mode for version 1.
- Prefer offline endless or short challenge sessions.
- Do not add ads before the core loop is fun.
- Do not add skins, shop, leaderboard, login, cloud sync, live events, or complex missions unless clearly needed later.

Expected output:
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

## Prompt RJ2: Game Design Document

Use this after the concept is clear.

```text
You are creating a game design document for my original Flutter rapid jump MVP.

Do not write code yet.

Use the approved concept from this task. If no concept exists, create a small original concept first and ask me to approve it before continuing.

What I want from you:
1. Game summary.
2. Core loop.
3. Session length target.
4. Win, lose, and restart conditions.
5. Character movement and jump rules.
6. Camera scrolling rules.
7. Platform rules.
8. Hazard and obstacle rules.
9. Collectible, score, and reward rules.
10. First 10 platform pattern guidelines.
11. Power-up rules, if any.
12. UI screens and HUD.
13. Sound, haptics, and visual feedback.
14. Difficulty progression.
15. Analytics events.
16. Ad placement rules for later.
17. Done criteria for the first playable prototype.

Rules:
- Keep version 1 simple.
- Avoid shop, online leaderboard, login, cloud sync, and complex economy in MVP.
- Make rules precise enough for implementation.
- Keep monetization out of active gameplay.
- Make hazards readable and fair.

Expected output:
- Complete MVP game design document.
- Rule tables where useful.
- First 10 pattern guidelines.
- Prototype done criteria.
- Risks and open questions.
```

## Prompt RJ3: Flutter Technical Architecture

Use this before implementation.

```text
You are designing the Flutter technical architecture for my original rapid jump game.

Use Flame if it is the best fit for game loop, physics-like movement, collisions, camera scrolling, particles, and platform spawning. If plain Flutter is better for this scope, explain why.

Do not write code yet.

What I want from you:
1. Recommend Flame or plain Flutter.
2. Define folder structure.
3. Define game loop architecture.
4. Define entity model: player, platform, hazard, pickup, camera, level/session state.
5. Define coordinate system and screen scaling.
6. Define input handling.
7. Define jump and gravity rules.
8. Define platform collision rules.
9. Define obstacle and spawn system.
10. Define score and game state.
11. Define local save data.
12. Define analytics event names.
13. Define future AdMob integration points.
14. Define test strategy.
15. Define the first implementation slice.

Rules:
- Follow the existing project architecture if this is inside an existing repo.
- Keep the first implementation slice small.
- Do not add Firebase, AdMob, purchases, leaderboard, skins, or shop yet unless explicitly approved.
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

## Prompt RJ4: First Playable Prototype

Use this to implement the first playable version.

```text
You are implementing the first playable prototype of my original Flutter rapid jump game.

Use the approved game design and technical architecture from this task. If no approved scope exists, create a small prototype scope and ask me to approve it before editing.

Scope:
- Main menu.
- One playable game mode.
- Player character with jump/movement.
- Platforms.
- Camera or vertical progression.
- One simple hazard or fail condition.
- Score or height/distance.
- Game over.
- Restart.
- Best score saved locally.
- Basic HUD.
- No ads.
- No shop.
- No skins.
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
- Do not copy assets, characters, platform layouts, obstacle patterns, UI, or sounds from existing games.
- If using placeholder visuals, label them as placeholders.

Expected output:
- Files changed.
- Prototype behavior.
- Manual test steps.
- Checks run or skipped.
- Remaining risks.
- Next recommended improvement.
```

## Prompt RJ5: Prototype Fun and Quality Review

Use this after the first playable prototype exists.

```text
You are reviewing the first playable prototype of my original rapid jump game.

Inspect the repository and prototype implementation. Do not edit files.

What I want from you:
1. Review whether controls feel likely to be responsive and fun.
2. Review whether jump arc, gravity, and landing feel readable.
3. Review whether platforms and hazards are fair.
4. Review whether score, restart, and best score are understandable.
5. Review whether difficulty is too easy, too hard, or okay.
6. Review performance risks.
7. Review code quality risks.
8. Identify the top 3 fixes before adding features.
9. Identify what should not be added yet.
10. Create a small improvement scope.

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

## Prompt RJ6: Platforms, Hazards, Missions, and Progression Plan

Use this after the core prototype is playable.

```text
You are planning platforms, hazards, missions, and progression for my original rapid jump game.

Do not write code yet.

Use the current prototype and game design. Keep changes small enough for one update.

What I want from you:
1. Define first 30-50 mission or challenge steps.
2. Define platform types.
3. Define hazard types.
4. Define 3-5 pickup or power-up ideas.
5. Score each pickup or power-up by fun, complexity, balance risk, and visual clarity.
6. Recommend only 1-2 additions for the next update.
7. Define difficulty progression.
8. Define reward loop.
9. Define implementation order.

Rules:
- Prefer readable platform patterns over random unfair difficulty.
- Do not add too many hazards or power-ups at once.
- Keep difficulty fair and learnable.
- Do not add monetization until the gameplay loop is stable.
- Avoid complex shop or upgrade economy in early versions.

Expected output:
- Mission/challenge plan.
- Platform and hazard table.
- Pickup or power-up table.
- Recommended next features.
- Reward loop.
- Implementation order.
```

## Prompt RJ7: Monetization and Analytics Plan

Use this only after the game loop is fun enough.

```text
You are planning user-friendly monetization and analytics for my original rapid jump game.

Do not write code yet.

What I want from you:
1. Decide whether the game is ready for ads.
2. Define rewarded ad opportunities.
3. Define whether interstitial ads are appropriate.
4. Define frequency caps.
5. Define where ads must never appear.
6. Define analytics events needed to measure session length, difficulty, retention, and ad impact.
7. Define policy risks.
8. Create a safe implementation scope.

Rules:
- User experience comes before revenue.
- Policy compliance comes before revenue.
- Do not show ads during active gameplay.
- Do not encourage ad clicks.
- Do not reward ad clicks.
- Prefer rewarded ads for optional revive, continue, bonus coins, or temporary booster trials.
- Use interstitials only at natural game-over or session-break transitions.
- Add frequency caps before scaling ads.

Expected output:
- Monetization readiness decision.
- Rewarded ad plan.
- Interstitial plan, if appropriate.
- Frequency cap rules.
- Analytics event list.
- Policy risk review.
- Implementation scope.
```

## Prompt RJ8: Store Listing and Creative Asset Plan

Use this when the game has enough real visuals for store assets.

```text
You are planning Google Play store listing assets for my original rapid jump game.

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
- Do not copy names, visuals, characters, platforms, obstacle patterns, maps, or branding from other games.
- Do not show unavailable skins, modes, rewards, maps, or power-ups.
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

## Prompt RJ9: Closed Testing and Release Readiness

Use this before Play Store testing or release.

```text
You are checking closed testing and release readiness for my original Flutter rapid jump game.

Use the repository and release checklist. Do not publish anything.

What I want from you:
1. Review build and version readiness.
2. Review gameplay readiness.
3. Review crash and performance risks.
4. Review ads and analytics readiness.
5. Review permissions and privacy risk.
6. Review Data safety impact.
7. Review store listing readiness.
8. Create a manual QA checklist.
9. Recommend internal test, closed test, delay, or release.

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

## Prompt RJ10: Post-Release Improvement Plan

Use this after testing or release.

```text
You are helping me improve my original rapid jump game after testing or release.

Use available tester feedback, reviews, analytics, Crashlytics, Android vitals, and AdMob data. If external data is missing, mark it as unknown.

What I want from you:
1. Summarize release health.
2. Identify gameplay issues.
3. Identify crash or performance issues.
4. Identify ad experience issues.
5. Identify difficulty, session length, or retention issues.
6. Recommend the next small update.
7. Identify what should not be built yet.
8. Create a learning note.

Rules:
- Fix crashes and serious gameplay frustration before adding new features.
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
Run Prompt RJ1 from `prompts/rapid-jump-game-prompt-process.md`.
```

Then:

```text
Run Prompt RJ2 from `prompts/rapid-jump-game-prompt-process.md` using the approved concept from this task.
```

Then:

```text
Run Prompt RJ3 from `prompts/rapid-jump-game-prompt-process.md` using the approved game design from this task.
```

Only after approving architecture:

```text
Run Prompt RJ4 from `prompts/rapid-jump-game-prompt-process.md` using the approved prototype scope from this task.
```

After the prototype is playable and reviewed:

```text
Run Prompt P1 from `prompts/game-production-ready-prompt-pack.md` for the current repository.
```

## Done Criteria

The game process is working when:

- The game has an original concept.
- The first prototype is playable.
- Jump movement, platforms, hazards, score, game over, restart, and best score work.
- Controls feel responsive.
- Hazards feel readable and fair.
- Missions or challenge steps create replay value.
- Visual and sound feedback feel satisfying.
- Ads never interrupt active gameplay.
- Store assets show real gameplay.
- Testing produces a learning note before the next update.
