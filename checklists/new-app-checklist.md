# New App Checklist

Use this checklist before starting any new Flutter app or game.

The purpose is to prevent random coding, unclear scope, weak monetization, and avoidable release mistakes. A new project should pass this checklist before production implementation begins.

## Scope

Use this checklist for:

- A brand-new Flutter app.
- A brand-new Flutter game.
- A major rebuild of an existing app.
- A reusable starter-kit experiment that may become a real product.

Do not use this checklist for small bug fixes or routine updates.

## Prerequisites

- Confirm the project has a clear owner.
- Confirm the project has a simple working name.
- Confirm whether this is an app, game, tool, utility, content app, or experiment.
- Confirm whether the goal is learning, portfolio, revenue, user growth, or testing a reusable system.
- Confirm the expected first release platform.

## 1. Idea Clarity

- [ ] Write the app or game name.
- [ ] Write the one-sentence product idea.
- [ ] Define the target user.
- [ ] Define the main problem or desire.
- [ ] Explain why the user would open it more than once.
- [ ] Identify the closest existing alternatives.
- [ ] Write what makes this project simpler, better, faster, more useful, or more fun.

## 2. Product Type

- [ ] Mark the project type: app or game.
- [ ] If app, define the core user task.
- [ ] If game, define the core game loop.
- [ ] Define the expected session length.
- [ ] Define the first success moment for the user.
- [ ] Define what the user should do after the first success moment.

## 3. MVP Scope

- [ ] Define the smallest useful version.
- [ ] List must-have features only.
- [ ] List nice-to-have features separately.
- [ ] Remove anything that is not needed for the first release.
- [ ] Define the first 3-5 screens.
- [ ] Define what can be mocked, delayed, or manually handled.
- [ ] Confirm the MVP can be built and tested quickly.

## 4. Screen Flow

- [ ] Draw or describe the first screen.
- [ ] Draw or describe the main flow.
- [ ] Define navigation between screens.
- [ ] Define empty states.
- [ ] Define error states.
- [ ] Define loading states.
- [ ] Define offline or no-internet behavior if relevant.

## 5. Data and Storage

- [ ] Define what data the app needs.
- [ ] Define whether data is local, cloud, or both.
- [ ] Define whether user login is required.
- [ ] Avoid login if the MVP does not need it.
- [ ] Define any sensitive data.
- [ ] Define backup or restore needs.
- [ ] Define data deletion needs if user data is stored.

## 6. Firebase Plan

- [ ] Decide whether Firebase is needed for the MVP.
- [ ] Decide whether Analytics is needed.
- [ ] Decide whether Crashlytics is needed.
- [ ] Decide whether Remote Config is needed.
- [ ] Decide whether Firestore, Realtime Database, Storage, Auth, or Cloud Functions are needed.
- [ ] Document required Firebase console setup.
- [ ] Avoid adding Firebase products without a clear use case.

## 7. Monetization Plan

- [ ] Decide whether the first release will include monetization.
- [ ] Choose monetization type: AdMob, in-app purchase, subscription, paid app, affiliate, or none.
- [ ] If using ads, define the ad formats.
- [ ] If using rewarded ads, define the reward.
- [ ] If using interstitial ads, define the natural transition point.
- [ ] If using banner ads, define where they appear.
- [ ] Define ad frequency limits.
- [ ] Confirm ads do not block the core user experience.
- [ ] Confirm test ads will be used during development.
- [ ] Confirm production ad IDs are not hardcoded in sample or test code.

## 8. Game-Specific Planning

Use this section only for games.

- [ ] Define the core loop.
- [ ] Define the player goal.
- [ ] Define scoring.
- [ ] Define win, lose, and retry conditions.
- [ ] Define difficulty progression.
- [ ] Define reward moments.
- [ ] Define sound and haptic needs.
- [ ] Define save progress needs.
- [ ] Define where rewarded ads fit naturally.
- [ ] Confirm the game can be fun before adding complex systems.

## 9. Technical Architecture

- [ ] Choose the base approach: starter kit, existing app clone, or fresh Flutter project.
- [ ] Define package name.
- [ ] Define app version.
- [ ] Define minimum supported Android version.
- [ ] Define state management approach.
- [ ] Define routing approach.
- [ ] Define feature folder structure.
- [ ] Define service layer needs.
- [ ] Define environment configuration needs.
- [ ] Confirm no secrets will be committed.

## 10. Analytics Plan

- [ ] Define the key success metric.
- [ ] Define first-open event.
- [ ] Define main action event.
- [ ] Define retention-related events.
- [ ] Define monetization events if ads or purchases are used.
- [ ] Define crash and error monitoring needs.
- [ ] Avoid tracking personal or sensitive data.

## 11. Testing Plan

- [ ] Define what logic needs unit tests.
- [ ] Define what UI needs widget tests.
- [ ] Define manual test devices or emulators.
- [ ] Define release smoke test steps.
- [ ] Define monetization test steps.
- [ ] Define offline or poor-network test steps if relevant.

## 12. Play Store Readiness

- [ ] Define app category.
- [ ] Draft short description.
- [ ] Draft full description.
- [ ] Define screenshot plan.
- [ ] Define feature graphic plan if needed.
- [ ] Identify privacy policy needs.
- [ ] Identify Data safety answers that may be required.
- [ ] Identify content rating concerns.
- [ ] Identify ads disclosure needs.
- [ ] Plan closed testing if required.

## 13. Risk Check

- [ ] Identify the biggest technical risk.
- [ ] Identify the biggest product risk.
- [ ] Identify the biggest monetization risk.
- [ ] Identify the biggest policy risk.
- [ ] Identify what can be cut if the project becomes too large.
- [ ] Confirm the first release is still small enough.

## 14. Codex Work Plan

- [ ] Write the first implementation prompt.
- [ ] Define what Codex should inspect first.
- [ ] Define the expected output.
- [ ] Define what should not be changed.
- [ ] Define verification commands.
- [ ] Define human review points.

## 15. Start Decision

- [ ] Confirm the idea is clear.
- [ ] Confirm the MVP is small.
- [ ] Confirm the first screen flow is known.
- [ ] Confirm architecture choices are known.
- [ ] Confirm monetization is user-friendly or deferred.
- [ ] Confirm Play Store risks are known.
- [ ] Confirm the next task is specific enough to start.

## Done Criteria

This checklist is complete when:

- The app or game can be explained in one sentence.
- The target user is clear.
- The MVP is small and specific.
- The first screens are known.
- Data, Firebase, monetization, testing, and release needs are understood.
- Major risks are written down.
- The first Codex task can be given without confusion.

## Output

After completing this checklist, create one of these:

- `templates/app-idea-brief.md` filled for the project.
- A project-specific planning document.
- A first Codex implementation prompt.
- A decision to stop, reduce scope, or delay the project.

