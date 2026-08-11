# Play Store Creative Assets Prompt Pack

Use this prompt pack to create or improve Google Play store listing creative assets for an existing Flutter app or game.

This pack covers:

- Screenshot strategy.
- Screenshot copy and layout briefs.
- Feature graphic or vector-style hero visual.
- App icon concept and export plan.
- Preview video script, shot list, and production package.
- Final asset QA before Play Console upload.

## Purpose

Create useful, truthful, policy-conscious Play Store creative assets that show the real app clearly and help users understand why the app is worth installing.

This pack is designed for Codex repository workflow. Codex should inspect the current repository first, use existing app evidence, and avoid fake UI or misleading claims.

## Naming and Package Rule

For new games in this app business, use this convention unless explicitly approved otherwise:

- Store/display name: ASO-friendly, human-readable, truthful, and not keyword-stuffed.
- Package name/application ID: `com.childhood.<game_slug>`.
- `<game_slug>` should be lowercase ASCII, start with a letter, and use letters/numbers only where practical.
- Keep display name and package name separate.
- Do not use unauthorized real brands, official teams, copyrighted characters, fake affiliations, or misleading keywords.
- Treat package name as permanent after Play Store publishing.

## Current Official Asset Checks

Before final upload, verify the current official Google Play requirements:

- Preview assets: https://support.google.com/googleplay/android-developer/answer/9866151
- Asset library: https://support.google.com/googleplay/android-developer/answer/16386748

As of August 9, 2026, Google Play guidance includes:

- App icon: 512 x 512, 32-bit PNG with alpha, max 1024 KB.
- Feature graphic: 1024 x 500, JPEG or 24-bit PNG without alpha.
- Screenshots: JPEG or 24-bit PNG without alpha, minimum dimension 320 px, maximum dimension 3840 px, and maximum side no more than twice the minimum side.
- Recommended app screenshots: at least 4 screenshots at 1080 px or higher, 9:16 portrait or 16:9 landscape.
- Preview video: one YouTube URL, no playlist/channel URL, no extra URL parameters, ads disabled, short and polished, with the first 30 seconds strong because autoplay may use that portion.

Treat these as a checklist, not a substitute for checking the official page before publishing.

## Core Rules

- Do not fake app screens.
- Do not show features the app does not have.
- Do not use fake rankings, fake reviews, fake downloads, fake earnings, or fake awards.
- Do not use "best", "#1", "top", "new", "sale", "download now", or similar risky promotional claims unless the current Play policy and real evidence support it.
- Use actual app UI for screenshots whenever final screenshots are being produced.
- Generated images may be used for backgrounds, feature graphics, icons, textures, and supporting visuals, but not to misrepresent the app UI.
- Keep text short and readable on phones.
- Avoid crowded screenshot text.
- Keep every asset consistent with the real app category, audience, tone, and monetization.
- Do not run build, install, emulator, or device launch unless explicitly requested or required to capture real screenshots.

## Recommended Flow

For one app, run:

1. Prompt S1: Store creative audit and asset plan.
2. Prompt S2: Screenshot storyboard and copy.
3. Prompt S2B: Screenshot asset production, when approved.
4. Prompt S3: Feature graphic and vector-style visual brief.
5. Prompt S3B: Feature graphic asset production, when approved.
6. Prompt S4: App icon concept brief.
7. Prompt S4B: App icon asset production, when approved.
8. Prompt S5: Preview video script and shot list.
9. Prompt S5B: Video production package, when approved.
10. Prompt S6: Final Play Store asset QA.

Pattern:

- `S` prompts inspect, plan, storyboard, or brief.
- `SB` prompts create or edit approved assets.
- Do not run an `SB` prompt until the matching `S` prompt has produced a scope and you approve it.

## Prompt S1: Store Creative Audit and Asset Plan

Use this first.

```text
You are creating a Google Play store listing creative asset plan for the current Flutter repository.

Inspect the repository directly. Do not edit files. Do not build, install, run emulator, or launch a device.

Discover the app name, package name, app category, core features, screens, visual style, existing assets, icons, screenshots, store metadata, Firebase/AdMob usage, and target audience from the repository where possible.

What I want from you:
1. Summarize the app's core user value.
2. Identify the likely target user.
3. Propose or validate an ASO-friendly display name.
4. Propose or validate the final package name using `com.childhood.<game_slug>` for new games.
5. Identify the best 4-8 screenshot moments from the real app.
6. Identify whether the app needs portrait screenshots, landscape screenshots, or both.
7. Identify feature graphic direction.
8. Identify app icon risks or improvement opportunities.
9. Identify whether a preview video is useful for this app.
10. Identify policy or misleading-claim risks for store creative.
11. Create a prioritized creative asset plan.

Rules:
- Do not ask me for information visible in the repository.
- Mark Play Console, live listing, reviews, or competitor data as unknown if not available.
- Do not create assets yet.
- Do not make fake claims.
- Do not keyword-stuff the app name.
- Do not use unauthorized real brands, official teams, copyrighted characters, or fake affiliation claims.
- Recommend only assets that match the real app.

Expected output:
- App creative summary.
- ASO-friendly display name recommendation.
- Package name recommendation.
- Screenshot plan.
- Feature graphic direction.
- App icon direction.
- Preview video recommendation.
- Missing external inputs.
- Priority asset checklist.
- Next prompt to run.
```

## Prompt S2: Screenshot Storyboard and Copy

Use this to design the screenshot set before creating images.

```text
You are creating a Google Play screenshot storyboard for the current Flutter app.

Use the repository inspection and any previous creative audit in this task. Do not edit files. Do not create final images yet.

What I want from you:
1. Choose 4-8 screenshot slots.
2. For each slot, define the real app screen or user moment to show.
3. Write short overlay copy for each screenshot.
4. Write alt text for each screenshot in 140 characters or less.
5. Define recommended orientation and size target.
6. Identify any screenshots that require a real device/emulator capture.
7. Identify any generated background, frame, or vector-style support asset needed.
8. Create a ready-to-run Prompt S2B input.

Rules:
- Prioritize real app UI in the first three screenshots.
- Keep screenshot text short, truthful, and readable.
- Do not split important UI across multiple screenshots unless it remains understandable.
- Do not include fake metrics, fake user results, fake ratings, or unavailable features.
- Do not use "download now" or other call-to-action copy.
- Do not create final assets in this prompt.

Expected output:
- Screenshot storyboard table.
- Overlay copy.
- Alt text.
- Capture requirements.
- Supporting asset requirements.
- Ready-to-run Prompt S2B input.
```

## Prompt S2B: Screenshot Asset Production

Use this after approving the screenshot storyboard.

```text
You are creating approved Google Play screenshot assets for the current Flutter app.

Use the approved screenshot storyboard from this task. Re-read the relevant repository assets and UI references before creating or editing files.

What I want from you:
1. Create only the approved screenshot assets, source templates, or image-generation prompts.
2. Use real app screens as the basis for final screenshots.
3. If real screenshots are not available and I did not approve emulator/device capture, create a screenshot production brief instead of fake final screenshots.
4. Keep overlay text readable on phone screens.
5. Export or specify assets in Play-compatible dimensions and formats.
6. Create alt text for each final screenshot.
7. Produce a QA checklist.

Rules:
- Do not fake UI.
- Do not build, install, run emulator, or launch a device unless explicitly approved for screenshot capture.
- Do not modify app code unless explicitly approved.
- Do not touch unrelated files.
- Do not include misleading claims or unsupported features.
- If using generated visuals, use them only as frames, backgrounds, or supporting graphics around real UI.

Expected output:
- Screenshot assets or production-ready briefs.
- Source files changed or created, if any.
- Export specs.
- Alt text.
- Manual capture steps, if needed.
- QA checklist.
- Remaining risks.
```

## Prompt S3: Feature Graphic and Vector-Style Visual Brief

Use this to plan the feature graphic or other vector-style store visuals.

```text
You are creating a feature graphic and vector-style visual brief for the current Flutter app.

Inspect the repository assets, app icon, theme colors, screenshots, and core app value. Do not edit files yet.

What I want from you:
1. Propose 3 feature graphic concepts.
2. Recommend the strongest concept.
3. Define composition, color palette, typography direction, and visual hierarchy.
4. Define whether to use actual UI, abstract vector-style visuals, product objects, or game scene visuals.
5. Write image-generation prompts if bitmap generation would help.
6. Define export requirements.
7. Create a ready-to-run Prompt S3B input.

Rules:
- Feature graphic must convey real app value.
- Avoid tiny text and crowded detail.
- Do not duplicate the app icon as the main graphic.
- Do not imply ranking, awards, price, sale, or unsupported claims.
- Do not create final assets in this prompt.

Expected output:
- 3 concepts.
- Recommended concept.
- Visual brief.
- Image-generation prompt, if useful.
- Export checklist.
- Ready-to-run Prompt S3B input.
```

## Prompt S3B: Feature Graphic Asset Production

Use this after approving the feature graphic concept.

```text
You are creating the approved feature graphic or vector-style store visual for the current Flutter app.

Use the approved feature graphic brief from this task. Re-read relevant repository assets before creating or editing files.

What I want from you:
1. Create only the approved feature graphic or source asset.
2. Use a 1024 x 500 target export for Google Play feature graphic.
3. Use JPEG or 24-bit PNG without alpha for final export.
4. Keep important content inside a safe central area.
5. Keep text minimal and readable.
6. Produce alt text in 140 characters or less.
7. Produce a QA checklist.

Rules:
- Do not touch unrelated files.
- Do not create misleading visuals.
- Do not use fake rankings, awards, reviews, or performance claims.
- Do not include Google Play badges unless explicitly approved and policy-safe.
- If the final export cannot be generated here, create a production-ready design brief and exact image-generation prompt.

Expected output:
- Feature graphic asset or production-ready prompt.
- Source files changed or created, if any.
- Export specs.
- Alt text.
- QA checklist.
- Remaining risks.
```

## Prompt S4: App Icon Concept Brief

Use this before changing or generating the app icon.

```text
You are creating an app icon concept brief for the current Flutter app.

Inspect the repository for existing icons, launcher assets, brand colors, app purpose, and competing visual patterns if available. Do not edit files yet.

What I want from you:
1. Summarize the current icon and brand direction.
2. Identify icon issues: clarity, contrast, recognizability, similarity to competitors, text, badges, or policy risk.
3. Propose 3 icon concepts.
4. Recommend the strongest concept.
5. Define shape, symbol, color, depth, and style.
6. Write image-generation prompts if bitmap generation would help.
7. Create a ready-to-run Prompt S4B input.

Rules:
- App icon must be recognizable at small size.
- Avoid text inside the icon unless the brand requires it.
- Do not include ranking, price, sale, Google Play category, or misleading badges.
- Do not replace launcher icons without explicit approval.
- Do not create final assets in this prompt.

Expected output:
- Current icon review.
- 3 icon concepts.
- Recommended concept.
- Icon generation prompt, if useful.
- Export checklist.
- Ready-to-run Prompt S4B input.
```

## Prompt S4B: App Icon Asset Production

Use this after approving the icon concept.

```text
You are creating the approved app icon asset for the current Flutter app.

Use the approved app icon concept from this task. Re-read existing icon assets before creating or editing files.

What I want from you:
1. Create only the approved app icon source or production-ready prompt.
2. Target Google Play app icon export: 512 x 512, 32-bit PNG with alpha, max 1024 KB.
3. Preserve or document launcher icon update steps separately.
4. Keep the icon simple and recognizable at small sizes.
5. Produce a QA checklist.

Rules:
- Do not overwrite existing launcher icons unless explicitly approved.
- Do not touch unrelated files.
- Do not include misleading text, badges, ranking, price, or sale claims.
- If final export cannot be generated here, create a production-ready icon prompt and export instructions.

Expected output:
- Icon asset or production-ready prompt.
- Source files changed or created, if any.
- Export specs.
- Launcher icon update notes, if needed.
- QA checklist.
- Remaining risks.
```

## Prompt S5: Preview Video Script and Shot List

Use this before creating a preview video.

```text
You are creating a Google Play preview video plan for the current Flutter app.

Inspect the repository, app screens, screenshots, assets, and previous creative audit in this task. Do not create final video files yet.

What I want from you:
1. Decide whether a preview video is worth making for this app.
2. Recommend portrait or landscape orientation.
3. Create a 20-30 second script.
4. Create a shot-by-shot storyboard.
5. Identify real app screens or gameplay moments to capture.
6. Write on-screen text, voiceover, and caption options.
7. Identify music, sound, transition, and pacing direction.
8. Identify what must be captured from a real device/emulator.
9. Create a ready-to-run Prompt S5B input.

Rules:
- Show real app experience.
- Keep the first 30 seconds strong.
- Do not include fake UI, fake claims, fake reviews, or unsupported results.
- Do not include people tapping a device unless off-device use is essential to the app.
- Avoid black bars.
- Plan for a YouTube upload URL, not a playlist or channel URL.
- Do not create final video in this prompt.

Expected output:
- Video recommendation.
- Orientation recommendation.
- 20-30 second script.
- Shot list.
- Capture checklist.
- Production asset checklist.
- Ready-to-run Prompt S5B input.
```

## Prompt S5B: Preview Video Production Package

Use this after approving the video plan.

```text
You are creating the approved Google Play preview video production package for the current Flutter app.

Use the approved video script and shot list from this task. Re-read relevant repository assets before creating or editing files.

What I want from you:
1. Create final production materials for the approved preview video.
2. Prepare shot list, captions, voiceover, timing, and editing notes.
3. Create any approved supporting visual assets or image-generation prompts.
4. Identify exact real app capture steps.
5. Create YouTube upload checklist for Play preview video use.
6. Create final QA checklist.

Rules:
- Do not fake app footage.
- Do not run emulator/device capture unless explicitly approved.
- Do not include ads in the video.
- Do not use misleading claims or unsupported features.
- Do not touch unrelated files.
- If final video rendering is not approved or not practical here, create a complete production package instead.

Expected output:
- Production package.
- Files changed or created, if any.
- Capture steps.
- Captions and voiceover text.
- YouTube upload checklist.
- Play Console video checklist.
- Remaining risks.
```

## Prompt S6: Final Play Store Asset QA

Use this before uploading assets to Play Console.

```text
You are doing final QA for Google Play store listing creative assets for the current Flutter app.

Inspect the created assets, source files, copy, screenshots, icon, feature graphic, and preview video production package available in the repository or this task. Do not edit files unless I explicitly approve fixes.

What I want from you:
1. Check assets against current Google Play requirements.
2. Check that screenshots show real app UI.
3. Check that icon and feature graphic meet size, format, and policy expectations.
4. Check that preview video plan or upload notes are Play-compatible.
5. Check text readability.
6. Check consistency across icon, screenshots, feature graphic, and video.
7. Identify misleading claims, unsupported features, or policy risks.
8. Create a final upload checklist.

Rules:
- Verify current official Google Play asset requirements before final upload if internet access is available.
- Do not publish anything.
- Do not make unsupported claims.
- Mark unknowns clearly.

Expected output:
- Asset QA summary.
- Pass/fail checklist.
- Required fixes.
- Optional improvements.
- Play Console upload checklist.
```

## Quick Copy-Paste Commands

```text
Run Prompt S1 from `prompts/play-store-creative-assets-prompt-pack.md` for the current repository.
```

```text
Run Prompt S2 from `prompts/play-store-creative-assets-prompt-pack.md` for the current repository.
```

```text
Run Prompt S2B from `prompts/play-store-creative-assets-prompt-pack.md` for the current repository, using the approved screenshot storyboard from this task.
```

```text
Run Prompt S3 from `prompts/play-store-creative-assets-prompt-pack.md` for the current repository.
```

```text
Run Prompt S3B from `prompts/play-store-creative-assets-prompt-pack.md` for the current repository, using the approved feature graphic brief from this task.
```

```text
Run Prompt S4 from `prompts/play-store-creative-assets-prompt-pack.md` for the current repository.
```

```text
Run Prompt S4B from `prompts/play-store-creative-assets-prompt-pack.md` for the current repository, using the approved app icon concept from this task.
```

```text
Run Prompt S5 from `prompts/play-store-creative-assets-prompt-pack.md` for the current repository.
```

```text
Run Prompt S5B from `prompts/play-store-creative-assets-prompt-pack.md` for the current repository, using the approved preview video plan from this task.
```

```text
Run Prompt S6 from `prompts/play-store-creative-assets-prompt-pack.md` for the current repository.
```

## Done Criteria

The store creative process is done when:

- Screenshot plan is based on real app screens.
- Screenshot text is short, readable, and truthful.
- Feature graphic communicates the app value without misleading claims.
- App icon is clear at small size and Play-compatible.
- Preview video plan shows real app experience.
- Required asset dimensions and formats are checked against current Google Play guidance.
- Assets have alt text or descriptions where useful.
- Play Console manual upload checklist is ready.
