# New App Planning Prompt

Use this prompt when starting a new Flutter app or game idea.

This prompt helps Codex turn a rough idea into a clear app brief, MVP scope, risk review, and first implementation task.

## Purpose

Guide a new app or game through disciplined planning before coding starts.

The goal is to prevent unclear scope, weak monetization, unnecessary Firebase setup, aggressive ads, and random implementation.

## When to Use

Use this prompt when:

- Starting a brand-new Flutter app.
- Starting a brand-new Flutter game.
- Turning a rough idea into a project plan.
- Reviewing whether an idea is small enough for MVP.
- Preparing to fill `templates/app-idea-brief.md`.

Do not use this prompt for small bug fixes or routine updates.

## Inputs Required

Provide as many of these as possible:

- App or game idea.
- Target user.
- Main problem or desire.
- Monetization goal.
- First platform.
- Any similar apps or games.
- Any required Firebase, AdMob, or Play Store constraints.
- Whether this should use the future starter kit or a fresh Flutter project.

If inputs are missing, Codex should ask focused questions or make clearly labeled assumptions.

## Prompt Text

```text
You are helping me plan a new Flutter app or game using the Flutter App Business Blueprint process.

Before writing code, help me turn this idea into a clear, small, release-ready MVP plan.

Repository process to follow:
- Use `checklists/new-app-checklist.md` as the planning gate.
- Use `templates/app-idea-brief.md` as the output structure.
- Keep the first version small.
- Prefer user experience before monetization.
- Prefer policy compliance before revenue.
- Prefer analytics before assumptions.
- Do not jump into implementation until the plan is clear.

My rough idea:
[PASTE IDEA HERE]

Known constraints:
[PASTE CONSTRAINTS HERE]

What I want from you:
1. Restate the idea in one sentence.
2. Identify the target user.
3. Clarify whether this is an app, game, utility, content app, tool, or experiment.
4. Define the smallest useful MVP.
5. List the first 3-5 screens.
6. Describe the main user flow.
7. Decide what data is needed.
8. Decide whether Firebase is needed for MVP.
9. Suggest a user-friendly monetization plan.
10. Suggest analytics events.
11. Identify Play Store and policy risks.
12. Identify what should be cut from the first version.
13. Produce a filled app idea brief based on `templates/app-idea-brief.md`.
14. Produce the first Codex implementation task only if the plan is clear.

Rules:
- Ask up to 5 focused questions first if critical information is missing.
- If the idea is too large, reduce scope.
- If monetization would hurt user experience, defer or redesign it.
- If Firebase is not needed for MVP, say so.
- If the idea is weak, explain the risk and suggest a better angle.
- Keep the plan practical enough for a solo developer.

Expected output:
- Planning questions, if needed.
- One-sentence idea.
- MVP scope.
- First screens.
- Main flow.
- Data/Firebase plan.
- Monetization plan.
- Analytics plan.
- Risk review.
- Filled app idea brief.
- First Codex task or a decision to delay/reduce scope.
```

## Expected Output

Codex should produce:

- A concise planning summary.
- A filled app idea brief.
- Clear MVP boundaries.
- A risk review.
- A start, reduce, delay, or stop recommendation.
- A first implementation task only when the plan is ready.

## Review Checklist

Before accepting the result, confirm:

- The idea is clear in one sentence.
- The target user is specific.
- The MVP is small enough.
- The first screens are known.
- Monetization fits the user journey.
- Firebase is only included when useful.
- Analytics events are meaningful.
- Play Store and policy risks are considered.
- The first Codex task is specific and safe.

## Common Mistakes

- Starting implementation before the MVP is clear.
- Adding login before it is needed.
- Adding Firebase products without a reason.
- Adding ads too early or too aggressively.
- Designing too many screens for version 1.
- Treating a game idea as only UI instead of a loop.
- Ignoring Play Store listing, privacy, and Data safety needs.

