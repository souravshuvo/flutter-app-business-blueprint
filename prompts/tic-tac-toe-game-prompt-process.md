# Tic Tac Toe Game Prompt Process

Use this prompt process to plan and build an original tic tac toe game for Flutter.

The goal is not to make a throwaway grid demo. The goal is to create a small, polished, testable, release-ready tic tac toe app with strong UX, fair AI, optional variants, safe monetization, and Play Store-ready assets.

## Purpose

Guide a tic tac toe game from rough idea to first playable prototype, then toward AI, variants, polish, monetization, store assets, testing, and release.

This process is designed for a solo Flutter developer. It favors correctness, simple UI, smooth interactions, and reusable game logic before online multiplayer, accounts, complex progression, or aggressive ads.

## When to Use

Use this process when:

- You want to create a new tic tac toe Flutter game.
- You want a small game that can be built, tested, released, and improved quickly.
- You want Codex to help with planning, architecture, prototype, review, monetization, and release.
- You want to reuse a disciplined process for simple board games.

Do not use this process to copy another game's name, UI, art, sound, icon, screenshots, monetization tricks, or branding.

## Core Rules

- Keep version 1 offline.
- Build correct 3x3 tic tac toe before variants.
- Keep game logic pure, deterministic, and well-tested.
- For AI, use a known deterministic strategy such as minimax or a clearly tested rule-based approach.
- Do not add online multiplayer, login, cloud sync, leaderboard, skins, or shop in MVP.
- Do not show ads during active play.
- Prefer rewarded ads only for optional cosmetics or hints if those features are added later.
- Use interstitials only at natural round/session transitions, with frequency caps.
- Keep the first prototype small enough to finish and test.

## Recommended Flow

1. Prompt TTT1: Original game concept and MVP plan.
2. Prompt TTT2: Game design document.
3. Prompt TTT3: Flutter technical architecture.
4. Prompt TTT4: First playable prototype.
5. Prompt TTT5: Prototype quality and correctness review.
6. Prompt TTT6: AI, variants, and polish plan.
7. Prompt TTT7: Monetization and analytics plan.
8. Prompt TTT8: Store listing and creative asset plan.
9. Prompt TTT9: Closed testing and release readiness.
10. Prompt TTT10: Post-release improvement plan.

## Production V1 Requirement

Do not publish after only the first playable prototype. For a release-ready version 1, use `prompts/game-production-ready-prompt-pack.md` after the prototype review.

Production v1 should include polished UI, tested game logic, at least local two-player plus one AI mode, production-safe AdMob if monetized, analytics, truthful store assets, and release QA.

Suggested content target: local two-player, one AI mode, polished score/session experience, and at least one small variant or difficulty improvement.

Run production prompts in this order:

1. `P1` production scope lock.
2. `P2` UI and gameplay polish.
3. `P3` mode/content implementation.
4. `P4` AdMob and analytics implementation.
5. `P5` store assets and listing production.
6. `P6` production release readiness.

## Prompt TTT1: Original Game Concept and MVP Plan

Use this before writing code.

```text
You are helping me plan an original Flutter tic tac toe game.

Do not write code yet.

The game should be polished and original in presentation. Do not copy names, art, UI, icons, sounds, screenshots, or branding from another tic tac toe app.

What I want from you:
1. Define the game idea in one sentence.
2. Define the target player.
3. Define the core loop.
4. Define what makes this app worth installing despite tic tac toe being simple.
5. Define the smallest playable MVP.
6. Define the first screen flow.
7. Define player modes for MVP.
8. Define board, turn, win, draw, restart, and scoring rules.
9. Define whether AI is included in MVP.
10. Define 3 possible visual themes and recommend one.
11. Define what should not be built in version 1.
12. Define a user-friendly monetization direction.
13. Define the first prototype task.

Rules:
- Keep MVP small enough for a solo developer.
- Prefer local two-player plus one AI difficulty if feasible.
- Do not add online multiplayer in version 1.
- Do not add ads before the game feels polished.
- Do not add shop, skins, login, cloud sync, or leaderboard unless clearly needed later.

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

## Prompt TTT2: Game Design Document

Use this after the concept is clear.

```text
You are creating a game design document for my original Flutter tic tac toe MVP.

Do not write code yet.

Use the approved concept from this task. If no concept exists, create a small original concept first and ask me to approve it before continuing.

What I want from you:
1. Game summary.
2. Core loop.
3. Session length target.
4. Game modes for MVP.
5. Board rules.
6. Turn rules.
7. Win and draw rules.
8. Score and match rules.
9. AI difficulty rules, if AI is included.
10. UI screens and HUD.
11. Animation and sound feedback.
12. Accessibility and readability rules.
13. Analytics events.
14. Ad placement rules for later.
15. Done criteria for the first playable prototype.

Rules:
- Keep version 1 simple.
- Make game logic precise enough for implementation and tests.
- Keep monetization out of active gameplay.
- Avoid online multiplayer, shop, skins, login, and cloud sync in MVP.

Expected output:
- Complete MVP game design document.
- Rule tables where useful.
- Prototype done criteria.
- Risks and open questions.
```

## Prompt TTT3: Flutter Technical Architecture

Use this before implementation.

```text
You are designing the Flutter technical architecture for my original tic tac toe game.

Do not write code yet.

What I want from you:
1. Recommend architecture for a small Flutter board game.
2. Define folder structure.
3. Define pure game engine model.
4. Define board state representation.
5. Define win/draw detection.
6. Define AI strategy: minimax, rule-based, or another tested approach.
7. Define UI state management.
8. Define local save data for settings and score.
9. Define analytics event names.
10. Define future AdMob integration points.
11. Define test strategy.
12. Define the first implementation slice.

Rules:
- Keep game logic separate from UI.
- Make game logic testable without Flutter widgets.
- Use a known deterministic strategy for AI or explain why a simpler tested rule-based AI is enough.
- Do not add Firebase, AdMob, purchases, leaderboard, online multiplayer, or cloud sync yet unless explicitly approved.
- Avoid overengineering.

Expected output:
- Architecture decision.
- Folder structure.
- Main classes or services.
- Game logic data model.
- AI approach.
- Data flow.
- First implementation slice.
- Test plan.
```

## Prompt TTT4: First Playable Prototype

Use this to implement the first playable version.

```text
You are implementing the first playable prototype of my original Flutter tic tac toe game.

Use the approved game design and technical architecture from this task. If no approved scope exists, create a small prototype scope and ask me to approve it before editing.

Scope:
- 3x3 board.
- Local two-player mode.
- Turn indicator.
- Tap to place X or O.
- Win detection.
- Draw detection.
- Restart.
- Basic score for current session.
- Simple polished UI.
- No ads.
- No online multiplayer.
- No shop.
- No leaderboard.

Optional only if approved:
- One AI difficulty.
- Basic settings for sound or vibration.

What I want from you:
1. Inspect the repository first.
2. Implement only the first playable prototype.
3. Keep game logic pure and tested.
4. Keep UI simple and polished.
5. Follow existing project patterns.
6. Add focused tests for win, draw, invalid move, restart, and AI if included.
7. Use lightweight verification unless a build is essential.
8. Explain how to run and manually test the prototype.

Rules:
- Do not add monetization yet.
- Do not add unrelated features.
- Do not introduce large dependencies unless approved.
- Do not copy assets, UI, sounds, icon, or branding from existing games.
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

## Prompt TTT5: Prototype Quality and Correctness Review

Use this after the first playable prototype exists.

```text
You are reviewing the first playable prototype of my original tic tac toe game.

Inspect the repository and prototype implementation. Do not edit files.

What I want from you:
1. Review game logic correctness.
2. Review invalid move handling.
3. Review win and draw detection.
4. Review restart and score behavior.
5. Review AI fairness and difficulty if AI exists.
6. Review UI clarity and tap feedback.
7. Review accessibility and small-screen readability.
8. Review code quality and test coverage.
9. Identify the top 3 fixes before adding features.
10. Identify what should not be added yet.
11. Create a small improvement scope.

Rules:
- Do not change code.
- Do not add ads yet.
- Prioritize correctness, polish, accessibility, and test coverage before monetization.
- Keep recommendations practical.

Expected output:
- Correctness review.
- UX review.
- Test coverage review.
- Top 3 fixes.
- Not-now list.
- Small improvement scope.
```

## Prompt TTT6: AI, Variants, and Polish Plan

Use this after the core prototype is playable and correct.

```text
You are planning AI, variants, and polish for my original tic tac toe game.

Do not write code yet.

Use the current prototype and game design. Keep changes small enough for one update.

What I want from you:
1. Define AI difficulty options.
2. Define the recommended AI strategy for each difficulty.
3. Define optional game variants.
4. Score each variant by fun, complexity, replay value, and confusion risk.
5. Recommend only 1-2 additions for the next update.
6. Define animation, sound, haptic, and accessibility polish.
7. Define implementation order.

Possible variants to evaluate:
- 4x4 board.
- Best-of series.
- Timed turns.
- Misere/reverse tic tac toe.
- Wildcard cell.
- Local tournament mode.

Rules:
- Prefer polish and AI before too many variants.
- Do not add online multiplayer yet.
- Do not add confusing variants unless the core game explains them clearly.
- Do not add monetization until the gameplay and UI feel polished.

Expected output:
- AI difficulty plan.
- Variant table.
- Recommended next features.
- Polish checklist.
- Implementation order.
```

## Prompt TTT7: Monetization and Analytics Plan

Use this only after the game is polished enough.

```text
You are planning user-friendly monetization and analytics for my original tic tac toe game.

Do not write code yet.

What I want from you:
1. Decide whether the game is ready for ads.
2. Define whether rewarded ads are useful.
3. Define whether interstitial ads are appropriate.
4. Define frequency caps.
5. Define where ads must never appear.
6. Define analytics events needed to measure round completion, replay, difficulty, retention, and ad impact.
7. Define policy risks.
8. Create a safe implementation scope.

Rules:
- User experience comes before revenue.
- Policy compliance comes before revenue.
- Do not show ads during active rounds.
- Do not encourage ad clicks.
- Do not reward ad clicks.
- Avoid aggressive ads because tic tac toe sessions are short.
- Use interstitials only after several completed rounds or at natural session transitions.
- Add frequency caps before scaling ads.

Expected output:
- Monetization readiness decision.
- Rewarded ad plan, if useful.
- Interstitial plan, if appropriate.
- Frequency cap rules.
- Analytics event list.
- Policy risk review.
- Implementation scope.
```

## Prompt TTT8: Store Listing and Creative Asset Plan

Use this when the game has enough real visuals for store assets.

```text
You are planning Google Play store listing assets for my original tic tac toe game.

Use real game screens and actual gameplay. Do not fake gameplay.

What I want from you:
1. Store title ideas.
2. Short description ideas.
3. Full description outline.
4. Screenshot storyboard.
5. Feature graphic concept.
6. App icon concept.
7. Preview video recommendation.
8. Policy and misleading-claim review.
9. Asset production checklist.

Rules:
- Do not copy names, visuals, boards, icons, sounds, or branding from other games.
- Do not show unavailable AI modes, variants, themes, rewards, or multiplayer.
- Do not use fake rankings, awards, downloads, reviews, or earnings.
- Keep screenshots based on actual gameplay.

Expected output:
- Store listing copy ideas.
- Screenshot plan.
- Feature graphic brief.
- Icon brief.
- Preview video recommendation.
- Asset checklist.
```

## Prompt TTT9: Closed Testing and Release Readiness

Use this before Play Store testing or release.

```text
You are checking closed testing and release readiness for my original Flutter tic tac toe game.

Use the repository and release checklist. Do not publish anything.

What I want from you:
1. Review build and version readiness.
2. Review gameplay correctness.
3. Review AI and variant readiness.
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

## Prompt TTT10: Post-Release Improvement Plan

Use this after testing or release.

```text
You are helping me improve my original tic tac toe game after testing or release.

Use available tester feedback, reviews, analytics, Crashlytics, Android vitals, and AdMob data. If external data is missing, mark it as unknown.

What I want from you:
1. Summarize release health.
2. Identify gameplay correctness issues.
3. Identify AI or variant issues.
4. Identify crash or performance issues.
5. Identify ad experience issues.
6. Identify retention or replay issues.
7. Recommend the next small update.
8. Identify what should not be built yet.
9. Create a learning note.

Rules:
- Fix correctness and UX issues before adding new features.
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
Run Prompt TTT1 from `prompts/tic-tac-toe-game-prompt-process.md`.
```

Then:

```text
Run Prompt TTT2 from `prompts/tic-tac-toe-game-prompt-process.md` using the approved concept from this task.
```

Then:

```text
Run Prompt TTT3 from `prompts/tic-tac-toe-game-prompt-process.md` using the approved game design from this task.
```

Only after approving architecture:

```text
Run Prompt TTT4 from `prompts/tic-tac-toe-game-prompt-process.md` using the approved prototype scope from this task.
```

## Done Criteria

The game process is working when:

- The game has a clear original presentation.
- The first prototype is playable.
- Board, turns, wins, draws, invalid moves, score, and restart are correct.
- Game logic has focused tests.
- AI is fair and understandable if included.
- UI is readable, responsive, and polished.
- Ads never interrupt active rounds.
- Store assets show real gameplay.
- Testing produces a learning note before the next update.
