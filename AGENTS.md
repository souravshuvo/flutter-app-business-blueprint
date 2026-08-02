# AGENTS.md

Guidance for Codex and any future AI agent working in this repository.

## Project Role

This repository is the long-term operating system for building Flutter apps and games as a solo app business.

Agents must treat this project as a reusable engineering system, not a one-off app repository. The goal is to create durable process, documentation, prompts, templates, starter kits, monetization patterns, and release playbooks that can be reused for many apps over 5-10 years.

## Core Rule

AI does not replace software engineering. It accelerates disciplined software engineering.

Agents should help the owner think, plan, review, implement, test, and improve. Do not encourage copy-paste development without understanding.

## Working Style

- Prefer clear process over fast output.
- Prefer small, reusable foundations over large one-off documents.
- Prefer practical checklists, templates, and examples over vague theory.
- Prefer English for repository files unless a file is intentionally written for Bangla readers.
- Keep files readable in Windows, GitHub, and common terminals.
- Use ASCII in source and documentation unless there is a strong reason not to.
- Keep changes focused on the user's current request.
- Do not rewrite unrelated files.
- Do not introduce large frameworks, tools, or dependencies without a clear reason.

## Decision Order

When working on this repo, follow this order:

1. Understand the goal.
2. Check existing files and structure.
3. Update or create the smallest useful artifact.
4. Keep the artifact reusable for future apps and games.
5. Verify the change.
6. Explain what changed and the next logical step.

## Documentation Standards

Documentation should be:

- Practical.
- Repeatable.
- Easy to scan.
- Versionable.
- Useful during real app development.
- Written so the owner can follow it again months later.

Every major document should answer:

- What is this for?
- When should it be used?
- What steps should be followed?
- What mistakes should be avoided?
- What does "done" mean?

## Planned Repository Areas

Use these areas consistently:

```text
handbook/              Long-form system documentation
prompts/               Reusable Codex prompts
templates/             Planning, app spec, issue, and release templates
playbooks/             Step-by-step operating procedures
checklists/            Practical checklists for repeatable work
agents/                Agent-specific notes, roles, and experiments
examples/              Small examples that demonstrate system patterns
starter_kit/           Future reusable Flutter app starter
flutter_monetization/  Future reusable AdMob and monetization layer
game_framework/        Future reusable simple-game foundation
release_system/        Play Store, testing, rollout, and update process
resources/             References, links, notes, and learning material
```

If a planned folder does not exist yet, create it only when it is needed for the current task.

## App and Game Workflow

Agents should guide every app or game through this lifecycle:

1. Idea
2. Market check
3. MVP scope
4. Screen flow
5. Technical architecture
6. Implementation
7. Human review
8. Testing
9. Firebase, analytics, and crash monitoring
10. Monetization
11. Closed testing
12. Production release
13. Monitoring
14. Revenue and retention review
15. Learning note
16. Next update

Do not jump straight to code when planning, architecture, monetization, privacy, or release requirements are unclear.

## Flutter Engineering Standards

When the repository later contains Flutter code, agents should prefer:

- Clear feature-based structure.
- Separation of UI, state, data, and platform services.
- Small widgets and focused services.
- Testable business logic.
- Explicit app configuration.
- Consistent naming.
- Centralized logging and error handling.
- Analytics events with stable names.
- No hardcoded production secrets.
- No real AdMob ad IDs in test examples unless explicitly required.

Before changing Flutter code, inspect the existing architecture and follow local patterns.

## Firebase Standards

For Firebase-related work:

- Keep setup steps documented.
- Separate dev/test/prod configuration where practical.
- Track only useful analytics events.
- Use Crashlytics for production crash visibility.
- Avoid logging personal or sensitive user data.
- Document required console-side setup.

## AdMob and Monetization Standards

Monetization must protect user experience and policy compliance.

Agents should:

- Prefer rewarded ads for optional value exchange.
- Use interstitial ads only at natural transition points.
- Avoid aggressive ad frequency.
- Keep test ads and production ads clearly separated.
- Document where each ad format is allowed.
- Add frequency caps before scaling ad placements.
- Never optimize revenue in a way that harms trust, usability, or policy compliance.

Every monetization change should consider:

- User experience.
- Policy risk.
- Revenue potential.
- Implementation complexity.
- Measurement plan.

## Game Standards

For game-related work, agents should think in loops:

- Core loop.
- Reward loop.
- Difficulty progression.
- Session length.
- Retention hook.
- Monetization moment.

Games should be simple enough to finish, test, release, and improve. Avoid overbuilding before the core loop is fun.

## Testing and Verification

For documentation-only changes:

- Check formatting.
- Check links or paths when present.
- Check `git status --short`.

For Flutter code changes:

- Run formatting.
- Run static analysis.
- Run relevant tests.
- Manually inspect risky UI or monetization behavior when practical.

If verification cannot be run, clearly say why.

## Done Criteria

A task is done when:

- The requested artifact or change exists.
- It fits the long-term system vision.
- It does not add unrelated churn.
- It is understandable by the owner later.
- Basic verification has been performed.
- The next useful step is clear.

## Git Hygiene

- Do not overwrite user changes.
- Do not reset or discard work unless explicitly asked.
- Keep commits focused when commits are requested.
- Prefer descriptive commit messages.
- Mention untracked or modified files in the final response when relevant.

## Agent Response Style

When reporting work:

- Be concise.
- Explain what changed.
- Mention verification.
- Suggest the next useful artifact or step.
- Avoid overpromising.

