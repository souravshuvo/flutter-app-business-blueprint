# Contributing

This repository is maintained as a long-term personal engineering system for building Flutter apps and games.

Most contributions will come from the owner working with Codex. The standards below exist so every document, template, checklist, and future code module improves the system instead of becoming one more disconnected file.

## Contribution Goals

Every contribution should help one of these goals:

- Make future Flutter apps faster to start.
- Make app and game planning clearer.
- Make Firebase, AdMob, testing, and release work more repeatable.
- Reduce mistakes during Play Store publishing.
- Capture lessons from real production apps.
- Improve the owner-agent workflow.

If a change does not support the long-term app business system, it probably does not belong here.

## Workflow

Use this workflow for most changes:

1. Define the purpose of the change.
2. Check the existing repository structure.
3. Choose the correct folder or create the smallest needed structure.
4. Draft the document, template, checklist, prompt, or code.
5. Review it for reuse across many apps and games.
6. Verify formatting or tests.
7. Commit with a clear message when ready.

## Documentation Contributions

Good documentation in this repository should be:

- Practical.
- Repeatable.
- Easy to scan.
- Specific enough to use during real work.
- General enough to reuse across future apps.

Use short sections, checklists, and examples when they make the process easier to follow.

Avoid:

- Long motivational writing without action steps.
- One-off advice that cannot be reused.
- Outdated policy claims without a source or review note.
- Copy-pasted instructions that do not match Flutter, Firebase, AdMob, or Play Store reality.

## File Naming

Use lowercase names with hyphens for most documentation files:

```text
new-app-checklist.md
admob-setup-playbook.md
firebase-crashlytics-guide.md
release-review-template.md
```

Use uppercase conventional names only when they are standard at the repository root:

```text
README.md
AGENTS.md
CONTRIBUTING.md
CHANGELOG.md
LICENSE
```

## Folder Rules

Use the planned repository areas consistently:

```text
handbook/              Long-form system documentation
prompts/               Reusable Codex prompts
templates/             Planning and release templates
playbooks/             Step-by-step operating procedures
checklists/            Repeatable checklists
agents/                Agent roles and AI workflow notes
examples/              Example projects or patterns
starter_kit/           Future Flutter starter kit
flutter_monetization/  Future AdMob and monetization layer
game_framework/        Future simple-game foundation
release_system/        Play Store and rollout process
resources/             References and learning notes
```

Do not create a new top-level folder unless the existing structure clearly cannot hold the work.

## Writing Style

- Write repository files in English by default.
- Use Bangla only when the document is specifically intended as a Bangla guide.
- Keep sentences clear and direct.
- Prefer checklists for repeated actions.
- Prefer examples for prompts and templates.
- Use ASCII unless a file intentionally needs Unicode.
- Avoid decorative formatting that may render poorly in terminals.

## Prompt Contributions

Reusable prompts should include:

- Purpose.
- When to use it.
- Inputs required.
- Prompt text.
- Expected output.
- Review checklist.

Prompts should help Codex work like a disciplined engineering partner, not a shortcut machine.

## Checklist Contributions

Checklists should be action-oriented.

Each checklist should include:

- Scope.
- Prerequisites.
- Steps.
- Verification.
- Done criteria.

Good checklist items start with verbs, such as:

- Confirm app package name.
- Verify Firebase project.
- Run Flutter analyze.
- Check AdMob test mode.
- Review Play Store Data safety answers.

## Playbook Contributions

Playbooks are step-by-step procedures for repeated workflows.

Each playbook should include:

- Goal.
- When to use it.
- Required tools or accounts.
- Step-by-step process.
- Common mistakes.
- Verification.
- Follow-up tasks.

## Future Flutter Code Contributions

When this repository contains Flutter code, use these standards:

- Follow existing architecture.
- Keep feature modules focused.
- Separate UI, state, data, and services.
- Keep business logic testable.
- Do not hardcode secrets.
- Keep AdMob test and production configuration clearly separated.
- Add or update tests for risky behavior.
- Run formatting and analysis before considering work done.

## Monetization Contributions

Monetization changes require extra care.

Before adding or changing ad behavior, document:

- Where the ad appears.
- Why that placement is acceptable.
- Whether it is banner, interstitial, rewarded, native, or app-open.
- Frequency rules.
- User experience risk.
- Policy risk.
- Measurement plan.

Ads should never be added only because they can increase revenue. They must fit the user journey.

## Game Contributions

For game-related work, define:

- Core loop.
- Player goal.
- Session length.
- Difficulty curve.
- Reward structure.
- Monetization moment.
- Retention hook.

Do not add complex systems before the core loop is proven.

## Review Checklist

Before a change is ready, ask:

- Does this support the 5-10 year system?
- Can it be reused across multiple apps or games?
- Is it practical enough to follow?
- Is it clear where the file belongs?
- Are assumptions documented?
- Was formatting or testing checked?
- Is the next step obvious?

## Commit Messages

Use short, descriptive commit messages.

Examples:

```text
Add project foundation docs
Add new app planning checklist
Add AdMob setup playbook
Define starter kit architecture
```

Prefer one focused commit per logical change.

## Versioning

This repository is early-stage. Until a formal release process exists:

- Use `0.x` versions for foundation work.
- Update version notes only when a meaningful milestone is reached.
- Do not treat every small document edit as a release.

## Definition of Done

A contribution is done when:

- It solves the current need.
- It fits the repository structure.
- It is reusable for future apps or games.
- It is readable later without extra explanation.
- Verification has been performed or the limitation is clearly stated.
- The next useful step is known.

