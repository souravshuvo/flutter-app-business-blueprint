# Farming Life Game Prompt Process

Use this prompt process to plan and build an original farming life game for Flutter.

The goal is not to clone FarmVille, Hay Day, Stardew Valley, Township, Harvest Moon, Animal Crossing, or any other existing game. The goal is to create a small, original, finishable farming life game with its own theme, crop loop, progression, visuals, monetization, and store assets.

## Purpose

Guide a farming life game from rough idea to first playable prototype, then toward crops, resources, upgrades, animals or crafting, monetization, store assets, testing, and release.

This process is designed for a solo Flutter developer. It favors a tiny satisfying farm loop before open world exploration, social systems, complex economy, story quests, online trading, live events, or giant content catalogs.

## When to Use

Use this process when:

- You want to create a new farming, garden, homestead, village, or cozy life game.
- You want an offline casual farming game that can be finished and released.
- You want Codex to help with planning, architecture, prototype, review, monetization, and release.
- You want to reuse a disciplined process for simulation or idle-lite games.

Do not use this process to copy another game's name, UI, art, crops, characters, town layout, economy, music, monetization tricks, or branding.

## Core Rules

- Do not copy existing game names, art, UI, icons, screenshots, crops, characters, maps, music, or branding.
- Keep version 1 offline.
- Build plant, water, grow, harvest, sell, upgrade, save, and return loop before animals, crafting, quests, town, social, or live events.
- Prefer one small farm screen for MVP.
- Keep crop and resource systems simple.
- Keep timers short enough for testing and satisfying early play.
- Do not add ads during core tap/harvest interactions.
- Prefer rewarded ads for optional speed-up, bonus coins, or extra seed packs.
- Use interstitials only at natural session transitions, with frequency caps.
- Keep the first prototype small enough to finish and test.

## Recommended Flow

1. Prompt FL1: Original game concept and MVP plan.
2. Prompt FL2: Game design document.
3. Prompt FL3: Flutter technical architecture.
4. Prompt FL4: First playable prototype.
5. Prompt FL5: Prototype fun and quality review.
6. Prompt FL6: Crops, upgrades, animals, and progression plan.
7. Prompt FL7: Monetization and analytics plan.
8. Prompt FL8: Store listing and creative asset plan.
9. Prompt FL9: Closed testing and release readiness.
10. Prompt FL10: Post-release improvement plan.

## Production V1 Requirement

Do not publish after only the first playable prototype. For a release-ready version 1, use `prompts/game-production-ready-prompt-pack.md` after the prototype review.

Production v1 should include polished UI, reliable save/restore, enough farming progression, production-safe AdMob, analytics, truthful store assets, and release QA.

Suggested content target: 30 progression steps, 6-10 crops, one meaningful upgrade path, and stable save/restore.

Run production prompts in this order:

1. `P1` production scope lock.
2. `P2` UI and gameplay polish.
3. `P3` crop/progression implementation.
4. `P4` AdMob and analytics implementation.
5. `P5` store assets and listing production.
6. `P6` production release readiness.

## Prompt FL1: Original Game Concept and MVP Plan

Use this before writing code.

```text
You are helping me plan an original Flutter farming life game.

Do not write code yet.

The game should be original. Do not copy names, art, UI, assets, exact branding, crops, characters, map layouts, economy, quests, or progression from FarmVille, Hay Day, Stardew Valley, Township, Harvest Moon, Animal Crossing, or any other existing game.

What I want from you:
1. Define the core game idea in one sentence.
2. Define the target player.
3. Define the core loop.
4. Define what makes this game different.
5. Define the smallest playable MVP.
6. Define the first screen flow.
7. Define farm plot, seed, water, growth, harvest, sell, upgrade, save, and return rules.
8. Define time model: real-time, session-time, or step-based.
9. Define first 3-5 crops for MVP.
10. Define 3 possible themes and recommend one.
11. Define what should not be built in version 1.
12. Define a user-friendly monetization direction.
13. Define the first prototype task.

Rules:
- Keep MVP small enough for a solo developer.
- Prefer one farm screen for version 1.
- Prefer offline play.
- Do not add ads before the core loop is satisfying.
- Do not add animals, crafting, town, quests, social, leaderboard, login, cloud sync, or live events unless clearly needed later.

Expected output:
- One-sentence concept.
- Target player.
- Core loop.
- Differentiation.
- MVP scope.
- First screen flow.
- Game rules.
- Time model recommendation.
- Theme recommendation.
- Not-now list.
- Monetization direction.
- First prototype task.
```

## Prompt FL2: Game Design Document

Use this after the concept is clear.

```text
You are creating a game design document for my original Flutter farming life MVP.

Do not write code yet.

Use the approved concept from this task. If no concept exists, create a small original concept first and ask me to approve it before continuing.

What I want from you:
1. Game summary.
2. Core loop.
3. Session length target.
4. Farm plot rules.
5. Seed and crop rules.
6. Watering and growth rules.
7. Harvest and sell rules.
8. Currency and upgrade rules.
9. Inventory or storage rules.
10. Offline progress rules, if included.
11. Save and restore rules.
12. First 10 progression steps.
13. UI screens and HUD.
14. Animation, sound, and haptic feedback.
15. Analytics events.
16. Ad placement rules for later.
17. Done criteria for the first playable prototype.

Rules:
- Keep version 1 simple.
- Avoid animals, crafting, town, quests, live events, shop complexity, login, and cloud sync in MVP.
- Make rules precise enough for implementation and tests.
- Keep monetization out of active farming interactions.

Expected output:
- Complete MVP game design document.
- Rule tables where useful.
- First 10 progression steps.
- Prototype done criteria.
- Risks and open questions.
```

## Prompt FL3: Flutter Technical Architecture

Use this before implementation.

```text
You are designing the Flutter technical architecture for my original farming life game.

Use plain Flutter if it is enough for farm grid UI, timers, state, storage, and animations. Use Flame only if the approved design requires a custom game scene or many animated objects. Explain the choice.

Do not write code yet.

What I want from you:
1. Recommend plain Flutter or Flame.
2. Define folder structure.
3. Define pure farming simulation model.
4. Define plot model.
5. Define crop model.
6. Define inventory, currency, and upgrade model.
7. Define time and growth calculation.
8. Define offline progress calculation, if included.
9. Define local save data.
10. Define UI state management.
11. Define analytics event names.
12. Define future AdMob integration points.
13. Define test strategy.
14. Define the first implementation slice.

Rules:
- Keep simulation logic separate from UI.
- Make crop growth and economy logic testable without Flutter widgets.
- Follow the existing project architecture if this is inside an existing repo.
- Keep the first implementation slice small.
- Do not add Firebase, AdMob, purchases, social, cloud sync, or complex economy yet unless explicitly approved.
- Avoid overengineering.

Expected output:
- Architecture decision.
- Folder structure.
- Main classes or services.
- Farm, crop, inventory, and upgrade data model.
- Time/save algorithms.
- Data flow.
- First implementation slice.
- Test plan.
```

## Prompt FL4: First Playable Prototype

Use this to implement the first playable version.

```text
You are implementing the first playable prototype of my original Flutter farming life game.

Use the approved game design and technical architecture from this task. If no approved scope exists, create a small prototype scope and ask me to approve it before editing.

Scope:
- One farm screen.
- Small farm grid or fixed plots.
- 2-3 crop types.
- Plant seeds.
- Water crops.
- Crops grow using approved time model.
- Harvest crops.
- Sell crops for coins.
- One simple upgrade, if approved.
- Local save and restore.
- Basic HUD.
- No ads.
- No animals.
- No crafting.
- No town.
- No quests.
- No shop complexity.

What I want from you:
1. Inspect the repository first.
2. Implement only the first playable prototype.
3. Keep simulation logic pure and tested.
4. Keep UI simple, readable, and polished.
5. Follow existing project patterns.
6. Add focused tests for plant, water, grow, harvest, sell, save, restore, and upgrade if included.
7. Use lightweight verification unless a build is essential.
8. Explain how to run and manually test the prototype.

Rules:
- Do not add monetization yet.
- Do not add unrelated features.
- Do not introduce large dependencies unless approved.
- Do not copy assets, crops, characters, maps, UI, sounds, or branding from existing games.
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

## Prompt FL5: Prototype Fun and Quality Review

Use this after the first playable prototype exists.

```text
You are reviewing the first playable prototype of my original farming life game.

Inspect the repository and prototype implementation. Do not edit files.

What I want from you:
1. Review whether the farming loop feels clear.
2. Review whether crop growth timing feels satisfying.
3. Review whether planting, watering, harvesting, and selling are understandable.
4. Review whether the economy is too fast, too slow, or okay.
5. Review save/restore behavior.
6. Review visual and sound feedback opportunities.
7. Review performance risks.
8. Review code quality and test coverage.
9. Identify the top 3 fixes before adding features.
10. Identify what should not be added yet.
11. Create a small improvement scope.

Rules:
- Do not change code.
- Do not add ads yet.
- Prioritize clarity, satisfying feedback, economy balance, save reliability, and test coverage before monetization.
- Keep recommendations practical.

Expected output:
- Loop review.
- Economy review.
- Save/reliability review.
- Test coverage review.
- Top 3 fixes.
- Not-now list.
- Small improvement scope.
```

## Prompt FL6: Crops, Upgrades, Animals, and Progression Plan

Use this after the core prototype is playable.

```text
You are planning crops, upgrades, animals, and progression for my original farming life game.

Do not write code yet.

Use the current prototype and game design. Keep changes small enough for one update.

What I want from you:
1. Define first 30 progression steps.
2. Define crop unlock progression.
3. Define upgrade ideas.
4. Define animal ideas, if appropriate.
5. Define crafting or production ideas, if appropriate.
6. Score each addition by fun, complexity, balance risk, and monetization risk.
7. Recommend only 1-2 additions for the next update.
8. Define reward loop.
9. Define implementation order.

Rules:
- Prefer crop variety and small upgrades before animals or crafting.
- Do not add too many systems at once.
- Keep economy fair and readable.
- Do not add monetization until the gameplay loop is stable.
- Avoid complex shop, social, or live event systems in early versions.

Expected output:
- First 30 progression steps.
- Crop unlock plan.
- Upgrade table.
- Animal/crafting table, if useful.
- Recommended next features.
- Reward loop.
- Implementation order.
```

## Prompt FL7: Monetization and Analytics Plan

Use this only after the farming loop is satisfying enough.

```text
You are planning user-friendly monetization and analytics for my original farming life game.

Do not write code yet.

What I want from you:
1. Decide whether the game is ready for ads.
2. Define rewarded ad opportunities.
3. Define whether interstitial ads are appropriate.
4. Define frequency caps.
5. Define where ads must never appear.
6. Define analytics events needed to measure plant, water, harvest, sell, upgrade, retention, economy, and ad impact.
7. Define policy risks.
8. Create a safe implementation scope.

Rules:
- User experience comes before revenue.
- Policy compliance comes before revenue.
- Do not show ads during active farming interactions.
- Do not encourage ad clicks.
- Do not reward ad clicks.
- Prefer rewarded ads for optional speed-up, bonus coins, seed packs, or temporary helper.
- Use interstitials only at natural session transitions.
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

## Prompt FL8: Store Listing and Creative Asset Plan

Use this when the game has enough real visuals for store assets.

```text
You are planning Google Play store listing assets for my original farming life game.

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
- Do not copy names, visuals, crops, characters, farms, maps, or branding from other games.
- Do not show unavailable animals, buildings, crops, rewards, maps, events, or modes.
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

## Prompt FL9: Closed Testing and Release Readiness

Use this before Play Store testing or release.

```text
You are checking closed testing and release readiness for my original Flutter farming life game.

Use the repository and release checklist. Do not publish anything.

What I want from you:
1. Review build and version readiness.
2. Review gameplay correctness.
3. Review economy and save-data readiness.
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

## Prompt FL10: Post-Release Improvement Plan

Use this after testing or release.

```text
You are helping me improve my original farming life game after testing or release.

Use available tester feedback, reviews, analytics, Crashlytics, Android vitals, and AdMob data. If external data is missing, mark it as unknown.

What I want from you:
1. Summarize release health.
2. Identify gameplay loop issues.
3. Identify economy, crop timing, or progression issues.
4. Identify save-data issues.
5. Identify crash or performance issues.
6. Identify ad experience issues.
7. Identify retention or session issues.
8. Recommend the next small update.
9. Identify what should not be built yet.
10. Create a learning note.

Rules:
- Fix crashes, save-data issues, and serious economy frustration before adding new features.
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
Run Prompt FL1 from `prompts/farming-life-game-prompt-process.md`.
```

Then:

```text
Run Prompt FL2 from `prompts/farming-life-game-prompt-process.md` using the approved concept from this task.
```

Then:

```text
Run Prompt FL3 from `prompts/farming-life-game-prompt-process.md` using the approved game design from this task.
```

Only after approving architecture:

```text
Run Prompt FL4 from `prompts/farming-life-game-prompt-process.md` using the approved prototype scope from this task.
```

## Done Criteria

The game process is working when:

- The game has an original concept.
- The first prototype is playable.
- Plant, water, grow, harvest, sell, save, restore, and restart work.
- Simulation logic has focused tests.
- Crop timing and economy feel fair.
- The loop feels satisfying before ads are added.
- New systems are added gradually.
- Ads never interrupt active farming interactions.
- Store assets show real gameplay.
- Testing produces a learning note before the next update.
