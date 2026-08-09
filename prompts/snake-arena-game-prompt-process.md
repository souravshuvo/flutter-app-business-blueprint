# Snake Arena Game Prompt Process

Use this prompt process to plan and build an original snake or worm arena game inspired by classic snake growth mechanics.

The goal is not to copy WormZone.io, Hungry Snake, Slither.io, or any other existing game. The goal is to create a small, original, finishable Flutter game with its own theme, visuals, progression, and monetization.

## Purpose

Guide a snake arena game from rough idea to first playable prototype, then toward bots, power-ups, monetization, store assets, testing, and release.

This process is designed for a solo Flutter developer. It favors a fun core loop before skins, leaderboard, online multiplayer, complex economies, or heavy backend systems.

## When to Use

Use this process when:

- You want to create a new snake, worm, or arena growth game.
- You want a game similar in broad genre to worm/snake arena games but legally and creatively original.
- You want to build a small MVP first.
- You want Codex to help with planning, architecture, prototype, review, monetization, and release.

Do not use this process to clone another game's name, UI, art, maps, assets, monetization tricks, or exact mechanics.

## Core Rules

- Do not copy existing game names, art, UI, icons, screenshots, maps, music, characters, or branding.
- Do not present the game as affiliated with WormZone.io, Hungry Snake, Slither.io, or any other game.
- Keep version 1 offline unless online multiplayer is explicitly approved later.
- Build the core loop before skins, leaderboard, login, cloud sync, battle pass, or complex shop systems.
- Prefer simple, responsive controls.
- Prefer offline arena plus bots for MVP.
- Do not add ads during active gameplay.
- Prefer rewarded ads for optional value.
- Use interstitials only at natural transitions, with frequency caps.
- Keep the first prototype small enough to finish and test.

## Recommended Flow

1. Prompt G1: Original game concept and MVP plan.
2. Prompt G2: Game design document.
3. Prompt G3: Flutter technical architecture.
4. Prompt G4: First playable prototype.
5. Prompt G5: Prototype fun and quality review.
6. Prompt G6: Bots, power-ups, and progression plan.
7. Prompt G7: Monetization and analytics plan.
8. Prompt G8: Store listing and creative asset plan.
9. Prompt G9: Closed testing and release readiness.
10. Prompt G10: Post-release improvement plan.

## Production V1 Requirement

Do not publish after only the first playable prototype. For a release-ready version 1, use `prompts/game-production-ready-prompt-pack.md` after the prototype review.

Production v1 should include polished UI, stable offline bot gameplay, enough content, production-safe AdMob, analytics, truthful store assets, and release QA.

Suggested content target: one polished arena plus 20-30 missions, objectives, bot difficulty milestones, or equivalent replayable goals.

Run production prompts in this order:

1. `P1` production scope lock.
2. `P2` UI and gameplay polish.
3. `P3` content and mission implementation.
4. `P4` AdMob and analytics implementation.
5. `P5` store assets and listing production.
6. `P6` production release readiness.

## Prompt G1: Original Game Concept and MVP Plan

Use this before writing code.

```text
You are helping me plan an original Flutter snake arena game inspired by classic snake growth mechanics.

Do not write code yet.

The game should be original. Do not copy names, art, UI, assets, exact branding, exact maps, or exact progression from WormZone.io, Hungry Snake, Slither.io, or any other existing game.

What I want from you:
1. Define the core game idea in one sentence.
2. Define the target player.
3. Define the core loop.
4. Define what makes this game different.
5. Define the smallest playable MVP.
6. Define the first screen flow.
7. Define controls.
8. Define food, growth, scoring, collision, and death rules.
9. Define enemy or bot behavior for MVP.
10. Define 3 possible themes and recommend one.
11. Define what should not be built in version 1.
12. Define a user-friendly monetization direction.
13. Define the first prototype task.

Rules:
- Keep MVP small enough for a solo developer.
- Prefer one game mode for version 1.
- Prefer offline bots instead of online multiplayer.
- Do not add ads before the core loop is fun.
- Do not add skins, shop, leaderboard, login, or cloud sync unless they are clearly needed later.

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

## Prompt G2: Game Design Document

Use this after the concept is clear.

```text
You are creating a game design document for my original Flutter snake arena MVP.

Do not write code yet.

Use the approved concept from this task. If no concept exists, create a small original concept first and ask me to approve it before continuing.

What I want from you:
1. Game summary.
2. Core loop.
3. Session length target.
4. Win, lose, and restart conditions.
5. Movement and control rules.
6. Food spawn rules.
7. Growth and scoring rules.
8. Collision rules.
9. Enemy or bot rules.
10. Power-up rules, if any.
11. Arena design.
12. UI screens and HUD.
13. Sound and visual feedback.
14. Difficulty progression.
15. Analytics events.
16. Ad placement rules for later.
17. Done criteria for the first playable prototype.

Rules:
- Keep version 1 simple.
- Avoid online multiplayer in MVP.
- Avoid complex economy, shop, skins, and login in MVP.
- Make rules precise enough for implementation.
- Keep monetization out of active gameplay.

Expected output:
- Complete MVP game design document.
- Rule tables where useful.
- Prototype done criteria.
- Risks and open questions.
```

## Prompt G3: Flutter Technical Architecture

Use this before implementation.

```text
You are designing the Flutter technical architecture for my original snake arena game.

Use Flame if it is the best fit for game loop, rendering, movement, collision, and entity management. If plain Flutter is better for this scope, explain why.

Do not write code yet.

What I want from you:
1. Recommend Flame or plain Flutter.
2. Define folder structure.
3. Define game loop architecture.
4. Define entity model: player, enemy, food, power-up, arena.
5. Define movement and input handling.
6. Define collision system.
7. Define spawn system.
8. Define scoring and growth state.
9. Define local save data.
10. Define settings and pause behavior.
11. Define analytics event names.
12. Define future AdMob integration points.
13. Define test strategy.
14. Define the first implementation slice.

Rules:
- Follow the existing project architecture if this is inside an existing repo.
- Keep the first implementation slice small.
- Do not add Firebase, AdMob, leaderboard, or purchases yet unless explicitly approved.
- Avoid overengineering.

Expected output:
- Architecture decision.
- Folder structure.
- Main classes or components.
- Data flow.
- First implementation slice.
- Test plan.
```

## Prompt G4: First Playable Prototype

Use this to implement the first playable version.

```text
You are implementing the first playable prototype of my original Flutter snake arena game.

Use the approved game design and technical architecture from this task. If no approved scope exists, create a small prototype scope and ask me to approve it before editing.

Scope:
- One arena.
- One controllable snake or worm.
- Food spawning.
- Growth.
- Score.
- Collision with boundary or self, depending on approved rules.
- Game over.
- Restart.
- Basic HUD.
- No ads.
- No skins.
- No leaderboard.
- No online multiplayer.

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
- Do not copy assets or UI from existing games.
- If using placeholder visuals, label them as placeholders.

Expected output:
- Files changed.
- Prototype behavior.
- Manual test steps.
- Checks run or skipped.
- Remaining risks.
- Next recommended improvement.
```

## Prompt G5: Prototype Fun and Quality Review

Use this after the first playable prototype exists.

```text
You are reviewing the first playable prototype of my original snake arena game.

Inspect the repository and prototype implementation. Do not edit files.

What I want from you:
1. Review whether movement feels likely to be fun.
2. Review whether collision rules are fair.
3. Review whether scoring and growth are understandable.
4. Review whether session length is likely too short, too long, or okay.
5. Review performance risks.
6. Review code quality risks.
7. Identify the top 3 fixes before adding features.
8. Identify what should not be added yet.
9. Create a small improvement scope.

Rules:
- Do not change code.
- Do not add ads yet.
- Prioritize fun and fairness before monetization.
- Keep recommendations practical.

Expected output:
- Fun review.
- Quality review.
- Top 3 fixes.
- Not-now list.
- Small improvement scope.
```

## Prompt G6: Bots, Power-Ups, and Progression Plan

Use this after the core prototype is playable.

```text
You are planning bots, power-ups, and progression for my original snake arena game.

Do not write code yet.

Use the current prototype and game design. Keep changes small enough for one update.

What I want from you:
1. Define simple bot behavior for MVP.
2. Define how bots spawn, move, eat, grow, and collide.
3. Define 3-5 power-up ideas.
4. Score each power-up by fun, complexity, balance risk, and visual clarity.
5. Recommend only 1-2 power-ups for the next update.
6. Define difficulty progression.
7. Define session reward loop.
8. Define implementation order.

Rules:
- Prefer simple bots over online multiplayer.
- Do not add too many power-ups at once.
- Keep difficulty fair.
- Do not add monetization until the gameplay loop is stable.

Expected output:
- Bot behavior plan.
- Power-up table.
- Recommended next features.
- Difficulty progression.
- Implementation order.
```

## Prompt G7: Monetization and Analytics Plan

Use this only after the game loop is fun enough.

```text
You are planning user-friendly monetization and analytics for my original snake arena game.

Do not write code yet.

What I want from you:
1. Decide whether the game is ready for ads.
2. Define rewarded ad opportunities.
3. Define whether interstitial ads are appropriate.
4. Define frequency caps.
5. Define where ads must never appear.
6. Define analytics events needed to measure fun, retention, and ad impact.
7. Define policy risks.
8. Create a safe implementation scope.

Rules:
- User experience comes before revenue.
- Policy compliance comes before revenue.
- Do not show ads during active gameplay.
- Do not encourage ad clicks.
- Do not reward ad clicks.
- Prefer rewarded ads for optional value.
- Use interstitials only at natural game-over or session transition points.
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

## Prompt G8: Store Listing and Creative Asset Plan

Use this when the game has enough real visuals for store assets.

```text
You are planning Google Play store listing assets for my original snake arena game.

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
- Do not copy names, visuals, or branding from other games.
- Do not claim multiplayer if the game is offline bots only.
- Do not show unavailable skins, power-ups, arenas, or rewards.
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

## Prompt G9: Closed Testing and Release Readiness

Use this before Play Store testing or release.

```text
You are checking closed testing and release readiness for my original Flutter snake arena game.

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

## Prompt G10: Post-Release Improvement Plan

Use this after testing or release.

```text
You are helping me improve my original snake arena game after testing or release.

Use available tester feedback, reviews, analytics, Crashlytics, Android vitals, and AdMob data. If external data is missing, mark it as unknown.

What I want from you:
1. Summarize release health.
2. Identify gameplay issues.
3. Identify crash or performance issues.
4. Identify ad experience issues.
5. Identify retention issues.
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
Run Prompt G1 from `prompts/snake-arena-game-prompt-process.md`.
```

Then:

```text
Run Prompt G2 from `prompts/snake-arena-game-prompt-process.md` using the approved concept from this task.
```

Then:

```text
Run Prompt G3 from `prompts/snake-arena-game-prompt-process.md` using the approved game design from this task.
```

Only after approving architecture:

```text
Run Prompt G4 from `prompts/snake-arena-game-prompt-process.md` using the approved prototype scope from this task.
```

## Done Criteria

The game process is working when:

- The game has an original concept.
- The first prototype is playable.
- Movement and collision feel fair.
- The core loop is fun before ads are added.
- Bots and power-ups are added gradually.
- Ads never interrupt active gameplay.
- Store assets show real gameplay.
- Testing produces a learning note before the next update.
