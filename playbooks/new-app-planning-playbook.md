# New App Planning Playbook

Use this playbook every time a new Flutter app or game idea appears.

The goal is to turn a rough idea into a clear, small, reviewable MVP plan before creating a Flutter project or writing production code.

## Goal

Create a repeatable planning workflow that produces:

- A clear one-sentence idea.
- A specific target user.
- A small MVP.
- A first screen flow.
- A data, Firebase, monetization, analytics, and testing plan.
- A risk review.
- A first Codex implementation task.

## When to Use

Use this playbook for:

- New Flutter apps.
- New Flutter games.
- Major product rebuilds.
- Starter-kit experiments that may become real products.

Do not use this playbook for:

- Small bug fixes.
- Routine app updates.
- Minor UI changes.
- Emergency production fixes.

## Required Files

- `checklists/new-app-checklist.md`
- `templates/app-idea-brief.md`
- `prompts/new-app-planning-prompt.md`

## Required Inputs

Before starting, collect what you already know:

- Rough app or game idea.
- Target user.
- Main problem or desire.
- First platform.
- Monetization goal.
- Similar apps or games.
- Known Firebase, AdMob, or Play Store constraints.
- Whether the project should use a starter kit or fresh Flutter project.

Missing inputs are allowed, but they must be handled as questions or assumptions.

## Step 1: Capture the Raw Idea

Write the idea in plain language.

Do not improve it yet. Capture the original thought so the project has a starting point.

Minimum raw idea format:

```text
I want to build [type of app/game] for [target user] that helps them [main task/desire].
```

## Step 2: Run the Planning Prompt

Use `prompts/new-app-planning-prompt.md`.

Paste the raw idea and known constraints into the prompt.

Codex should return:

- Planning questions if needed.
- One-sentence idea.
- MVP scope.
- First screens.
- Main flow.
- Data and Firebase plan.
- Monetization plan.
- Analytics plan.
- Risk review.
- Filled app idea brief.
- First Codex task or a reduce/delay/stop recommendation.

## Step 3: Answer Critical Questions

If Codex asks questions, answer only what is needed to reduce uncertainty.

Prefer short answers.

Important questions usually involve:

- Target user.
- First release goal.
- Core app task or game loop.
- Whether monetization is required in version 1.
- Whether data must sync across devices.
- Whether Play Store policy risk exists.

Do not spend days researching before deciding whether the MVP is worth building.

## Step 4: Fill the App Idea Brief

Create a project-specific copy of `templates/app-idea-brief.md`.

Recommended location for future project briefs:

```text
examples/app-briefs/[project-name]-brief.md
```

If `examples/app-briefs/` does not exist yet, create it when the first real brief is needed.

Fill the brief using the planning prompt output.

Do not edit the original template when planning a real app.

## Step 5: Apply the New App Checklist

Review the filled brief against `checklists/new-app-checklist.md`.

Focus especially on:

- Idea clarity.
- MVP size.
- First screens.
- Data and storage.
- Firebase need.
- Monetization fit.
- Game loop, if relevant.
- Technical architecture.
- Analytics.
- Testing.
- Play Store readiness.
- Risk check.

The checklist does not need perfect answers, but it must reveal major unknowns.

## Step 6: Reduce Scope

Before implementation, cut the first version down.

Ask:

- Can this release work with fewer screens?
- Can login wait?
- Can cloud sync wait?
- Can monetization wait?
- Can advanced settings wait?
- Can AI features wait?
- Can animations or polish wait?

The first version should prove the core user value or game loop.

## Step 7: Decide Firebase and Analytics

Use Firebase only when it supports the MVP.

Default decisions:

- Analytics: useful for most production apps.
- Crashlytics: useful for most production apps.
- Auth: only when user identity is required.
- Firestore or Realtime Database: only when cloud data is required.
- Storage: only when files or media need cloud storage.
- Remote Config: useful later, not always needed in MVP.

Document why each Firebase product is included or deferred.

## Step 8: Decide Monetization

Choose the simplest monetization that fits the user journey.

Default decisions:

- Use no ads if the MVP needs trust or focus first.
- Use rewarded ads when the user gets optional value.
- Use banners only where they do not reduce usability.
- Use interstitial ads only at natural transition points.
- Avoid app-open ads until retention and user experience are understood.

Document ad format, placement, frequency, and test mode.

## Step 9: Review Play Store Risk

Before implementation, identify:

- App category.
- Ads disclosure.
- Data safety concerns.
- Privacy policy needs.
- Content rating concerns.
- Permission needs.
- Sensitive content concerns.
- Closed testing needs.

If policy risk is unclear, research official sources before release planning.

## Step 10: Approve or Stop

Choose one:

- Start implementation.
- Reduce scope and revise the brief.
- Delay the project.
- Stop the project.

Start implementation only when:

- The idea is clear.
- The MVP is small.
- The first screens are known.
- Monetization is user-friendly or deferred.
- Major risks are understood.
- The first Codex task is specific.

## Step 11: Create the First Codex Task

The first implementation task should be narrow.

Good first tasks:

- Create the Flutter project structure.
- Create the first screen flow with placeholder data.
- Define app architecture and folder structure.
- Implement the core loop for a simple game.
- Add local-only MVP behavior before Firebase.

Avoid first tasks like:

- Build the complete app.
- Add Firebase, AdMob, login, analytics, and all screens at once.
- Make it production ready immediately.
- Clone a large existing app.

## Verification

The planning phase is complete when:

- A project-specific app idea brief exists or is ready to create.
- `checklists/new-app-checklist.md` has been reviewed.
- MVP scope is reduced.
- Firebase and monetization decisions are documented.
- Play Store risks are known.
- The first Codex implementation task is clear.

## Common Mistakes

- Coding before the first screen flow is clear.
- Adding login too early.
- Adding Firebase products just because they are familiar.
- Adding ads before the user journey is stable.
- Planning too many screens.
- Ignoring privacy and Data safety until release day.
- Treating game ideas as screens instead of loops.
- Letting Codex implement without a clear review point.

## Follow-Up Tasks

After this playbook is complete, create or update:

- A project-specific app idea brief.
- A first implementation prompt.
- A technical architecture note.
- A release checklist when the MVP is close to testing.
- A learning note after the first release.

