# Emoji Chor-Police Game Prompt Process

Use this prompt process to plan and build an original emoji-themed Chor-Police game for Flutter.

The game is based on the classic Raja, Mantri, Chor, Police party game. The goal is to make a vibrant, lighthearted mobile version with secret roles, bluffing, guessing, scoring, pass-and-play privacy, simple AI, polished emoji visuals, and production-safe monetization.

## Purpose

Guide Emoji Chor-Police from concept to first playable prototype, then toward single-player AI, pass-and-play, scoring history, polish, monetization, store assets, testing, and release.

This process is designed for a solo Flutter developer. It favors a small, polished, offline game before adding online multiplayer, accounts, cloud sync, complex avatars, tournaments, or live events.

## When to Use

Use this process when:

- You want to create a Chor-Police, Raja-Mantri-Chor-Police, hidden-role, or local party guessing game.
- You want an offline casual game that can be finished and released.
- You want Codex to help with planning, architecture, prototype, review, monetization, and release.
- You want the game to become a polished Play Store product, not only a prototype.

Do not use this process to copy another game's name, UI, art, card designs, animations, sounds, monetization tricks, store assets, or branding.

## Core Role Theme

Default version 1 role set:

| Role | Emoji | Default Points | Theme |
| --- | --- | ---: | --- |
| King / Raja | 👑 | 1000 | Gold / yellow |
| Minister / Mantri | 🧙‍♂️ | 800 | Purple / blue |
| Police | 👮‍♂️ | 500 if correct | Dark blue |
| Thief / Chor | 🥷 | 0 if caught, 500 if Police is wrong | Dark red / black |
| Secret card | 🎴 or ❓ | - | Neutral gray |

Default scoring assumption:

- King gets 1000 points each round.
- Minister gets 800 points each round.
- Police gets 500 points only when the Thief is guessed correctly.
- Thief gets 0 points when caught.
- If Police guesses wrong, Police gets 0 and Thief gets 500.

If the preferred local rule is different, Codex should identify the difference before implementation and ask for approval.

## Core Rules

- Keep version 1 offline.
- Build role shuffle, role assignment, Police reveal, accusation, round reveal, score update, next round, and final result before online play, tournaments, login, or cloud sync.
- Single player should support one human vs 3 AI bots.
- Pass-and-play should support 4 local players on one phone.
- In pass-and-play, each player must privately reveal their role using a deliberate hold-to-reveal or tap-and-hide flow.
- The game must prevent accidental role leaks during pass-and-play.
- AI Police should use simple, fair guessing logic with configurable difficulty only if approved.
- Do not show ads during role reveal, Police accusation, or round reveal.
- Prefer interstitial ads only after round summary, match end, or clear session breaks, with frequency caps.
- Prefer rewarded ads only for optional cosmetic emoji themes, harmless extra challenge modes, or non-competitive bonuses.
- Keep the first prototype small enough to finish and test.

## Recommended Flow

1. Prompt ECP1: Original game concept and MVP plan.
2. Prompt ECP2: Game design document.
3. Prompt ECP3: Flutter technical architecture.
4. Prompt ECP4: First playable prototype.
5. Prompt ECP5: Prototype fun and quality review.
6. Prompt ECP6: Modes, bots, scoring, and progression plan.
7. Prompt ECP7: Monetization and analytics plan.
8. Prompt ECP8: Store listing and creative asset plan.
9. Prompt ECP9: Closed testing and release readiness.
10. Prompt ECP10: Post-release improvement plan.

## Production V1 Requirement

Do not publish after only the first playable prototype. For a release-ready version 1, use `prompts/game-production-ready-prompt-pack.md` after the prototype review.

Production v1 should include polished emoji UI, correct role/scoring logic, single-player vs 3 AI bots, 4-player pass-and-play, score history, production-safe AdMob, analytics, truthful store assets, and release QA.

Suggested content target: single-player mode, pass-and-play mode, 5-10 round match presets, local score history, simple AI Police logic, and 20-30 achievements or challenge goals.

Run production prompts in this order:

1. `P1` production scope lock.
2. `P2` UI and gameplay polish.
3. `P3` modes, bots, scoring, and content implementation.
4. `P4` AdMob and analytics implementation.
5. `P5` store assets and listing production.
6. `P6` production release readiness.

## Prompt ECP1: Original Game Concept and MVP Plan

Use this before writing code.

```text
You are helping me plan an original Flutter emoji-themed Chor-Police game based on Raja, Mantri, Chor, Police.

Do not write code yet.

The game should be original. Do not copy names, art, UI, card designs, sounds, animations, monetization, or store assets from any existing Chor-Police, hidden-role, or party game.

Use this default role theme:
- King / Raja: 👑, 1000 points.
- Minister / Mantri: 🧙‍♂️, 800 points.
- Police: 👮‍♂️, 500 points if the Thief is guessed correctly.
- Thief / Chor: 🥷, 0 points if caught, 500 points if Police guesses wrong.
- Secret card: 🎴 or ❓.

What I want from you:
1. Define the core game idea in one sentence.
2. Define the target player.
3. Define the nostalgic hook.
4. Define the core loop.
5. Define what makes this emoji version different.
6. Define the smallest playable MVP.
7. Define the first screen flow.
8. Define single-player rules.
9. Define pass-and-play rules.
10. Define role assignment, Police reveal, accusation, reveal, and scoring rules.
11. Define basic AI behavior.
12. Define 3 possible visual themes and recommend one.
13. Define what should not be built in version 1.
14. Define a user-friendly monetization direction.
15. Define the first prototype task.

Rules:
- Keep MVP small enough for a solo developer.
- Prefer offline single-player and pass-and-play before online multiplayer.
- Do not add ads before the role logic and scoring are correct.
- Do not add login, cloud sync, online multiplayer, chat, complex avatars, tournaments, betting-like mechanics, or live events.
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
- AI behavior.
- Theme recommendation.
- Not-now list.
- Monetization direction.
- First prototype task.
```

## Prompt ECP2: Game Design Document

Use this after the concept is clear.

```text
You are creating a game design document for my original Flutter Emoji Chor-Police MVP.

Do not write code yet.

Use the approved concept from this task. If no concept exists, create a small original concept first and ask me to approve it before continuing.

What I want from you:
1. Game summary.
2. Core loop.
3. Session length target.
4. MVP game modes.
5. Role table with emoji, points, color theme, and behavior.
6. Shuffle and card assignment rules.
7. Single-player round flow.
8. Pass-and-play privacy flow.
9. Police reveal rules.
10. Accusation rules.
11. Correct and wrong guess scoring rules.
12. Round summary and match summary.
13. Score history rules.
14. UI screens and HUD.
15. Sound, haptics, and visual feedback.
16. Analytics events.
17. Ad placement rules for later.
18. Done criteria for the first playable prototype.

Rules:
- Make role and scoring rules precise enough for implementation.
- Keep version 1 simple.
- Avoid online multiplayer, chat, login, cloud sync, tournaments, and complex cosmetics in MVP.
- Keep monetization out of active role reveal and accusation moments.
- Pass-and-play privacy must be treated as a core requirement.

Expected output:
- Complete MVP game design document.
- Role and scoring table.
- Screen flow.
- Prototype done criteria.
- Risks and open questions.
```

## Prompt ECP3: Flutter Technical Architecture

Use this before implementation.

```text
You are designing the Flutter technical architecture for my original Emoji Chor-Police game.

Use plain Flutter unless a game library is clearly justified. This game should usually work well with Flutter widgets, animations, state management, and pure Dart game logic.

Do not write code yet.

What I want from you:
1. Recommend plain Flutter or a game library.
2. Define folder structure.
3. Define domain model: role, player, bot, round, match, accusation, score, mode, result.
4. Define role shuffle and assignment logic.
5. Define single-player AI flow.
6. Define pass-and-play private reveal flow.
7. Define match controller flow.
8. Define local save data for settings, match presets, and score history if included.
9. Define UI screens.
10. Define animation approach for shuffle, card flip, reveal, and result.
11. Define analytics event names.
12. Define future AdMob integration points.
13. Define test strategy.
14. Define the first implementation slice.

Rules:
- Follow the existing project architecture if this is inside an existing repo.
- Keep role/scoring rules in pure Dart where practical.
- Keep UI separate from game rules.
- Do not add Firebase, AdMob, purchases, online play, chat, cloud sync, or complex cosmetics yet unless explicitly approved.
- Avoid overengineering.

Expected output:
- Architecture decision.
- Folder structure.
- Main classes or components.
- Match state flow.
- Private reveal flow.
- Data flow.
- First implementation slice.
- Test plan.
```

## Prompt ECP4: First Playable Prototype

Use this to implement the first playable version.

```text
You are implementing the first playable prototype of my original Flutter Emoji Chor-Police game.

Use the approved game design and technical architecture from this task. If no approved scope exists, create a small prototype scope and ask me to approve it before editing.

Scope:
- Main menu.
- Single-player mode with 1 human and 3 AI bots.
- 4-player pass-and-play mode if small enough.
- Role shuffle animation or simple shuffle state.
- Secret role assignment.
- Private role reveal for pass-and-play.
- Police reveal.
- Police accusation.
- Round reveal.
- Score update.
- Next round.
- Match summary.
- No ads.
- No online play.
- No chat.
- No shop.

What I want from you:
1. Inspect the repository first.
2. Implement only the first playable prototype.
3. Keep code small and reviewable.
4. Follow existing project patterns.
5. Add unit tests for role assignment and scoring rules where practical.
6. Use lightweight verification unless a build is essential.
7. Explain how to run and manually test the prototype.

Rules:
- Do not add monetization yet.
- Do not add unrelated features.
- Do not introduce large dependencies unless approved.
- Do not copy UI, sounds, card designs, icons, or assets from existing games.
- If using placeholder visuals, label them as placeholders.
- Pass-and-play must not reveal all roles at once.

Expected output:
- Files changed.
- Prototype behavior.
- Scoring rules covered.
- Manual test steps.
- Checks run or skipped.
- Remaining risks.
- Next recommended improvement.
```

## Prompt ECP5: Prototype Fun and Quality Review

Use this after the first playable prototype exists.

```text
You are reviewing the first playable prototype of my original Emoji Chor-Police game.

Inspect the repository and prototype implementation. Do not edit files.

What I want from you:
1. Review whether the role reveal flow feels clear and fun.
2. Review whether pass-and-play privacy is safe.
3. Review whether scoring rules are correct.
4. Review whether AI Police behavior is understandable and fair.
5. Review whether round and match summaries are clear.
6. Review UI polish and readability.
7. Review animation and feedback quality.
8. Review performance risks.
9. Review code quality risks.
10. Identify the top 3 fixes before adding features.
11. Identify what should not be added yet.
12. Create a small improvement scope.

Rules:
- Do not change code.
- Do not add ads yet.
- Prioritize rule correctness, privacy, readability, and feedback before monetization.
- Keep recommendations practical.

Expected output:
- Fun review.
- Rule correctness review.
- Privacy review.
- Quality review.
- Top 3 fixes.
- Not-now list.
- Small improvement scope.
```

## Prompt ECP6: Modes, Bots, Scoring, and Progression Plan

Use this after the core prototype is playable.

```text
You are planning modes, bot behavior, scoring history, achievements, and replay value for my original Emoji Chor-Police game.

Do not write code yet.

Use the current prototype and game design. Keep changes small enough for one update.

What I want from you:
1. Define production v1 game modes.
2. Define 5-10 round match presets.
3. Define single-player AI behavior options.
4. Define pass-and-play improvements.
5. Define local score history.
6. Define 20-30 achievements or challenge goals.
7. Define optional emoji theme ideas.
8. Score each idea by user value, effort, risk, monetization fit, and policy risk.
9. Recommend only the best next additions.
10. Define implementation order.

Rules:
- Prefer replayable offline modes over online multiplayer.
- Do not add chat, accounts, live events, cloud sync, or tournaments in early versions.
- Do not create features only to force more ad impressions.
- Keep achievements family-friendly and simple.
- Keep AI transparent enough that users do not feel cheated.

Expected output:
- Mode plan.
- Bot behavior plan.
- Challenge/achievement list.
- Optional feature score table.
- Recommended next additions.
- Implementation order.
```

## Prompt ECP7: Monetization and Analytics Plan

Use this only after the game loop is fun enough and scoring is stable.

```text
You are planning user-friendly monetization and analytics for my original Emoji Chor-Police game.

Do not write code yet.

What I want from you:
1. Decide whether the game is ready for ads.
2. Define whether banner ads are appropriate.
3. Define whether interstitial ads are appropriate.
4. Define rewarded ad opportunities, if any.
5. Define frequency caps.
6. Define where ads must never appear.
7. Define analytics events needed to measure mode starts, round finishes, Police accuracy, AI outcomes, pass-and-play completion, session length, retention, and ad impact.
8. Define Play policy and invalid traffic risks.
9. Create a safe implementation scope.

Rules:
- User experience comes before revenue.
- Policy compliance comes before revenue.
- Do not show ads during private role reveal.
- Do not show ads during Police accusation.
- Do not show ads during round reveal animation.
- Do not encourage ad clicks.
- Do not reward ad clicks.
- Use interstitials only after round summary, match end, or clear session breaks.
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

## Prompt ECP8: Store Listing and Creative Asset Plan

Use this when the game has enough real visuals for store assets.

```text
You are planning Google Play store listing assets for my original Emoji Chor-Police game.

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
- Do not copy names, visuals, card designs, characters, UI, screenshots, or branding from other games.
- Do not show unavailable online play, tournaments, teams, rewards, avatars, or features.
- Do not use fake rankings, awards, downloads, reviews, or earnings.
- Keep screenshots based on actual gameplay.
- Keep emoji usage clear and family-friendly.

Expected output:
- Store listing copy ideas.
- Screenshot plan.
- Feature graphic brief.
- Icon brief.
- Preview video script.
- Asset checklist.
```

## Prompt ECP9: Closed Testing and Release Readiness

Use this before Play Store testing or release.

```text
You are checking closed testing and release readiness for my original Flutter Emoji Chor-Police game.

Use the repository and release checklist. Do not publish anything.

What I want from you:
1. Review build and version readiness.
2. Review role and scoring readiness.
3. Review single-player and pass-and-play readiness.
4. Review privacy flow readiness for pass-and-play.
5. Review crash and performance risks.
6. Review ads and analytics readiness.
7. Review permissions and privacy risk.
8. Review Data safety impact.
9. Review store listing readiness.
10. Create a manual QA checklist.
11. Recommend internal test, closed test, delay, or release.

Rules:
- Do not claim release readiness if checks were not run.
- Keep unknowns clear.
- Prefer internal or closed testing if risk is unclear.
- Do not run heavy build/install/emulator unless explicitly approved.
- Block release if pass-and-play can accidentally reveal hidden roles.

Expected output:
- Release readiness summary.
- Blockers.
- Manual QA checklist.
- Play Console checklist.
- Recommendation.
```

## Prompt ECP10: Post-Release Improvement Plan

Use this after testing or release.

```text
You are helping me improve my original Emoji Chor-Police game after testing or release.

Use available tester feedback, reviews, analytics, Crashlytics, Android vitals, and AdMob data. If external data is missing, mark it as unknown.

What I want from you:
1. Summarize release health.
2. Identify scoring or rule issues.
3. Identify pass-and-play privacy issues.
4. Identify AI fairness or clarity issues.
5. Identify crash or performance issues.
6. Identify ad experience issues.
7. Identify mode popularity, session length, or retention issues.
8. Recommend the next small update.
9. Identify what should not be built yet.
10. Create a learning note.

Rules:
- Fix rule bugs, privacy problems, crashes, and serious gameplay frustration before adding new features.
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
Run Prompt ECP1 from `prompts/emoji-chor-police-game-prompt-process.md`.
```

Then:

```text
Run Prompt ECP2 from `prompts/emoji-chor-police-game-prompt-process.md` using the approved concept from this task.
```

Then:

```text
Run Prompt ECP3 from `prompts/emoji-chor-police-game-prompt-process.md` using the approved game design from this task.
```

Only after approving architecture:

```text
Run Prompt ECP4 from `prompts/emoji-chor-police-game-prompt-process.md` using the approved prototype scope from this task.
```

After the prototype is playable and reviewed:

```text
Run Prompt P1 from `prompts/game-production-ready-prompt-pack.md` for the current repository.
```

## Done Criteria

The game process is working when:

- The game has an original concept.
- The first prototype is playable.
- Roles are shuffled and assigned correctly.
- Police reveal, accusation, round reveal, scoring, next round, and match summary work.
- Single-player vs 3 AI bots works.
- Pass-and-play protects private roles.
- UI is clear, polished, emoji-themed, and readable.
- Local score history or achievements create replay value.
- Ads never interrupt hidden-role gameplay.
- Store assets show real gameplay.
- Testing produces a learning note before the next update.
