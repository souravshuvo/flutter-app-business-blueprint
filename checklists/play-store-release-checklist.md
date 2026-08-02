# Play Store Release Checklist

Use this checklist before releasing a Flutter app or game to Google Play.

The purpose is to catch technical, policy, privacy, store listing, testing, and monetization issues before a release reaches users.

## Scope

Use this checklist for:

- Internal testing releases.
- Closed testing releases.
- Open testing releases.
- First production release.
- Production updates.
- Monetized app or game updates.

Do not skip this checklist for small updates. Small updates can still break policy, privacy, ads, analytics, or app quality.

## Official Sources to Review

Review the current official docs before every important release:

- Google Play Developer Program Policy: https://support.google.com/googleplay/android-developer/answer/17190352
- Target API level requirements: https://developer.android.com/google/play/requirements/target-sdk
- Create and set up your app: https://support.google.com/googleplay/android-developer/answer/9859152
- Data safety form: https://support.google.com/googleplay/android-developer/answer/10787469
- Testing tracks: https://support.google.com/googleplay/android-developer/answer/9845334
- New personal account testing requirements: https://support.google.com/googleplay/android-developer/answer/14151465
- Content rating: https://support.google.com/googleplay/android-developer/answer/9859655
- Pre-launch report: https://support.google.com/googleplay/android-developer/answer/9842757
- Android vitals: https://developer.android.com/topic/performance/vitals
- Staged rollouts: https://support.google.com/googleplay/android-developer/answer/6346149
- AdMob policies: https://support.google.com/admob/answer/6128543
- AdMob implementation guidance: https://support.google.com/admob/answer/2936217

## Current Rule Review

- [ ] Check current target API level requirements before uploading the app bundle.
- [ ] Check whether the developer account has current verification or Play Console requirements.
- [ ] Check whether the account is a personal account subject to closed testing requirements.
- [ ] Check whether any Google Play policy changed since the previous release.
- [ ] Check whether any Firebase, AdMob, analytics, or third-party SDK behavior changed.

Note: As of August 2, 2026, Google says that starting August 31, 2026, new apps and app updates must target Android 16/API 36 or higher for most app categories. Always confirm the current requirement from the official target API page before release.

## 1. Release Identity

- [ ] Confirm app name.
- [ ] Confirm package name.
- [ ] Confirm package name is final because package names cannot be reused or changed after upload.
- [ ] Confirm app type: app or game.
- [ ] Confirm free or paid status.
- [ ] Confirm release track: internal, closed, open, or production.
- [ ] Confirm release type: first release, update, hotfix, experiment, or staged rollout.
- [ ] Confirm release owner.
- [ ] Confirm release date target.

## 2. Versioning

- [ ] Increment `versionCode`.
- [ ] Set correct `versionName`.
- [ ] Confirm package name matches previous release for updates.
- [ ] Confirm signing key or upload key is correct.
- [ ] Confirm the build artifact is an Android App Bundle unless there is a specific reason otherwise.
- [ ] Save release notes for this version.

## 3. Build Configuration

- [ ] Build release artifact from the correct branch.
- [ ] Confirm debug mode is disabled.
- [ ] Confirm release signing is configured.
- [ ] Confirm app icon, label, and package ID are correct.
- [ ] Confirm target SDK meets current Google Play requirement.
- [ ] Confirm minimum SDK is intentional.
- [ ] Confirm no local-only config is included.
- [ ] Confirm no development API endpoints are used.
- [ ] Confirm no test Firebase project is used in production.
- [ ] Confirm no secrets, private keys, or admin credentials are bundled.
- [ ] Confirm ProGuard/R8/minification settings are intentional.
- [ ] Upload deobfuscation or symbol files when needed.

## 4. Flutter Quality Gate

- [ ] Run dependency install.
- [ ] Run formatting.
- [ ] Run static analysis.
- [ ] Run unit tests.
- [ ] Run widget tests.
- [ ] Run integration tests if available.
- [ ] Build the release app bundle.
- [ ] Install and launch the release build on a real device or emulator.
- [ ] Smoke test the main user flow.
- [ ] Smoke test first launch after fresh install.
- [ ] Smoke test update path if this is an app update.
- [ ] Smoke test offline or weak network behavior if relevant.
- [ ] Smoke test back button and navigation.
- [ ] Smoke test permissions.
- [ ] Smoke test dark mode if supported.
- [ ] Smoke test small and large screen layouts if relevant.

## 5. Crash and Performance Gate

- [ ] Confirm the app does not crash on first launch.
- [ ] Confirm the main flow does not crash.
- [ ] Confirm known Crashlytics issues are reviewed.
- [ ] Confirm Android vitals from the previous release are reviewed.
- [ ] Confirm no known serious ANR issue is ignored.
- [ ] Confirm startup time is acceptable.
- [ ] Confirm memory-heavy screens are tested.
- [ ] Confirm battery-heavy features are intentional.
- [ ] Confirm background work is necessary and controlled.
- [ ] Confirm logs do not expose private data.

## 6. Pre-Launch Report

- [ ] Upload the test or release artifact to Play Console.
- [ ] Wait for the pre-launch report when available.
- [ ] Review stability issues.
- [ ] Review performance issues.
- [ ] Review accessibility issues.
- [ ] Review screenshots.
- [ ] Review warnings and minor issues.
- [ ] Add test credentials if login blocks meaningful testing.
- [ ] Add a Robo script or game loop if the crawler cannot reach the main flow.
- [ ] Fix serious issues before production.
- [ ] Document ignored issues with reasons.

## 7. Data Safety and Privacy

- [ ] Review all data collected by the app.
- [ ] Review all data shared by the app.
- [ ] Review data collected or shared by SDKs and libraries.
- [ ] Review Firebase Analytics data.
- [ ] Review Crashlytics data.
- [ ] Review AdMob advertising data.
- [ ] Review login or account data if used.
- [ ] Review location, contacts, photos, files, microphone, camera, health, or financial data if used.
- [ ] Confirm Data safety answers match actual app and SDK behavior.
- [ ] Confirm privacy policy exists if required.
- [ ] Confirm privacy policy is linked in Play Console.
- [ ] Confirm privacy policy is accessible in the app if needed.
- [ ] Confirm data deletion flow or instructions if user data is stored.
- [ ] Confirm encryption in transit claims are accurate.
- [ ] Confirm personal or sensitive data is not logged.

## 8. Permissions

- [ ] List every Android permission requested by the app.
- [ ] Remove unused permissions.
- [ ] Confirm each permission supports a core user-facing feature.
- [ ] Confirm runtime permission prompts appear at the right time.
- [ ] Confirm permission denial is handled gracefully.
- [ ] Confirm prominent disclosure and consent are included when required.
- [ ] Confirm sensitive permissions are documented for Play review.

## 9. App Content and Policy

- [ ] Review Google Play Developer Program Policies.
- [ ] Confirm app content is appropriate for Google Play.
- [ ] Confirm app does not mislead users.
- [ ] Confirm app does not imitate system UI or warnings.
- [ ] Confirm app does not make false earning, ranking, health, financial, or performance claims.
- [ ] Confirm app does not include restricted content.
- [ ] Confirm user-generated content moderation requirements if applicable.
- [ ] Confirm AI-generated content policy requirements if applicable.
- [ ] Confirm gambling, finance, health, children, dating, social, or sensitive category rules if applicable.
- [ ] Confirm local law concerns for target countries.

## 10. Target Audience and Content Rating

- [ ] Select target audience accurately.
- [ ] Confirm whether children are included in the target audience.
- [ ] If children are included, review Families policy and ad SDK requirements.
- [ ] Complete content rating questionnaire accurately.
- [ ] Confirm content rating matches app content and ads.
- [ ] Re-submit content rating if app content or features changed.
- [ ] Confirm ads shown in the app are appropriate for the content rating.

## 11. Ads and Monetization

Use this section if the app has ads, in-app products, subscriptions, paid features, affiliate links, or any revenue feature.

- [ ] Declare whether the app contains ads in Play Console.
- [ ] Confirm AdMob account and app are correctly configured.
- [ ] Confirm production ad unit IDs are used only in production builds.
- [ ] Confirm test ads are used during development and QA.
- [ ] Confirm no developer, tester, friend, or family member is asked to click real ads.
- [ ] Confirm no feature encourages users to click ads.
- [ ] Confirm no reward is tied to clicking ads.
- [ ] Confirm rewarded ads reward viewing/completing the ad flow, not clicking the ad.
- [ ] Confirm banner ads have reserved space and do not cause accidental clicks.
- [ ] Confirm interstitial ads appear only at natural transition points.
- [ ] Confirm interstitial ads do not appear on app load or exit.
- [ ] Confirm repeated interstitials do not overwhelm users.
- [ ] Confirm app-open ads are not confused with interstitials.
- [ ] Confirm frequency caps are implemented.
- [ ] Confirm ad loading failures do not block core app usage.
- [ ] Confirm purchases or subscriptions are clearly described.
- [ ] Confirm paid features match store listing and in-app text.

## 12. Store Listing

- [ ] Confirm app title.
- [ ] Confirm short description.
- [ ] Confirm full description.
- [ ] Confirm app icon.
- [ ] Confirm feature graphic if needed.
- [ ] Confirm phone screenshots.
- [ ] Confirm tablet screenshots if tablet support is claimed.
- [ ] Confirm game screenshots if this is a game.
- [ ] Confirm preview video if used.
- [ ] Confirm category.
- [ ] Confirm tags.
- [ ] Confirm contact email.
- [ ] Confirm website if used.
- [ ] Confirm privacy policy URL.
- [ ] Confirm store listing text does not include misleading claims.
- [ ] Confirm store listing text does not mention unsupported features.
- [ ] Confirm screenshots match the current release.
- [ ] Confirm screenshots do not show fake results, fake earnings, or policy-risk content.

## 13. Testing Track

- [ ] Start with internal testing when possible.
- [ ] Confirm internal test build installs.
- [ ] Confirm testers have access.
- [ ] Confirm feedback channel exists.
- [ ] Use closed testing before production when required or useful.
- [ ] Confirm closed testers are real target-like users where possible.
- [ ] For eligible new personal developer accounts, confirm at least 12 testers are opted in for the required 14 continuous days before applying for production access.
- [ ] Document tester feedback.
- [ ] Fix serious tester-reported issues before production.
- [ ] Do not use open testing until the store listing is ready to be visible.

## 14. Production Release

- [ ] Confirm all Play Console dashboard setup items are complete.
- [ ] Confirm App content page has no blocking issues.
- [ ] Confirm release notes are written.
- [ ] Confirm countries and regions are intentional.
- [ ] Confirm device catalog exclusions are intentional.
- [ ] Confirm pricing is intentional.
- [ ] Confirm managed publishing setting is intentional.
- [ ] Confirm review warnings are understood.
- [ ] Submit release for review only after checklist is complete.
- [ ] Record submission date and version.

## 15. Staged Rollout for Updates

Use this section for production updates. Staged rollouts do not apply to first-time production releases.

- [ ] Decide rollout percentage.
- [ ] Decide rollout countries if needed.
- [ ] Monitor Crashlytics after rollout starts.
- [ ] Monitor Android vitals.
- [ ] Monitor Play Console reviews and ratings.
- [ ] Monitor AdMob revenue and ad issues if monetized.
- [ ] Pause rollout if serious crash, ANR, policy, or monetization issue appears.
- [ ] Increase rollout only after metrics look healthy.
- [ ] Document rollout decisions.

## 16. Post-Release Monitoring

- [ ] Confirm release is live or pending review.
- [ ] Check install and update availability.
- [ ] Check Crashlytics within 24 hours of release.
- [ ] Check Android vitals after data becomes available.
- [ ] Check user reviews.
- [ ] Check tester or user feedback.
- [ ] Check AdMob impressions, match rate, eCPM, and invalid traffic warnings if monetized.
- [ ] Check analytics events.
- [ ] Check store listing visibility.
- [ ] Create a post-release learning note using `templates/post-release-learning-note.md`.

## Done Criteria

This checklist is complete when:

- Build, versioning, signing, and target API are verified.
- Main release build is tested.
- Data safety and privacy answers match real app behavior.
- Store listing is accurate.
- Content rating and target audience are complete.
- Ads and monetization are compliant and user-friendly.
- Pre-launch report and quality signals are reviewed.
- Testing track requirements are satisfied.
- Release decision is documented.
- Post-release monitoring plan is clear.

