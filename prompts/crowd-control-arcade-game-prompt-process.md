# Crowd Control Arcade Game Prompt Process

Use this prompt process to plan and build an original crowd-control arcade game for Flutter.

The goal is not to clone Mob Control or any other existing game. The goal is to create a small, original, finishable arcade game based on broad crowd-scaling mechanics: launch units, pass through gates, grow or shrink the crowd, overcome enemy groups, and finish levels.

## Purpose

Guide a crowd-control arcade game from rough idea to first playable prototype, then toward gates, enemies, level design, upgrades, monetization, store assets, testing, and release.

This process is designed for a solo Flutter developer. It favors a satisfying core loop, readable gates, simple unit movement, and small handcrafted levels before complex base-building, live events, online competition, or deep upgrade economies.

## When to Use

Use this process when:

- You want to create a new crowd-control arcade game.
- You want a simple offline level-based game that can be finished and released.
- You want Codex to help with planning, architecture, prototype, review, monetization, and release.
- You want to reuse a disciplined process for hyper-casual or casual arcade games.

Do not use this process to copy another game's name, UI, art, units, gates, level layouts, cannon, base designs, music, monetization tricks, or branding.

## Core Rules

- Do not copy existing game names, art, UI, icons, screenshots, units, gates, cannons, bases, maps, music, characters, or branding.
- Keep version 1 offline.
- Build launch, gate choice, crowd scaling, enemy collision, level win, level lose, and restart before upgrades, base-building, skins, events, or leaderboard.
- Prefer one simple level mode for MVP.
- Keep levels handcrafted or generated from simple original templates.
- Do not add ads during active gameplay.
- Prefer rewarded ads for optional continue, bonus coins, or booster trial.
- Use interstitials only at natural level-end transitions, with frequency caps.
- Keep the first prototype small enough to finish and test.

## Recommended Flow

1. Prompt CC1: Original game concept and MVP plan.
2. Prompt CC2: Game design document.
3. Prompt CC3: Flutter technical architecture.
4. Prompt CC4: First playable prototype.
5. Prompt CC5: Prototype fun and quality review.
6. Prompt CC6: Levels, gates, enemies, and progression plan.
7. Prompt CC7: Monetization and analytics plan.
8. Prompt CC8: Store listing and creative asset plan.
9. Prompt CC9: Closed testing and release readiness.
10. Prompt CC10: Post-release improvement plan.

## Production V1 Requirement

Do not publish after only the first playable prototype. For a release-ready version 1, use `prompts/game-production-ready-prompt-pack.md` after the prototype review.

Production v1 should include polished UI, stable crowd/gate gameplay, enough levels, production-safe AdMob, analytics, truthful store assets, and release QA.

Suggested content target: 30-50 playable levels with readable gate and enemy progression.

Run production prompts in this order:

1. `P1` production scope lock.
2. `P2` UI and gameplay polish.
3. `P3` level implementation.
4. `P4` AdMob and analytics implementation.
5. `P5` store assets and listing production.
6. `P6` production release readiness.

## Prompt CC1: Original Game Concept and MVP Plan

Use this before writing code.

```text
You are helping me plan an original Flutter crowd-control arcade game.

Do not write code yet.

The game should be original. Do not copy names, art, UI, assets, exact branding, units, gates, cannons, bases, levels, upgrades, or progression from Mob Control or any other existing game.

What I want from you:
1. Define the core game idea in one sentence.
2. Define the target player.
3. Define the core loop.
4. Define what makes this game different.
5. Define the smallest playable MVP.
6. Define the first screen flow.
7. Define controls.
8. Define unit launching, gate, crowd scaling, collision, win, and lose rules.
9. Define enemy group or base behavior for MVP.
10. Define 3 possible themes and recommend one.
11. Define what should not be built in version 1.
12. Define a user-friendly monetization direction.
13. Define the first prototype task.

Rules:
- Keep MVP small enough for a solo developer.
- Prefer one game mode for version 1.
- Prefer offline levels.
- Do not add ads before the core loop is fun.
- Do not add base-building, skins, shop, leaderboard, login, cloud sync, or live events unless clearly needed later.

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

## Prompt CC2: Game Design Document

Use this after the concept is clear.

```text
You are creating a game design document for my original Flutter crowd-control arcade MVP.

Do not write code yet.

Use the approved concept from this task. If no concept exists, create a small original concept first and ask me to approve it before continuing.

What I want from you:
1. Game summary.
2. Core loop.
3. Session length target.
4. Level win, lose, and restart conditions.
5. Launching and control rules.
6. Unit movement rules.
7. Gate types and math rules.
8. Crowd scaling rules.
9. Enemy group and base rules.
10. Collision and combat resolution rules.
11. Scoring and reward rules.
12. First 10 level design guidelines.
13. UI screens and HUD.
14. Sound and visual feedback.
15. Difficulty progression.
16. Analytics events.
17. Ad placement rules for later.
18. Done criteria for the first playable prototype.

Rules:
- Keep version 1 simple.
- Avoid complex upgrades, base-building, shop, leaderboard, login, and cloud sync in MVP.
- Make rules precise enough for implementation.
- Keep monetization out of active gameplay.

Expected output:
- Complete MVP game design document.
- Rule tables where useful.
- First 10 level guidelines.
- Prototype done criteria.
- Risks and open questions.
```

## Prompt CC3: Flutter Technical Architecture

Use this before implementation.

```text
You are designing the Flutter technical architecture for my original crowd-control arcade game.

Use Flame if it is the best fit for game loop, rendering, unit movement, collision, gates, crowd simulation, and animations. If plain Flutter is better for this scope, explain why.

Do not write code yet.

What I want from you:
1. Recommend Flame or plain Flutter.
2. Define folder structure.
3. Define game loop architecture.
4. Define entity model: launcher, unit, gate, enemy, base, level, projectile or stream.
5. Define coordinate system and screen scaling.
6. Define input handling.
7. Define unit spawning and movement.
8. Define gate collision and math effects.
9. Define crowd grouping and performance approach.
10. Define enemy collision and combat resolution.
11. Define level data format.
12. Define scoring and level state.
13. Define local save data.
14. Define analytics event names.
15. Define future AdMob integration points.
16. Define test strategy.
17. Define the first implementation slice.

Rules:
- Follow the existing project architecture if this is inside an existing repo.
- Keep the first implementation slice small.
- Do not add Firebase, AdMob, purchases, leaderboard, base-building, or upgrade economy yet unless explicitly approved.
- Avoid overengineering.
- Avoid simulating too many individual units if a grouped approximation is enough for MVP.

Expected output:
- Architecture decision.
- Folder structure.
- Main classes or components.
- Coordinate and collision rules.
- Crowd simulation approach.
- Data flow.
- First implementation slice.
- Test plan.
```

## Prompt CC4: First Playable Prototype

Use this to implement the first playable version.

```text
You are implementing the first playable prototype of my original Flutter crowd-control arcade game.

Use the approved game design and technical architecture from this task. If no approved scope exists, create a small prototype scope and ask me to approve it before editing.

Scope:
- One playable level.
- Simple launcher or spawner.
- Units move forward.
- Two or three gates with basic math effects.
- Crowd size changes after gates.
- One enemy group or enemy base.
- Simple collision or combat resolution.
- Win condition.
- Lose condition.
- Restart.
- Basic HUD.
- No ads.
- No upgrades.
- No shop.
- No base-building.
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
- Do not copy assets, gates, units, cannons, bases, UI, or level layouts from existing games.
- If using placeholder visuals, label them as placeholders.

Expected output:
- Files changed.
- Prototype behavior.
- Manual test steps.
- Checks run or skipped.
- Remaining risks.
- Next recommended improvement.
```

## Prompt CC5: Prototype Fun and Quality Review

Use this after the first playable prototype exists.

```text
You are reviewing the first playable prototype of my original crowd-control arcade game.

Inspect the repository and prototype implementation. Do not edit files.

What I want from you:
1. Review whether launching and movement feel clear.
2. Review whether gate choices are readable and satisfying.
3. Review whether crowd scaling feels understandable.
4. Review whether enemy collision or combat resolution feels fair.
5. Review whether level difficulty is too easy, too hard, or okay.
6. Review performance risks caused by unit count.
7. Review code quality risks.
8. Identify the top 3 fixes before adding features.
9. Identify what should not be added yet.
10. Create a small improvement scope.

Rules:
- Do not change code.
- Do not add ads yet.
- Prioritize readability, control feel, performance, and satisfying feedback before monetization.
- Keep recommendations practical.

Expected output:
- Fun review.
- Quality review.
- Top 3 fixes.
- Not-now list.
- Small improvement scope.
```

## Prompt CC6: Levels, Gates, Enemies, and Progression Plan

Use this after the core prototype is playable.

```text
You are planning levels, gates, enemies, and progression for my original crowd-control arcade game.

Do not write code yet.

Use the current prototype and game design. Keep changes small enough for one update.

What I want from you:
1. Define first 20 level progression.
2. Define level difficulty variables.
3. Define gate types and when they appear.
4. Define enemy types or base variants.
5. Define 3-5 booster or power-up ideas.
6. Score each booster by fun, complexity, balance risk, and monetization risk.
7. Recommend only 1-2 additions for the next update.
8. Define reward loop.
9. Define implementation order.

Rules:
- Prefer simple original levels over complex systems.
- Do not add too many gates, enemies, or boosters at once.
- Keep math readable to players.
- Keep difficulty fair.
- Do not add monetization until the gameplay loop is stable.
- Avoid complex shop or upgrade economy in early versions.

Expected output:
- First 20 level plan.
- Difficulty variables.
- Gate table.
- Enemy table.
- Booster table.
- Recommended next features.
- Reward loop.
- Implementation order.
```

## Prompt CC7: Monetization and Analytics Plan

Use this only after the game loop is fun enough.

```text
You are planning user-friendly monetization and analytics for my original crowd-control arcade game.

Do not write code yet.

What I want from you:
1. Decide whether the game is ready for ads.
2. Define rewarded ad opportunities.
3. Define whether interstitial ads are appropriate.
4. Define frequency caps.
5. Define where ads must never appear.
6. Define analytics events needed to measure level difficulty, retention, and ad impact.
7. Define policy risks.
8. Create a safe implementation scope.

Rules:
- User experience comes before revenue.
- Policy compliance comes before revenue.
- Do not show ads during active gameplay.
- Do not encourage ad clicks.
- Do not reward ad clicks.
- Prefer rewarded ads for optional continue, bonus coins, or booster trials.
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

## Prompt CC8: Store Listing and Creative Asset Plan

Use this when the game has enough real visuals for store assets.

```text
You are planning Google Play store listing assets for my original crowd-control arcade game.

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
- Do not copy names, visuals, units, gates, cannons, bases, maps, or branding from other games.
- Do not show unavailable upgrades, bases, skins, rewards, maps, or modes.
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

## Prompt CC9: Closed Testing and Release Readiness

Use this before Play Store testing or release.

```text
You are checking closed testing and release readiness for my original Flutter crowd-control arcade game.

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

## Prompt CC10: Post-Release Improvement Plan

Use this after testing or release.

```text
You are helping me improve my original crowd-control arcade game after testing or release.

Use available tester feedback, reviews, analytics, Crashlytics, Android vitals, and AdMob data. If external data is missing, mark it as unknown.

What I want from you:
1. Summarize release health.
2. Identify gameplay issues.
3. Identify crash or performance issues.
4. Identify ad experience issues.
5. Identify level difficulty, readability, performance, or retention issues.
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
Run Prompt CC1 from `prompts/crowd-control-arcade-game-prompt-process.md`.
```

Then:

```text
Run Prompt CC2 from `prompts/crowd-control-arcade-game-prompt-process.md` using the approved concept from this task.
```

Then:

```text
Run Prompt CC3 from `prompts/crowd-control-arcade-game-prompt-process.md` using the approved game design from this task.
```

Only after approving architecture:

```text
Run Prompt CC4 from `prompts/crowd-control-arcade-game-prompt-process.md` using the approved prototype scope from this task.
```

## Done Criteria

The game process is working when:

- The game has an original concept.
- The first prototype is playable.
- Launching, gates, crowd scaling, enemy collision, win, lose, and restart work.
- Gate choices feel readable and satisfying.
- Performance remains stable with the target unit count.
- Levels and boosters are added gradually.
- Ads never interrupt active gameplay.
- Store assets show real gameplay.
- Testing produces a learning note before the next update.
