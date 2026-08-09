# Match Puzzle Game Prompt Process

Use this prompt process to plan and build an original match puzzle game for Flutter.

The goal is not to clone Candy Crush, Royal Match, Toon Blast, Gardenscapes, Homescapes, Tile Master, or any other existing game. The goal is to create a small, original, finishable match puzzle game with its own theme, board rules, level goals, visuals, progression, and monetization.

## Purpose

Guide a match puzzle game from rough idea to first playable prototype, then toward levels, blockers, boosters, monetization, store assets, testing, and release.

This process is designed for a solo Flutter developer. It favors a clean core loop, correct match logic, satisfying cascades, readable goals, and small level progression before complex maps, story systems, live events, shops, login, or cloud systems.

## When to Use

Use this process when:

- You want to create a new match-3, tap-to-match, tile match, pair match, or grid-based puzzle game.
- You want an offline casual puzzle game that can be finished and released.
- You want Codex to help with planning, architecture, prototype, review, monetization, and release.
- You want to reuse a disciplined process for casual puzzle games.

Do not use this process to copy another game's name, UI, art, board layouts, levels, boosters, characters, music, monetization tricks, or branding.

## Core Rules

- Do not copy existing game names, art, UI, icons, screenshots, board layouts, levels, boosters, characters, music, or branding.
- Keep version 1 offline.
- Build board, move, match detection, removal, gravity/refill, level goal, win, lose, and restart before map progression, boosters, shop, story, or events.
- Prefer one simple mode for MVP.
- Keep levels handcrafted or generated from simple original templates.
- Keep game logic deterministic and testable.
- Do not add ads during active puzzle play.
- Prefer rewarded ads for optional extra moves, continue, or booster trials.
- Use interstitials only at natural level-end transitions, with frequency caps.
- Keep the first prototype small enough to finish and test.

## Recommended Flow

1. Prompt MP1: Original game concept and MVP plan.
2. Prompt MP2: Game design document.
3. Prompt MP3: Flutter technical architecture.
4. Prompt MP4: First playable prototype.
5. Prompt MP5: Prototype fun and quality review.
6. Prompt MP6: Levels, blockers, boosters, and progression plan.
7. Prompt MP7: Monetization and analytics plan.
8. Prompt MP8: Store listing and creative asset plan.
9. Prompt MP9: Closed testing and release readiness.
10. Prompt MP10: Post-release improvement plan.

## Production V1 Requirement

Do not publish after only the first playable prototype. For a release-ready version 1, use `prompts/game-production-ready-prompt-pack.md` after the prototype review.

Production v1 should include polished UI, tested puzzle logic, enough levels, production-safe AdMob, analytics, truthful store assets, and release QA.

Suggested content target: 40-80 playable levels with gradual difficulty progression.

Run production prompts in this order:

1. `P1` production scope lock.
2. `P2` UI and gameplay polish.
3. `P3` level implementation.
4. `P4` AdMob and analytics implementation.
5. `P5` store assets and listing production.
6. `P6` production release readiness.

## Prompt MP1: Original Game Concept and MVP Plan

Use this before writing code.

```text
You are helping me plan an original Flutter match puzzle game.

Do not write code yet.

The game should be original. Do not copy names, art, UI, assets, exact branding, board layouts, levels, boosters, characters, or progression from Candy Crush, Royal Match, Toon Blast, Gardenscapes, Homescapes, Tile Master, or any other existing game.

What I want from you:
1. Define the core game idea in one sentence.
2. Define the target player.
3. Define the core loop.
4. Define what makes this game different.
5. Choose the best matching mechanic for MVP: swap match-3, tap-to-match, tile match, pair match, merge match, or another simple rule.
6. Define the smallest playable MVP.
7. Define the first screen flow.
8. Define board, move, match, removal, gravity/refill, win, and lose rules.
9. Define level goal structure for MVP.
10. Define 3 possible themes and recommend one.
11. Define what should not be built in version 1.
12. Define a user-friendly monetization direction.
13. Define the first prototype task.

Rules:
- Keep MVP small enough for a solo developer.
- Prefer one puzzle mode for version 1.
- Prefer offline levels.
- Do not add ads before the core loop is fun.
- Do not add map progression, story, shop, skins, login, cloud sync, or live events unless clearly needed later.

Expected output:
- One-sentence concept.
- Target player.
- Core loop.
- Matching mechanic decision.
- Differentiation.
- MVP scope.
- First screen flow.
- Game rules.
- Theme recommendation.
- Not-now list.
- Monetization direction.
- First prototype task.
```

## Prompt MP2: Game Design Document

Use this after the concept is clear.

```text
You are creating a game design document for my original Flutter match puzzle MVP.

Do not write code yet.

Use the approved concept from this task. If no concept exists, create a small original concept first and ask me to approve it before continuing.

What I want from you:
1. Game summary.
2. Core loop.
3. Session length target.
4. Puzzle mode and board size.
5. Tile or piece types.
6. Move rules.
7. Match detection rules.
8. Removal and scoring rules.
9. Gravity and refill rules.
10. Cascade rules.
11. Shuffle or no-move rules.
12. Level win and lose conditions.
13. Move limit, score target, collection target, or timed goal rules.
14. First 10 level design guidelines.
15. UI screens and HUD.
16. Sound and visual feedback.
17. Difficulty progression.
18. Analytics events.
19. Ad placement rules for later.
20. Done criteria for the first playable prototype.

Rules:
- Keep version 1 simple.
- Avoid complex blockers and boosters in the first prototype.
- Avoid map progression, story, shop, login, and cloud sync in MVP.
- Make rules precise enough for implementation and tests.
- Keep monetization out of active gameplay.

Expected output:
- Complete MVP game design document.
- Rule tables where useful.
- First 10 level guidelines.
- Prototype done criteria.
- Risks and open questions.
```

## Prompt MP3: Flutter Technical Architecture

Use this before implementation.

```text
You are designing the Flutter technical architecture for my original match puzzle game.

Use Flame only if it is clearly useful for animations, particle effects, and board interactions. If plain Flutter is better for this board puzzle scope, explain why.

Do not write code yet.

What I want from you:
1. Recommend Flame or plain Flutter.
2. Define folder structure.
3. Define pure puzzle engine model.
4. Define board representation.
5. Define tile model.
6. Define move validation.
7. Define match detection algorithm.
8. Define removal, gravity, refill, and cascade algorithm.
9. Define no-move and shuffle handling.
10. Define level data format.
11. Define scoring and level state.
12. Define local save data.
13. Define analytics event names.
14. Define future AdMob integration points.
15. Define test strategy.
16. Define the first implementation slice.

Rules:
- Keep puzzle logic separate from UI.
- Make board logic testable without Flutter widgets.
- Follow the existing project architecture if this is inside an existing repo.
- Keep the first implementation slice small.
- Do not add Firebase, AdMob, purchases, map progression, or booster economy yet unless explicitly approved.
- Avoid overengineering.

Expected output:
- Architecture decision.
- Folder structure.
- Main classes or components.
- Board and tile data model.
- Match/cascade algorithms.
- Data flow.
- First implementation slice.
- Test plan.
```

## Prompt MP4: First Playable Prototype

Use this to implement the first playable version.

```text
You are implementing the first playable prototype of my original Flutter match puzzle game.

Use the approved game design and technical architecture from this task. If no approved scope exists, create a small prototype scope and ask me to approve it before editing.

Scope:
- One playable level.
- One board size.
- Basic tile types.
- Approved move mechanic.
- Match detection.
- Tile removal.
- Gravity and refill.
- Cascades if approved.
- Move counter or simple goal.
- Win condition.
- Lose condition.
- Restart.
- Basic HUD.
- No ads.
- No boosters.
- No blockers.
- No map progression.
- No shop.

What I want from you:
1. Inspect the repository first.
2. Implement only the first playable prototype.
3. Keep puzzle logic pure and tested.
4. Keep UI simple and polished.
5. Follow existing project patterns.
6. Add focused tests for move validation, match detection, removal, gravity/refill, win, lose, and restart.
7. Use lightweight verification unless a build is essential.
8. Explain how to run and manually test the prototype.

Rules:
- Do not add monetization yet.
- Do not add unrelated features.
- Do not introduce large dependencies unless approved.
- Do not copy assets, boards, levels, boosters, UI, sounds, or branding from existing games.
- If using placeholder visuals, label them as placeholders.

Expected output:
- Files changed.
- Prototype behavior.
- Tests added.
- Manual test steps.
- Checks run or skipped.
- Remaining risks.
- Next recommended improvement.
```

## Prompt MP5: Prototype Fun and Quality Review

Use this after the first playable prototype exists.

```text
You are reviewing the first playable prototype of my original match puzzle game.

Inspect the repository and prototype implementation. Do not edit files.

What I want from you:
1. Review puzzle logic correctness.
2. Review move clarity and feedback.
3. Review match detection and cascade behavior.
4. Review level goal clarity.
5. Review whether difficulty is too easy, too hard, or okay.
6. Review visual and sound feedback opportunities.
7. Review performance risks.
8. Review code quality and test coverage.
9. Identify the top 3 fixes before adding features.
10. Identify what should not be added yet.
11. Create a small improvement scope.

Rules:
- Do not change code.
- Do not add ads yet.
- Prioritize correctness, readability, satisfying feedback, and test coverage before monetization.
- Keep recommendations practical.

Expected output:
- Correctness review.
- Fun and feedback review.
- Test coverage review.
- Top 3 fixes.
- Not-now list.
- Small improvement scope.
```

## Prompt MP6: Levels, Blockers, Boosters, and Progression Plan

Use this after the core prototype is playable.

```text
You are planning levels, blockers, boosters, and progression for my original match puzzle game.

Do not write code yet.

Use the current prototype and game design. Keep changes small enough for one update.

What I want from you:
1. Define first 20 level progression.
2. Define level difficulty variables.
3. Define how new tile types are introduced.
4. Define 3-5 blocker ideas.
5. Define 3-5 booster ideas.
6. Score each blocker and booster by fun, complexity, balance risk, and monetization risk.
7. Recommend only 1-2 additions for the next update.
8. Define reward loop.
9. Define implementation order.

Rules:
- Prefer handcrafted or simple generated levels for early versions.
- Do not add too many blockers or boosters at once.
- Keep difficulty fair and readable.
- Do not add monetization until the gameplay loop is stable.
- Avoid complex shop or booster economy in early versions.

Expected output:
- First 20 level plan.
- Difficulty variables.
- Blocker table.
- Booster table.
- Recommended next features.
- Reward loop.
- Implementation order.
```

## Prompt MP7: Monetization and Analytics Plan

Use this only after the game loop is fun enough.

```text
You are planning user-friendly monetization and analytics for my original match puzzle game.

Do not write code yet.

What I want from you:
1. Decide whether the game is ready for ads.
2. Define rewarded ad opportunities.
3. Define whether interstitial ads are appropriate.
4. Define frequency caps.
5. Define where ads must never appear.
6. Define analytics events needed to measure level difficulty, moves, failures, retention, booster use, and ad impact.
7. Define policy risks.
8. Create a safe implementation scope.

Rules:
- User experience comes before revenue.
- Policy compliance comes before revenue.
- Do not show ads during active puzzle play.
- Do not encourage ad clicks.
- Do not reward ad clicks.
- Prefer rewarded ads for optional extra moves, continues, or booster trials.
- Use interstitials only at natural level-end transitions.
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

## Prompt MP8: Store Listing and Creative Asset Plan

Use this when the game has enough real visuals for store assets.

```text
You are planning Google Play store listing assets for my original match puzzle game.

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
- Do not copy names, visuals, boards, tiles, boosters, characters, maps, or branding from other games.
- Do not show unavailable boosters, levels, rewards, maps, events, or modes.
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

## Prompt MP9: Closed Testing and Release Readiness

Use this before Play Store testing or release.

```text
You are checking closed testing and release readiness for my original Flutter match puzzle game.

Use the repository and release checklist. Do not publish anything.

What I want from you:
1. Review build and version readiness.
2. Review gameplay correctness.
3. Review level readiness.
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

## Prompt MP10: Post-Release Improvement Plan

Use this after testing or release.

```text
You are helping me improve my original match puzzle game after testing or release.

Use available tester feedback, reviews, analytics, Crashlytics, Android vitals, and AdMob data. If external data is missing, mark it as unknown.

What I want from you:
1. Summarize release health.
2. Identify gameplay correctness issues.
3. Identify level difficulty or progression issues.
4. Identify crash or performance issues.
5. Identify ad experience issues.
6. Identify retention, replay, or level failure issues.
7. Recommend the next small update.
8. Identify what should not be built yet.
9. Create a learning note.

Rules:
- Fix correctness and serious level frustration before adding new features.
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
Run Prompt MP1 from `prompts/match-puzzle-game-prompt-process.md`.
```

Then:

```text
Run Prompt MP2 from `prompts/match-puzzle-game-prompt-process.md` using the approved concept from this task.
```

Then:

```text
Run Prompt MP3 from `prompts/match-puzzle-game-prompt-process.md` using the approved game design from this task.
```

Only after approving architecture:

```text
Run Prompt MP4 from `prompts/match-puzzle-game-prompt-process.md` using the approved prototype scope from this task.
```

## Done Criteria

The game process is working when:

- The game has an original concept.
- The first prototype is playable.
- Board, moves, match detection, removal, gravity/refill, win, lose, and restart work.
- Puzzle logic has focused tests.
- Level goals are readable and fair.
- Cascades and feedback feel satisfying.
- Blockers and boosters are added gradually.
- Ads never interrupt active puzzle play.
- Store assets show real gameplay.
- Testing produces a learning note before the next update.
