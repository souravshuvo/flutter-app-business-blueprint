# Arrow Puzzle: Tap Puzzle Games Brief

Use this brief to plan the first MVP of `Arrow Puzzle: Tap Puzzle Games`.

Status: Draft  
Date: 2026-08-02  
Planning source: `templates/app-idea-brief.md`

## Confirmed MVP Decisions

- Valid arrows should slide out of the board with a short animation.
- Invalid taps should shake the tapped tile.
- First prototype should use linear level progression, not a full Level Select screen.
- Visual style should be flat colorful.
- First prototype should use pure Flutter widgets, not Flame.
- Firebase and AdMob should wait until the core puzzle loop is playable.

## Basic Info

Project name: Arrow Puzzle: Tap Puzzle Games

Working name: Arrow Puzzle

Project type: Game

Owner: Shuvo

Date: 2026-08-02

Target first platform: Android / Google Play

Primary goal: Build a small, polished casual puzzle game that can validate the game loop and later support AdMob monetization.

## One-Sentence Idea

This project helps casual puzzle players relax and challenge their brain by tapping arrows in the correct order to clear each puzzle board.

## Assumptions to Confirm

- The first version is a simple offline puzzle game.
- The game uses local level data, not cloud levels.
- The first release focuses on Android only.
- The game should be monetized with AdMob after the core loop is fun.
- The first MVP should avoid login, accounts, cloud sync, and complex economy systems.

## Target User

Who is this for?

- Primary user: Casual mobile puzzle players.
- User skill level: Beginner to intermediate.
- User country or market: Global Android users, with Bangladesh and similar Android-heavy markets included.
- User problem: Wants quick, simple puzzle sessions without complex rules.
- User motivation: Relaxation, brain challenge, level completion, and short-session entertainment.

## Problem or Desire

What problem, need, or desire does this project serve?

- Current pain: Many puzzle games are overloaded with ads, timers, confusing mechanics, or too much visual noise.
- Current workaround: Users play generic tap, sort, parking, or arrow puzzle games.
- Why existing alternatives are not enough: The game can compete by being lighter, clearer, faster, and less annoying.
- Why the user would care now: A clean puzzle game with quick levels is easy to try and replay.

## Product Type

Choose one:

- Game

If game:

- Core loop: Look at the arrow board, choose a tap order, tap arrows to clear pieces, complete the level, then move to the next level.
- Player goal: Clear every arrow from the board without getting stuck.
- Session length: 1-5 minutes.
- Replay reason: More levels, increasing difficulty, hints, daily puzzles, and better completion streaks.

## MVP Scope

Smallest useful first version:

- Must-have feature 1: Core arrow-tapping puzzle board.
- Must-have feature 2: First 10 handcrafted levels for prototype, then 20-30 levels before release.
- Must-have feature 3: Level complete, retry, and next-level flow.

Nice-to-have features for later:

- Later feature 1: Hints with rewarded ads.
- Later feature 2: Daily challenge.
- Later feature 3: Skins, themes, sounds, and haptics.

Out of scope for first release:

- Not now: Login or cloud sync.
- Not now: Multiplayer or leaderboard.
- Not now: Complex level editor.

## First Screens

List the first 3-5 screens.

1. Screen: Home
   Purpose: Start game, continue current level, access settings.
2. Screen: Puzzle Board
   Purpose: Main gameplay screen.
3. Screen: Level Complete
   Purpose: Reward completion and move to next level.
4. Screen: Settings
   Purpose: Sound, haptic, privacy, and basic controls.

Later screen:

- Level Select: Add after the core loop is proven.

## Main User Flow

Describe the main flow from app open to first success.

```text
Open app
-> Tap Play
-> Load first puzzle board
-> Tap arrows in a valid order
-> Clear board
-> See Level Complete
-> Tap Next Level
```

## Data Plan

What data does the project need?

- Local data: Current level, unlocked levels, settings, basic progress.
- Cloud data: None for MVP.
- User-generated data: None for MVP.
- Sensitive data: None expected.
- Login required: No.
- Data deletion required: Not required for local-only MVP, but clear progress can be added later.

## Firebase Plan

Needed for MVP:

- Analytics: Yes, for production MVP if release is planned.
- Crashlytics: Yes, for production MVP.
- Remote Config: Later.
- Auth: No.
- Firestore or Realtime Database: No.
- Storage: No.
- Cloud Functions: No.

Notes:

- Console setup needed: Firebase project, Android app, Analytics, Crashlytics.
- Events to track: first_open, level_start, level_complete, level_fail, hint_used, retry_level.
- Error monitoring needs: startup crash, board generation failure, level load failure.

## Monetization Plan

First release monetization:

- AdMob

If using ads:

- Banner placement: Optional bottom banner on Home or Level Select only, not on the gameplay board for MVP.
- Interstitial placement: After every 3-5 completed levels, only after the Level Complete screen.
- Rewarded ad reward: Hint, extra undo, or skip stuck level.
- App-open ad use: Defer until retention and UX are understood.
- Native ad placement: Defer.
- Frequency limits: Interstitial cooldown and max per session required.
- Test ad plan: Use test ads during development and QA.

Why monetization fits the user journey:

Rewarded hints fit naturally because players may get stuck and can choose to watch an ad for help. Interstitial ads should be limited and only appear after level completion so they do not interrupt thinking.

## Analytics Plan

Key success metric: Level completion rate and day-1 retention.

Events to track:

- First open: `first_open`
- Main action: `arrow_tapped`
- Completion or success: `level_complete`
- Retention signal: `session_start`, `level_start`
- Monetization signal: `rewarded_hint_started`, `rewarded_hint_completed`, `interstitial_shown`
- Error signal: `level_load_error`, Crashlytics errors

## Technical Plan

Project base:

- Starter kit: Later, if available.
- Fresh Flutter project: Yes for MVP prototype.
- Existing app reference: None yet.

Architecture choices:

- Package name: To be decided before Play Console setup.
- Minimum Android version: To be decided based on current Flutter and Play requirements.
- State management: Keep simple for MVP; consider Riverpod or ValueNotifier after prototype review.
- Routing: Simple route structure for Home, Level Select, Game, Complete, Settings.
- Local storage: SharedPreferences or lightweight local storage for progress and settings.
- Services: Level service, progress service, settings service, ad service later, analytics service later.
- Environment configuration: Separate development/test and production ad/Firebase config.

## Testing Plan

What must be tested before release?

- Unit tests: Level validation, move rules, win condition, level unlock logic.
- Widget tests: Board renders, tap updates board, level complete state.
- Manual smoke tests: First install, first level, retry, next level, settings.
- Monetization tests: Rewarded hint flow, interstitial cooldown, ad failure handling.
- Offline tests: Game should work offline except ad loading and analytics.
- Device or emulator targets: Small Android phone, large Android phone, at least one older Android version if available.

## Play Store Plan

- App category: Game / Puzzle.
- Short description draft: Tap arrows, clear puzzles, and relax with quick brain challenges.
- Full description draft: To be written after MVP gameplay is stable.
- Screenshot plan: Home, puzzle board, level complete, level select, theme/settings if polished.
- Privacy policy needed: Yes if using AdMob, Firebase Analytics, or Crashlytics.
- Data safety concerns: Ads, analytics, crash diagnostics.
- Content rating concerns: Low risk if no violence, UGC, gambling, or sensitive content.
- Ads disclosure: Required if AdMob is included.
- Closed testing plan: Required or recommended before production, depending on account requirements.

## Risks

Biggest risks:

- Product risk: Generic puzzle concept may not stand out.
- Technical risk: Puzzle rules and level generation may become harder than expected.
- Monetization risk: Too many ads can hurt retention and ratings.
- Policy risk: Data safety and ads disclosure must match SDK behavior.
- Scope risk: Adding themes, daily puzzles, generated levels, and monetization too early.

What can be cut if the project becomes too large?

- Cut option 1: Generated levels; use handcrafted levels first.
- Cut option 2: Level select; use simple linear progression first.
- Cut option 3: Ads; ship first test build without monetization.

## First Codex Task

What should Codex do first?

Goal: Create a technical design note for the core arrow puzzle mechanic before writing Flutter code.

Files or folders to inspect:

- `examples/app-briefs/arrow-puzzle-tap-puzzle-games-brief.md`
- `checklists/new-app-checklist.md`
- `game_framework/README.md`
- `starter_kit/README.md`

Expected output:

- Clear board rules.
- Arrow movement or blocking rules.
- Level data model.
- Win and stuck conditions.
- First 10 sample levels.
- Recommended Flutter project structure.
- First prototype implementation prompt.

Do not change:

- Do not create the Flutter app yet.
- Do not add Firebase yet.
- Do not add AdMob yet.

Verification:

- Rules can be explained simply.
- A level can be represented as data.
- The first 10 levels are playable on paper.
- First prototype scope avoids Firebase and AdMob.

Human review needed:

- Confirm exact puzzle rules.
- Confirm whether the 10 sample levels feel good after prototype testing.

## Start Decision

Choose one:

- Start planning

Reason:

The idea is clear enough to continue planning, but the exact puzzle rules must be defined before implementation. The first task should be a game mechanic design note, not Flutter code.

## Done Criteria

This brief is ready when:

- The idea is clear in one sentence.
- The target user is specific.
- The MVP is small.
- The first screens are known.
- Data, Firebase, monetization, testing, and Play Store needs are considered.
- Risks are written down.
- The first Codex task is specific.
