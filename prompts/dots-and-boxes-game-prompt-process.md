# Dots and Boxes Game Prompt Process

Use this prompt process to plan and build an original Dots and Boxes game for Flutter.

Dots and Boxes is a turn-based grid strategy game where players draw lines between dots. When a player completes the fourth side of a box, they claim that box and get another turn. The goal is to create a polished mobile version with correct line/box logic, clean touch controls, local multiplayer, bot play, safe monetization, and production-ready store assets.

## Purpose

Guide a Dots and Boxes game from rules and data model validation to first playable prototype, then toward bot difficulty, board presets, themes, scoring history, monetization, store assets, testing, and release.

This process is designed for a solo Flutter developer. It favors a correct and testable game engine before animations, bot intelligence, themes, online multiplayer, or complex progression systems.

## When to Use

Use this process when:

- You want to create a Dots and Boxes, dot grid, line drawing, or box capture strategy game.
- You want an offline two-player strategy game that can be finished and released.
- You want Codex to help with board logic, architecture, prototype, review, monetization, and release.
- You want the game to become a polished Play Store product, not only a prototype.

Do not use this process to copy another game's name, UI, board art, sound, animations, monetization tricks, store assets, or branding.

## Core Board Model

Dots and Boxes operates on a `(rows + 1) x (cols + 1)` dot grid, creating a `rows x cols` matrix of scoreable boxes.

Example: a `5 x 5` dot grid creates `4 x 4` boxes.

Recommended domain model:

```dart
enum PlayerType { player1, player2, none }

class DotsAndBoxesGame {
  DotsAndBoxesGame({this.rows = 4, this.cols = 4}) {
    horizontalLines = List.generate(rows + 1, (_) => List.filled(cols, false));
    verticalLines = List.generate(rows, (_) => List.filled(cols + 1, false));
    boxOwners = List.generate(rows, (_) => List.filled(cols, PlayerType.none));
  }

  final int rows;
  final int cols;

  late List<List<bool>> horizontalLines; // (rows + 1) x cols
  late List<List<bool>> verticalLines; // rows x (cols + 1)
  late List<List<PlayerType>> boxOwners; // rows x cols
}
```

Core completion logic:

```dart
bool isBoxComplete(int r, int c) {
  return horizontalLines[r][c] &&
      horizontalLines[r + 1][c] &&
      verticalLines[r][c] &&
      verticalLines[r][c + 1];
}
```

Core move rules:

- A player draws one undrawn horizontal or vertical line.
- If that line completes one or more boxes, the current player owns those boxes.
- If a player completes at least one box, they get another turn.
- If no box is completed, the turn passes to the other player.
- The game ends when every box is owned.
- The winner is the player with more boxes.

## Core Rules

- Keep version 1 offline.
- Lock rows/cols presets and board scaling before UI polish.
- Keep line drawing and box completion rules in pure Dart where practical.
- Drawing a line that is already drawn must be rejected safely.
- A single line can complete two adjacent boxes and should award both boxes.
- Extra turn logic must be correct and tested.
- Touch detection should be forgiving near line boundaries but must not select the wrong line.
- Use `CustomPainter` for the board and `GestureDetector` or equivalent for touch input.
- Do not show ads during active turns, line drawing, box completion animation, or game-over animation.
- Prefer interstitial ads only after match end or clear session breaks, with frequency caps.
- Prefer rewarded ads only for optional hints, undo, cosmetic themes, or training content.
- Keep the first prototype small enough to finish and test.

## Recommended Flow

1. Prompt DAB1: Rules, grid, and data model validation.
2. Prompt DAB2: Original game concept and MVP plan.
3. Prompt DAB3: Game design document.
4. Prompt DAB4: Flutter technical architecture.
5. Prompt DAB5: First playable prototype.
6. Prompt DAB6: Prototype rule and quality review.
7. Prompt DAB7: Bot, hints, undo, and progression plan.
8. Prompt DAB8: Monetization and analytics plan.
9. Prompt DAB9: Store listing and creative asset plan.
10. Prompt DAB10: Closed testing, release readiness, and post-release improvement.

## Production V1 Requirement

Do not publish after only the first playable prototype. For a release-ready version 1, use `prompts/game-production-ready-prompt-pack.md` after the prototype review.

Production v1 should include polished board UI, correct line/box/extra-turn logic, local two-player mode, one bot mode, multiple grid sizes, score history, production-safe AdMob, analytics, truthful store assets, and release QA.

Suggested content target: local two-player, player vs bot, 3-4 grid presets such as 3x3, 4x4, 5x5, and 6x6 boxes, 2-3 bot difficulty levels or one reliable bot, undo or hint support if approved, and complete line/box completion tests.

Run production prompts in this order:

1. `P1` production scope lock.
2. `P2` UI and gameplay polish.
3. `P3` bot, grid presets, hints, undo, and settings implementation.
4. `P4` AdMob and analytics implementation.
5. `P5` store assets and listing production.
6. `P6` production release readiness.

## Prompt DAB1: Rules, Grid, and Data Model Validation

Use this before game design or coding.

```text
You are helping me validate the rules, grid model, and data structures for an original Flutter Dots and Boxes game.

Do not write code yet.

First, inspect any existing board logic, notes, code, or assets in the repository. If no implementation exists, use this brief and create a precise rule specification.

Core model:
- `rows` and `cols` represent scoreable boxes.
- Dots are `(rows + 1) x (cols + 1)`.
- Horizontal lines are `(rows + 1) x cols`.
- Vertical lines are `rows x (cols + 1)`.
- Box owners are `rows x cols`.

What I want from you:
1. Define the exact board model.
2. Define line identifiers for horizontal and vertical lines.
3. Define valid index ranges.
4. Define box completion logic.
5. Define how one line can complete one or two boxes.
6. Define extra-turn behavior.
7. Define invalid move behavior.
8. Define game-over and winner rules.
9. Define draw rules.
10. Define grid size presets for version 1.
11. Define validation checks required before gameplay implementation.
12. Define test cases for line drawing, box completion, extra turns, and game over.

Rules:
- Do not guess silently.
- Mark assumptions clearly.
- Prefer a complete and testable engine specification over visual polish.
- If grid sizes or rules are inconsistent, stop at a correction plan and ask for approval.

Expected output:
- Final rules specification.
- Matrix size specification.
- Line and box indexing rules.
- Extra-turn and game-over rules.
- Implementation-ready test checklist.
```

## Prompt DAB2: Original Game Concept and MVP Plan

Use this after rules and data model are validated.

```text
You are helping me plan an original Flutter Dots and Boxes game.

Do not write code yet.

Use the approved rules and data model specification from this task.

What I want from you:
1. Define the core game idea in one sentence.
2. Define the target player.
3. Define the casual strategy hook.
4. Define the core loop.
5. Define what makes this version different.
6. Define the smallest playable MVP.
7. Define the first screen flow.
8. Define local two-player rules.
9. Define player vs bot rules.
10. Define touch interaction rules.
11. Define line highlight and box capture feedback.
12. Define what should not be built in version 1.
13. Define a user-friendly monetization direction.
14. Define the first prototype task.

Rules:
- Keep MVP small enough for a solo developer.
- Prefer offline local two-player before online multiplayer.
- Do not add ads before the line/box engine is correct.
- Do not add login, cloud sync, online multiplayer, chat, complex shop, or live events.
- Keep the game family-friendly and policy-safe.

Expected output:
- One-sentence concept.
- Target player.
- Strategy hook.
- Core loop.
- Differentiation.
- MVP scope.
- First screen flow.
- Interaction rules.
- Not-now list.
- Monetization direction.
- First prototype task.
```

## Prompt DAB3: Game Design Document

Use this after the concept is clear.

```text
You are creating a game design document for my original Flutter Dots and Boxes MVP.

Do not write code yet.

Use the approved rules/data model specification and concept from this task.

What I want from you:
1. Game summary.
2. Core loop.
3. Session length target.
4. MVP game modes.
5. Board/grid presets.
6. Line drawing rules.
7. Box completion rules.
8. Extra-turn rules.
9. Turn flow.
10. Legal line highlighting.
11. Invalid move feedback.
12. Win, lose, and draw rules.
13. Bot behavior for MVP.
14. UI screens and HUD.
15. Sound, haptics, and visual feedback.
16. Analytics events.
17. Ad placement rules for later.
18. Done criteria for the first playable prototype.

Rules:
- Make rules precise enough for implementation.
- Keep version 1 simple.
- Avoid online play, chat, account systems, leaderboards, and complex cosmetics in MVP.
- Keep monetization out of active turns.
- Rule correctness is more important than visual effects.

Expected output:
- Complete MVP game design document.
- Rule tables where useful.
- Screen flow.
- Prototype done criteria.
- Risks and open questions.
```

## Prompt DAB4: Flutter Technical Architecture

Use this before implementation.

```text
You are designing the Flutter technical architecture for my original Dots and Boxes game.

Use plain Flutter unless a game library is clearly justified. This game should usually work well with Flutter widgets, CustomPainter, animations, state management, and pure Dart board logic.

Do not write code yet.

What I want from you:
1. Recommend plain Flutter or a game library.
2. Define folder structure.
3. Define domain model: game state, player, line, horizontal line, vertical line, box, move, turn, bot, match result.
4. Define immutable or mutable board state approach.
5. Define line drawing logic.
6. Define adjacent box lookup.
7. Define box completion detection.
8. Define extra-turn flow.
9. Define bot move selection.
10. Define CustomPainter board rendering.
11. Define touch detection near line boundaries.
12. Define local save data for settings and match history if included.
13. Define analytics event names.
14. Define future AdMob integration points.
15. Define test strategy.
16. Define the first implementation slice.

Rules:
- Follow the existing project architecture if this is inside an existing repo.
- Keep board rules in pure Dart where practical.
- Keep UI separate from board rules.
- Do not add Firebase, AdMob, purchases, online play, cloud sync, or complex themes yet unless explicitly approved.
- Add board engine tests before relying on the UI.
- Avoid overengineering.

Expected output:
- Architecture decision.
- Folder structure.
- Main classes or components.
- Board validation approach.
- Line/box/turn state flow.
- Data flow.
- First implementation slice.
- Test plan.
```

## Prompt DAB5: First Playable Prototype

Use this to implement the first playable version.

```text
You are implementing the first playable prototype of my original Flutter Dots and Boxes game.

Use the approved rules specification, game design, and technical architecture from this task. If no approved scope exists, create a small prototype scope and ask me to approve it before editing.

Scope:
- Main menu.
- Local two-player mode.
- One default grid size, such as 4x4 boxes.
- Board rendered with CustomPainter or equivalent.
- Touch detection for horizontal and vertical lines.
- Turn indicator.
- Draw line.
- Complete box.
- Award extra turn after completed box.
- Score display.
- Game-over and winner/draw result.
- Restart.
- No ads.
- No online play.
- No shop.
- No leaderboard.

What I want from you:
1. Inspect the repository first.
2. Implement only the first playable prototype.
3. Keep code small and reviewable.
4. Follow existing project patterns.
5. Add unit tests for line drawing, box completion, extra turns, and game over where practical.
6. Use lightweight verification unless a build is essential.
7. Explain how to run and manually test the prototype.

Rules:
- Do not add monetization yet.
- Do not add unrelated features.
- Do not introduce large dependencies unless approved.
- Do not copy UI, board art, icons, sounds, or assets from existing games.
- If using placeholder visuals, label them as placeholders.
- Do not proceed if the line/box model is incomplete or inconsistent.

Expected output:
- Files changed.
- Prototype behavior.
- Board engine rules covered.
- Manual test steps.
- Checks run or skipped.
- Remaining risks.
- Next recommended improvement.
```

## Prompt DAB6: Prototype Rule and Quality Review

Use this after the first playable prototype exists.

```text
You are reviewing the first playable prototype of my original Dots and Boxes game.

Inspect the repository and prototype implementation. Do not edit files.

What I want from you:
1. Review whether matrix sizes match the approved specification.
2. Review whether line drawing prevents duplicate moves.
3. Review whether adjacent box lookup is correct.
4. Review whether completing one or two boxes works.
5. Review whether extra-turn behavior is correct.
6. Review whether game-over and winner/draw rules are correct.
7. Review whether touch interaction is clear and forgiving.
8. Review UI polish and readability.
9. Review performance risks.
10. Review code quality risks.
11. Identify the top 3 fixes before adding features.
12. Identify what should not be added yet.
13. Create a small improvement scope.

Rules:
- Do not change code.
- Do not add ads yet.
- Prioritize rule correctness, board clarity, touch reliability, and feedback before monetization.
- Keep recommendations practical.

Expected output:
- Rule correctness review.
- Board engine review.
- Quality review.
- Top 3 fixes.
- Not-now list.
- Small improvement scope.
```

## Prompt DAB7: Bot, Hints, Undo, and Progression Plan

Use this after the local two-player prototype is playable and correct.

```text
You are planning bot play, hints, undo, grid presets, settings, match history, and replay value for my original Dots and Boxes game.

Do not write code yet.

Use the current prototype and game design. Keep changes small enough for one update.

What I want from you:
1. Define production v1 game modes.
2. Define player vs bot behavior.
3. Define 2-3 possible bot difficulty levels.
4. Define hint behavior.
5. Define undo behavior.
6. Define grid presets.
7. Define local match history.
8. Define board and line theme options.
9. Score each idea by user value, effort, risk, monetization fit, and policy risk.
10. Recommend only the best next additions.
11. Define implementation order.

Rules:
- Prefer reliable basic AI over clever but buggy AI.
- Do not add online multiplayer, chat, accounts, live events, cloud sync, or tournaments in early versions.
- Do not create features only to force more ad impressions.
- Hints should never break game rules.
- Undo should be clear and fair.

Expected output:
- Mode plan.
- Bot behavior plan.
- Hint/undo plan.
- Grid preset plan.
- Optional feature score table.
- Recommended next additions.
- Implementation order.
```

## Prompt DAB8: Monetization and Analytics Plan

Use this only after the line/box engine is correct and the game loop is stable.

```text
You are planning user-friendly monetization and analytics for my original Dots and Boxes game.

Do not write code yet.

What I want from you:
1. Decide whether the game is ready for ads.
2. Define whether banner ads are appropriate.
3. Define whether interstitial ads are appropriate.
4. Define rewarded ad opportunities, if any.
5. Define frequency caps.
6. Define where ads must never appear.
7. Define analytics events needed to measure match starts, match finishes, grid size, move counts, boxes completed, extra turns, undo usage, hint usage, bot difficulty, session length, retention, and ad impact.
8. Define Play policy and invalid traffic risks.
9. Create a safe implementation scope.

Rules:
- User experience comes before revenue.
- Policy compliance comes before revenue.
- Do not show ads during active turn selection.
- Do not show ads during line draw or box completion animation.
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

## Prompt DAB9: Store Listing and Creative Asset Plan

Use this when the game has enough real visuals for store assets.

```text
You are planning Google Play store listing assets for my original Dots and Boxes game.

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
- Do not copy names, visuals, board art, UI, screenshots, sounds, or branding from other games.
- Do not show unavailable online play, tournaments, ranks, rewards, or features.
- Do not use fake rankings, awards, downloads, reviews, or earnings.
- Keep screenshots based on actual gameplay.
- Make the dots, lines, boxes, scores, and turn state easy to inspect in screenshots.

Expected output:
- Store listing copy ideas.
- Screenshot plan.
- Feature graphic brief.
- Icon brief.
- Preview video script.
- Asset checklist.
```

## Prompt DAB10: Closed Testing, Release Readiness, and Post-Release Improvement

Use this before Play Store testing or after the first testing cycle.

```text
You are checking release readiness and improvement priorities for my original Flutter Dots and Boxes game.

Use the repository, release checklist, tester feedback, analytics, Crashlytics, Android vitals, and AdMob data where available. If external data is missing, mark it as unknown.

What I want from you:
1. Review build and version readiness.
2. Review line/box engine readiness.
3. Review local two-player and bot readiness.
4. Review grid preset readiness.
5. Review hint/undo/settings readiness if included.
6. Review crash and performance risks.
7. Review ads and analytics readiness.
8. Review permissions and privacy risk.
9. Review Data safety impact.
10. Review store listing readiness.
11. Create a manual QA checklist.
12. Recommend internal test, closed test, delay, production release, or next small update.

Rules:
- Do not claim release readiness if checks were not run.
- Keep unknowns clear.
- Prefer internal or closed testing if risk is unclear.
- Do not run heavy build/install/emulator unless explicitly approved.
- Block release if line drawing, box completion, extra-turn, scoring, or game-over logic is not verified.

Expected output:
- Release readiness summary.
- Blockers.
- Manual QA checklist.
- Play Console checklist.
- Top improvement priorities.
- Recommendation.
```

## Quick Copy-Paste Sequence

Start with:

```text
Run Prompt DAB1 from `prompts/dots-and-boxes-game-prompt-process.md`.
```

Then:

```text
Run Prompt DAB2 from `prompts/dots-and-boxes-game-prompt-process.md` using the approved rules and data model specification from this task.
```

Then:

```text
Run Prompt DAB3 from `prompts/dots-and-boxes-game-prompt-process.md` using the approved concept from this task.
```

Then:

```text
Run Prompt DAB4 from `prompts/dots-and-boxes-game-prompt-process.md` using the approved game design from this task.
```

Only after approving architecture:

```text
Run Prompt DAB5 from `prompts/dots-and-boxes-game-prompt-process.md` using the approved prototype scope from this task.
```

After the prototype is playable and reviewed:

```text
Run Prompt P1 from `prompts/game-production-ready-prompt-pack.md` for the current repository.
```

## Done Criteria

The game process is working when:

- The board model is validated.
- The game has an original concept.
- The first prototype is playable.
- Horizontal lines, vertical lines, box ownership, extra turns, scoring, game over, and restart work correctly.
- Touch detection is reliable and readable.
- Local two-player mode works.
- Player vs bot works for production v1 if approved.
- UI is clear and polished enough for casual strategy players.
- Ads never interrupt active turns or box completion.
- Store assets show real gameplay.
- Testing produces a learning note before the next update.
