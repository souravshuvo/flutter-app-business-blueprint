# Arrow Puzzle First Prototype Prompt

Use this prompt to create the first playable Flutter prototype for `Arrow Puzzle: Tap Puzzle Games`.

This prompt should be used only after reviewing:

- `examples/app-briefs/arrow-puzzle-tap-puzzle-games-brief.md`
- `game_framework/arrow-puzzle-mechanics.md`

## Purpose

Build the smallest playable Flutter prototype that proves the core puzzle loop.

The prototype should focus on gameplay, not monetization, Firebase, store listing, or long-term polish.

## When to Use

Use this prompt when ready to create or update the first Flutter implementation for Arrow Puzzle.

Do not use this prompt to add:

- Firebase
- AdMob
- Play Store setup
- Daily challenge
- Generated levels
- Level Select
- Cloud sync
- Leaderboards

## Inputs Required

- Target Flutter project location.
- Desired package name.
- Whether to create a fresh Flutter app or use an existing app.
- Preferred state management if already decided.

## Prompt Text

```text
You are helping me build the first playable Flutter prototype for `Arrow Puzzle: Tap Puzzle Games`.

Before coding, inspect these files:

- `examples/app-briefs/arrow-puzzle-tap-puzzle-games-brief.md`
- `game_framework/arrow-puzzle-mechanics.md`
- `AGENTS.md`
- `CONTRIBUTING.md`

Goal:
Create the smallest playable prototype that proves the core puzzle loop.

Confirmed MVP decisions:
- Use pure Flutter widgets, not Flame.
- Use linear level progression.
- Do not build Level Select yet.
- Use flat colorful visual style.
- Valid arrows slide out of the board with a short animation.
- Invalid taps shake only the tapped tile.
- Store progress locally.
- Do not add Firebase yet.
- Do not add AdMob yet.

Build only:
1. Home screen with Play/Continue.
2. Puzzle board screen.
3. Level complete screen.
4. Optional settings screen if simple.
5. First 10 local levels from `game_framework/arrow-puzzle-mechanics.md`.
6. Pure Dart puzzle engine.
7. Local progress.
8. Retry and next level.
9. Unit tests for puzzle engine.

Architecture:
- Keep puzzle rules in pure Dart under a domain layer.
- Keep UI separate from puzzle rules.
- Use a small controller/application layer for current level state.
- Keep the implementation easy to test and change.

Do not:
- Add Firebase.
- Add AdMob.
- Add login.
- Add generated levels.
- Add Level Select.
- Add store listing files.
- Add complex scoring.
- Add hidden symbols, blockers, skins, or themes.

Verification:
- Run formatting.
- Run static analysis.
- Run unit tests.
- Confirm sample levels 1-10 pass solvability validation.
- Confirm valid taps remove arrows.
- Confirm invalid taps do not mutate board state.
- Confirm win condition works.

Expected output:
- Explain the implementation plan.
- Make the smallest focused code changes.
- Report verification results.
- List anything deferred.
```

## Expected Output

Codex should produce:

- A focused implementation plan.
- A playable local prototype.
- Pure Dart engine tests.
- Clear verification results.
- A list of deferred items.

## Review Checklist

Before accepting implementation:

- Core rule matches `game_framework/arrow-puzzle-mechanics.md`.
- Engine is separate from UI.
- First 10 levels are available locally.
- Linear level flow works.
- Valid arrows slide out.
- Invalid taps shake the tapped tile.
- No Firebase was added.
- No AdMob was added.
- Tests cover the puzzle engine.

