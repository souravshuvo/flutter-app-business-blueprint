# Arrow Puzzle Mechanics

Technical design note for `Arrow Puzzle: Tap Puzzle Games`.

Status: Draft  
Date: 2026-08-02  
Related brief: `examples/app-briefs/arrow-puzzle-tap-puzzle-games-brief.md`

## Goal

Define the core puzzle rules before writing Flutter code.

The MVP should prove that the game loop is understandable, relaxing, and testable:

```text
Look at board
-> Find a clear arrow
-> Tap arrow
-> Arrow exits board
-> Repeat until board is clear
-> Complete level
```

## MVP Design Decision

Use pure Flutter widgets for the first prototype.

Reason:

- The game is a grid puzzle, not a physics-heavy action game.
- Flutter widgets are enough for board layout, taps, simple movement, and level UI.
- A pure Dart puzzle engine will be easier to unit test.
- Flame can be considered later if animation, particles, or richer game scenes become important.

## Confirmed MVP Decisions

- Valid arrows slide out of the board with a short animation.
- Invalid taps shake only the tapped tile.
- First prototype uses linear level progression.
- Level Select is deferred until the core loop is proven.
- Visual style is flat colorful.
- Hints are optional and should wait until the core loop feels good.
- Firebase and AdMob are deferred until after the first playable prototype.

## Core Rule

An arrow can be removed when the full path from the arrow to the edge of the board is clear in the arrow's direction.

If another arrow blocks that path, the tap is invalid.

When a valid arrow is tapped:

1. The arrow moves out of the board in its direction.
2. The arrow is removed from the board.
3. The board state updates.
4. The player continues until all arrows are removed.

## Direction Symbols

Use these symbols in level data:

```text
U = arrow points up
D = arrow points down
L = arrow points left
R = arrow points right
. = empty cell
```

Future symbols can be added later:

```text
# = fixed blocker
? = hidden arrow
* = special tile
```

Do not add future symbols in the first prototype.

## Coordinate System

Use zero-based row and column positions.

```text
row 0 = top row
col 0 = left column
```

Example 4x4 board:

```text
row 0: R...
row 1: ....
row 2: ..D.
row 3: ...L
```

Cell `(0, 0)` contains `R`.

## Valid Tap Rules

### Up Arrow

An `U` arrow is valid if every cell above it in the same column is empty.

```text
..U..
.....
```

### Down Arrow

A `D` arrow is valid if every cell below it in the same column is empty.

```text
..D..
.....
```

### Left Arrow

An `L` arrow is valid if every cell to its left in the same row is empty.

```text
...L.
```

### Right Arrow

An `R` arrow is valid if every cell to its right in the same row is empty.

```text
.R...
```

## Invalid Tap Feedback

If the player taps a blocked arrow:

- Do not remove the arrow.
- Play a short blocked animation.
- Optionally use light haptic feedback.
- Optionally highlight the blocking arrow or lane later.

For MVP, shake only the tapped tile.

## Win Condition

The player wins when every arrow has been removed from the board.

```text
all cells == "."
```

After win:

- Show Level Complete screen.
- Save progress.
- Unlock the next level.
- Offer next level.

For MVP, use linear progression:

```text
Level 1 -> Level Complete -> Level 2 -> Level Complete -> Level 3
```

Do not build a full Level Select screen until the core loop is proven.

## Stuck Condition

For MVP, a well-designed level should never become stuck after valid moves because removing arrows only opens more paths.

A level is considered invalid or stuck if:

- Arrows remain on the board.
- No arrow has a clear path to the edge.

This should be caught during level validation before release.

## Level Validation Rule

Before shipping a level, run a solvability check:

1. Copy the board.
2. Find all arrows with clear paths.
3. Remove at least one clear arrow.
4. Repeat until no arrows remain or no clear arrows exist.
5. Level is valid only if all arrows are removed.

Because removing arrows only opens paths, any valid clear arrow can be removed during validation.

## Level Data Model

Recommended MVP data shape:

```text
id: 1
name: First Tap
rows:
  - R...
  - ....
  - ....
  - ...L
```

Rules:

- Every row must have the same length.
- Allowed MVP symbols are `U`, `D`, `L`, `R`, and `.`.
- A level must contain at least one arrow.
- A level must pass solvability validation.
- Start with small boards before adding larger boards.

## Difficulty Progression

Use these knobs to increase difficulty:

- Board size: 3x3, 4x4, 5x5, 6x6.
- Arrow count.
- More arrows blocking each other.
- More mixed directions.
- Fewer immediately available valid arrows.
- Longer dependency chains.
- Optional future blockers.

Do not add timers in MVP. A relaxing puzzle game should first prove the board mechanic.

## Hint Rule

For MVP without monetization:

- Hint highlights one currently valid arrow.

For later rewarded ads:

- Player can watch a rewarded ad to receive one hint.
- Reward must be optional.
- Core gameplay must still work without watching ads.

## Undo Rule

Undo is optional for MVP.

If added:

- Store previous board states in a stack.
- One undo reverses the last valid arrow removal.
- Invalid taps do not create undo states.

## Scoring

Scoring is optional for MVP.

Recommended first release:

- No complex score.
- Track completed levels only.

Future scoring ideas:

- Moves used.
- Hints used.
- Time completed.
- Perfect clear without hint.

## First 10 Sample Levels

Rows are listed from top to bottom.

### Level 1: First Tap

```text
R...
....
....
...L
```

Lesson: Tap arrows with fully open lanes.

### Level 2: Four Directions

```text
.D..
....
...L
..U.
```

Lesson: Learn up, down, left, and right exits.

### Level 3: Free the Lane

```text
..D.
....
..R.
...L
```

Lesson: Remove a blocking arrow to open a vertical lane.

### Level 4: Chain Order

```text
R..D
....
.R..
...L
```

Lesson: Some arrows become valid only after later arrows exit.

### Level 5: Cross Paths

```text
..D.
.R..
....
.U.L
```

Lesson: One row action can open a column action.

### Level 6: Wider Board

```text
.D.R.
.....
.R...
..U.L
.....
```

Lesson: Introduce 5x5 scanning.

### Level 7: Edge Dependency

```text
R...D
.R...
.....
...L.
U....
```

Lesson: Boundary arrows can still be blocked by inner dependencies.

### Level 8: Two-Step Unlock

```text
..D..
.R.R.
.....
.L.U.
.....
```

Lesson: Clear one arrow to unlock another arrow, then unlock a third.

### Level 9: Long Chain

```text
.D..R
.....
.R.D.
.....
U..L.
```

Lesson: Longer dependency chain across rows and columns.

### Level 10: MVP Challenge

```text
R..D..
.R....
..D.L.
......
.U..R.
...L..
```

Lesson: First 6x6 challenge with multiple dependencies.

## Recommended Flutter Structure

Keep the puzzle engine pure Dart and separate from UI.

```text
lib/
|-- main.dart
|-- features/
|   `-- arrow_puzzle/
|       |-- domain/
|       |   |-- arrow_direction.dart
|       |   |-- board_position.dart
|       |   |-- puzzle_cell.dart
|       |   |-- puzzle_level.dart
|       |   `-- puzzle_engine.dart
|       |-- data/
|       |   `-- local_level_pack.dart
|       |-- application/
|       |   `-- puzzle_controller.dart
|       `-- presentation/
|           |-- pages/
|           |   |-- home_page.dart
|           |   |-- level_select_page.dart
|           |   |-- puzzle_page.dart
|           |   |-- level_complete_page.dart
|           |   `-- settings_page.dart
|           `-- widgets/
|               |-- puzzle_board_widget.dart
|               `-- arrow_tile_widget.dart
```

## Engine Responsibilities

`puzzle_engine.dart` should handle:

- Parsing level rows.
- Validating board shape.
- Checking whether a tap is valid.
- Removing a valid arrow.
- Checking win condition.
- Checking stuck condition.
- Returning currently valid moves.

The engine should not depend on Flutter widgets.

## UI Responsibilities

The UI should handle:

- Rendering the board.
- Handling taps.
- Playing animations.
- Showing invalid tap feedback.
- Showing level completion.
- Showing settings.

The UI should not decide puzzle rules.

## Unit Test Targets

Before building more levels, test:

- Level rows must be rectangular.
- Invalid symbols are rejected.
- Empty levels are rejected.
- A clear arrow is valid.
- A blocked arrow is invalid.
- A valid tap removes the arrow.
- An invalid tap does not change the board.
- Win condition is true when board is empty.
- Stuck condition is true when arrows remain but no valid moves exist.
- Sample levels 1-10 pass solvability validation.

## First Prototype Scope

Build only:

- Home screen.
- Puzzle board screen.
- Level complete screen.
- First 10 local levels.
- Local progress.
- Retry and next level.
- Basic sound/haptic toggle if easy.
- Slide-out animation for valid taps.
- Tile shake animation for invalid taps.
- Flat colorful visual style.

Do not build yet:

- Firebase.
- AdMob.
- Store listing.
- Daily challenge.
- Generated levels.
- Themes or skins.
- Leaderboard.
- Cloud sync.
- Level Select.

## Human Review Questions

Confirm before implementation:

- Are the first 10 levels fun enough to continue?
- Are the slide and shake animations readable on a real phone?
- Is the flat colorful style clear enough for small screens?
- Should hints be added after the first playable prototype?
