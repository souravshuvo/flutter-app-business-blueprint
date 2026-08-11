# Sholo Guti Game Prompt Process

Use this prompt process to plan and build an original Sholo Guti / 16 Beads game for Flutter.

Sholo Guti is a tactical graph-based board game where two players move and capture beads across connected intersection nodes. The goal is to create a polished mobile version with correct board logic, readable moves, local multiplayer, AI play, useful hints, safe monetization, and production-ready store assets.

## Purpose

Guide a Sholo Guti game from board/rule validation to first playable prototype, then toward AI, rule polish, match history, monetization, store assets, testing, and release.

This process is designed for a solo Flutter developer. It favors a correct and testable board engine before visual polish, bot difficulty, themes, online multiplayer, or complex account systems.

## When to Use

Use this process when:

- You want to create a Sholo Guti, 16 Guti, 16 Beads, or Sixteen Soldiers strategy board game.
- You want an offline two-player strategy game that can be finished and released.
- You want Codex to help with board graph design, architecture, prototype, review, monetization, and release.
- You want the game to become a polished Play Store product, not only a prototype.

Do not use this process to copy another game's name, UI, board art, bead designs, sounds, monetization tricks, store assets, or branding.

## Core Board Model

Sholo Guti should be represented as a graph, not as a simple rectangular grid.

Important: the board must be validated before implementation. Traditional digital Sholo Guti commonly uses 37 valid intersections, but some drafts or diagrams may label fewer nodes. If the provided diagram labels only `0-31`, Codex must not silently implement a 32-node board while claiming it is a 37-node board. It must reconcile the exact board map first.

Recommended domain model:

```dart
enum PlayerType { player1, player2, none }

class BoardNode {
  BoardNode({
    required this.id,
    required this.xRatio,
    required this.yRatio,
    required this.connectedNodes,
    this.currentOccupant = PlayerType.none,
  });

  final int id;
  final double xRatio;
  final double yRatio;
  final List<int> connectedNodes;
  PlayerType currentOccupant;
}
```

Core movement model:

- Normal move: move one bead to an adjacent connected empty node.
- Capture move: jump from source node A over adjacent opponent node B into empty destination node C.
- A, B, and C must be connected along a valid board line.
- Captured bead at B is removed.
- Multi-capture rules must be locked before implementation because local variants differ.
- Win condition: capture all opponent beads or block all legal opponent moves, depending on approved rules.

## Core Rules

- Keep version 1 offline.
- Lock the exact board graph before coding gameplay.
- Validate node count, coordinates, bidirectional edges, jump paths, initial placement, and legal move generation.
- Build local two-player mode before bot difficulty, hints, themes, or online play.
- Keep game rules in pure Dart where practical.
- Every legal move and capture should be highlightable before the player commits.
- Do not show ads during active turn selection, move animation, capture chain, or game over animation.
- Prefer interstitial ads only after match end or clear session breaks, with frequency caps.
- Prefer rewarded ads only for optional hints, undo packs, cosmetic boards, or training content.
- Keep the first prototype small enough to finish and test.

## Recommended Flow

1. Prompt SG1: Board and rule validation.
2. Prompt SG2: Original game concept and MVP plan.
3. Prompt SG3: Game design document.
4. Prompt SG4: Flutter technical architecture.
5. Prompt SG5: First playable prototype.
6. Prompt SG6: Prototype rule and quality review.
7. Prompt SG7: AI, hints, undo, and progression plan.
8. Prompt SG8: Monetization and analytics plan.
9. Prompt SG9: Store listing and creative asset plan.
10. Prompt SG10: Closed testing, release readiness, and post-release improvement.

## Production V1 Requirement

Do not publish after only the first playable prototype. For a release-ready version 1, use `prompts/game-production-ready-prompt-pack.md` after the prototype review.

Production v1 should include a validated 37-node board graph, correct movement and capture logic, local two-player mode, one bot mode, move highlighting, match result, local settings, production-safe AdMob, analytics, truthful store assets, and release QA.

Suggested content target: local two-player, player vs bot, 2-3 bot difficulty levels or one reliable bot, undo or hint support if approved, match history, board/bead theme options, and complete move/capture validation tests.

Run production prompts in this order:

1. `P1` production scope lock.
2. `P2` UI and gameplay polish.
3. `P3` AI, hints, undo, settings, and content implementation.
4. `P4` AdMob and analytics implementation.
5. `P5` store assets and listing production.
6. `P6` production release readiness.

## Prompt SG1: Board and Rule Validation

Use this before game design or coding.

```text
You are helping me validate the board and rules for an original Flutter Sholo Guti / 16 Beads game.

Do not write code yet.

First, inspect any existing board diagrams, notes, code, or assets in the repository. If no implementation exists, use the provided rule brief and create a precise board/rule specification.

Important:
- Traditional Sholo Guti is commonly described as a 37-intersection board.
- If a provided diagram labels only `0-31`, treat it as incomplete or variant-specific.
- Do not silently implement a 32-node board while calling it a 37-node board.
- Reconcile the final board graph before implementation.

What I want from you:
1. Define the exact board node count.
2. Define every node coordinate as screen ratios.
3. Define every direct edge.
4. Define every valid jump path.
5. Confirm edges are bidirectional.
6. Confirm all jump paths are collinear along board lines.
7. Define initial bead positions for player 1 and player 2.
8. Define empty starting nodes.
9. Define normal move rules.
10. Define capture rules.
11. Decide whether multi-capture is allowed, mandatory, or optional.
12. Decide whether backward moves are allowed, restricted, or variant-based.
13. Define win and draw/stalemate rules.
14. Create validation checks required before gameplay implementation.

Rules:
- Do not guess silently.
- Mark assumptions clearly.
- Prefer a complete and testable board graph over a visually approximate board.
- If the board/rules are inconsistent, stop at a correction plan and ask for approval.

Expected output:
- Final board specification.
- Node/edge/jump-path validation notes.
- Initial placement.
- Movement and capture rules.
- Variant assumptions.
- Implementation-ready rule checklist.
```

## Prompt SG2: Original Game Concept and MVP Plan

Use this after board and rules are validated.

```text
You are helping me plan an original Flutter Sholo Guti / 16 Beads game.

Do not write code yet.

Use the approved board and rule specification from this task.

What I want from you:
1. Define the core game idea in one sentence.
2. Define the target player.
3. Define the cultural/nostalgic hook.
4. Define the core loop.
5. Define what makes this version different.
6. Define the smallest playable MVP.
7. Define the first screen flow.
8. Define local two-player rules.
9. Define player vs bot rules.
10. Define touch interaction rules.
11. Define move highlighting and capture feedback.
12. Define what should not be built in version 1.
13. Define a user-friendly monetization direction.
14. Define the first prototype task.

Rules:
- Keep MVP small enough for a solo developer.
- Prefer offline local two-player before online multiplayer.
- Do not add ads before the move/capture engine is correct.
- Do not add login, cloud sync, online multiplayer, chat, complex shop, or live events.
- Keep the game family-friendly and policy-safe.

Expected output:
- One-sentence concept.
- Target player.
- Cultural hook.
- Core loop.
- Differentiation.
- MVP scope.
- First screen flow.
- Interaction rules.
- Not-now list.
- Monetization direction.
- First prototype task.
```

## Prompt SG3: Game Design Document

Use this after the concept is clear.

```text
You are creating a game design document for my original Flutter Sholo Guti MVP.

Do not write code yet.

Use the approved board/rule specification and concept from this task.

What I want from you:
1. Game summary.
2. Core loop.
3. Session length target.
4. MVP game modes.
5. Board graph summary.
6. Initial setup.
7. Normal move rules.
8. Capture and multi-capture rules.
9. Turn flow.
10. Legal move highlighting.
11. Invalid move feedback.
12. Win, lose, draw, and blocked-move rules.
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

## Prompt SG4: Flutter Technical Architecture

Use this before implementation.

```text
You are designing the Flutter technical architecture for my original Sholo Guti game.

Use plain Flutter unless a game library is clearly justified. This game should usually work well with Flutter widgets, CustomPainter, animations, state management, and pure Dart board logic.

Do not write code yet.

What I want from you:
1. Recommend plain Flutter or a game library.
2. Define folder structure.
3. Define domain model: board node, edge, jump path, bead, move, capture, turn, player, bot, match result.
4. Define immutable or mutable board state approach.
5. Define legal move generation.
6. Define capture detection.
7. Define multi-capture flow.
8. Define bot move selection.
9. Define CustomPainter board rendering.
10. Define node/bead touch handling.
11. Define local save data for settings and match history if included.
12. Define analytics event names.
13. Define future AdMob integration points.
14. Define test strategy.
15. Define the first implementation slice.

Rules:
- Follow the existing project architecture if this is inside an existing repo.
- Keep board rules in pure Dart where practical.
- Keep UI separate from board rules.
- Do not add Firebase, AdMob, purchases, online play, cloud sync, or complex themes yet unless explicitly approved.
- Add board validation tests before relying on the graph.
- Avoid overengineering.

Expected output:
- Architecture decision.
- Folder structure.
- Main classes or components.
- Board validation approach.
- Move/capture state flow.
- Data flow.
- First implementation slice.
- Test plan.
```

## Prompt SG5: First Playable Prototype

Use this to implement the first playable version.

```text
You are implementing the first playable prototype of my original Flutter Sholo Guti game.

Use the approved board specification, game design, and technical architecture from this task. If no approved scope exists, create a small prototype scope and ask me to approve it before editing.

Scope:
- Main menu.
- Local two-player mode.
- Validated board graph.
- Board rendered with CustomPainter or equivalent.
- 16 beads per player.
- Turn indicator.
- Select bead.
- Highlight legal moves and captures.
- Normal move.
- Capture move.
- Multi-capture only if approved.
- Win/loss detection.
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
5. Add unit tests for board validation, legal moves, captures, and win conditions where practical.
6. Use lightweight verification unless a build is essential.
7. Explain how to run and manually test the prototype.

Rules:
- Do not add monetization yet.
- Do not add unrelated features.
- Do not introduce large dependencies unless approved.
- Do not copy UI, board art, bead designs, icons, or assets from existing games.
- If using placeholder visuals, label them as placeholders.
- Do not proceed if the board graph is incomplete or inconsistent.

Expected output:
- Files changed.
- Prototype behavior.
- Board validation covered.
- Move/capture rules covered.
- Manual test steps.
- Checks run or skipped.
- Remaining risks.
- Next recommended improvement.
```

## Prompt SG6: Prototype Rule and Quality Review

Use this after the first playable prototype exists.

```text
You are reviewing the first playable prototype of my original Sholo Guti game.

Inspect the repository and prototype implementation. Do not edit files.

What I want from you:
1. Review whether the board graph matches the approved specification.
2. Review whether initial bead placement is correct.
3. Review whether legal move generation is correct.
4. Review whether capture logic is correct.
5. Review whether multi-capture behavior matches the approved rule.
6. Review whether win/blocked-move rules are correct.
7. Review whether touch interaction is clear.
8. Review UI polish and readability.
9. Review performance risks.
10. Review code quality risks.
11. Identify the top 3 fixes before adding features.
12. Identify what should not be added yet.
13. Create a small improvement scope.

Rules:
- Do not change code.
- Do not add ads yet.
- Prioritize rule correctness, board clarity, move readability, and feedback before monetization.
- Keep recommendations practical.

Expected output:
- Rule correctness review.
- Board graph review.
- Quality review.
- Top 3 fixes.
- Not-now list.
- Small improvement scope.
```

## Prompt SG7: AI, Hints, Undo, and Progression Plan

Use this after the local two-player prototype is playable and correct.

```text
You are planning AI, hints, undo, settings, match history, and replay value for my original Sholo Guti game.

Do not write code yet.

Use the current prototype and game design. Keep changes small enough for one update.

What I want from you:
1. Define production v1 game modes.
2. Define player vs bot behavior.
3. Define 2-3 possible bot difficulty levels.
4. Define hint behavior.
5. Define undo behavior.
6. Define local match history.
7. Define board and bead theme options.
8. Score each idea by user value, effort, risk, monetization fit, and policy risk.
9. Recommend only the best next additions.
10. Define implementation order.

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
- Optional feature score table.
- Recommended next additions.
- Implementation order.
```

## Prompt SG8: Monetization and Analytics Plan

Use this only after the move/capture engine is correct and the game loop is stable.

```text
You are planning user-friendly monetization and analytics for my original Sholo Guti game.

Do not write code yet.

What I want from you:
1. Decide whether the game is ready for ads.
2. Define whether banner ads are appropriate.
3. Define whether interstitial ads are appropriate.
4. Define rewarded ad opportunities, if any.
5. Define frequency caps.
6. Define where ads must never appear.
7. Define analytics events needed to measure match starts, match finishes, move counts, captures, undo usage, hint usage, bot difficulty, session length, retention, and ad impact.
8. Define Play policy and invalid traffic risks.
9. Create a safe implementation scope.

Rules:
- User experience comes before revenue.
- Policy compliance comes before revenue.
- Do not show ads during active turn selection.
- Do not show ads during move or capture animation.
- Do not show ads during mandatory multi-capture chains.
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

## Prompt SG9: Store Listing and Creative Asset Plan

Use this when the game has enough real visuals for store assets.

```text
You are planning Google Play store listing assets for my original Sholo Guti game.

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
- Do not copy names, visuals, board art, bead designs, UI, screenshots, or branding from other games.
- Do not show unavailable online play, tournaments, ranks, rewards, or features.
- Do not use fake rankings, awards, downloads, reviews, or earnings.
- Keep screenshots based on actual gameplay.
- Make the board and beads easy to inspect in screenshots.

Expected output:
- Store listing copy ideas.
- Screenshot plan.
- Feature graphic brief.
- Icon brief.
- Preview video script.
- Asset checklist.
```

## Prompt SG10: Closed Testing, Release Readiness, and Post-Release Improvement

Use this before Play Store testing or after the first testing cycle.

```text
You are checking release readiness and improvement priorities for my original Flutter Sholo Guti game.

Use the repository, release checklist, tester feedback, analytics, Crashlytics, Android vitals, and AdMob data where available. If external data is missing, mark it as unknown.

What I want from you:
1. Review build and version readiness.
2. Review board graph readiness.
3. Review move/capture rule readiness.
4. Review local two-player and bot readiness.
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
- Block release if board graph, move logic, capture logic, or win logic is not verified.

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
Run Prompt SG1 from `prompts/sholo-guti-game-prompt-process.md`.
```

Then:

```text
Run Prompt SG2 from `prompts/sholo-guti-game-prompt-process.md` using the approved board and rule specification from this task.
```

Then:

```text
Run Prompt SG3 from `prompts/sholo-guti-game-prompt-process.md` using the approved concept from this task.
```

Then:

```text
Run Prompt SG4 from `prompts/sholo-guti-game-prompt-process.md` using the approved game design from this task.
```

Only after approving architecture:

```text
Run Prompt SG5 from `prompts/sholo-guti-game-prompt-process.md` using the approved prototype scope from this task.
```

After the prototype is playable and reviewed:

```text
Run Prompt P1 from `prompts/game-production-ready-prompt-pack.md` for the current repository.
```

## Done Criteria

The game process is working when:

- The board graph is validated.
- The game has an original concept.
- The first prototype is playable.
- Initial placement, normal moves, captures, turn switching, win/loss, and restart work correctly.
- Legal moves and captures are easy to understand.
- Local two-player mode works.
- Player vs bot works for production v1 if approved.
- UI is clear and polished enough for strategy players.
- Ads never interrupt active turns or capture chains.
- Store assets show real gameplay.
- Testing produces a learning note before the next update.
