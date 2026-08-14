from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    Flowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "output" / "pdf" / "game-production-store-asset-prompt-runbook.pdf"


class Rule(Flowable):
    def __init__(self, width=170 * mm, color=colors.HexColor("#D6DEE8")):
        super().__init__()
        self.width = width
        self.color = color
        self.height = 1

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(0.75)
        self.canv.line(0, 0, self.width, 0)


def make_styles():
    base = getSampleStyleSheet()
    styles = {
        "title": ParagraphStyle(
            "TitleCustom",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=27,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#172033"),
            spaceAfter=8,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=15,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#4A5568"),
            spaceAfter=14,
        ),
        "h1": ParagraphStyle(
            "H1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=15,
            leading=19,
            textColor=colors.HexColor("#172033"),
            spaceBefore=12,
            spaceAfter=6,
        ),
        "h2": ParagraphStyle(
            "H2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12.5,
            leading=16,
            textColor=colors.HexColor("#24415F"),
            spaceBefore=10,
            spaceAfter=5,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=13.5,
            textColor=colors.HexColor("#202938"),
            spaceAfter=5,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8.2,
            leading=11.5,
            textColor=colors.HexColor("#445064"),
            spaceAfter=4,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=12.8,
            leftIndent=12,
            firstLineIndent=-7,
            textColor=colors.HexColor("#202938"),
            spaceAfter=2.5,
        ),
        "code": ParagraphStyle(
            "Code",
            parent=base["BodyText"],
            fontName="Courier",
            fontSize=7.4,
            leading=10.1,
            leftIndent=0,
            rightIndent=0,
            backColor=colors.HexColor("#F6F8FB"),
            borderColor=colors.HexColor("#D8E0EA"),
            borderWidth=0.5,
            borderPadding=6,
            textColor=colors.HexColor("#1F2937"),
            splitLongWords=True,
            wordWrap="CJK",
            spaceAfter=8,
        ),
        "label": ParagraphStyle(
            "Label",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=9.5,
            leading=12.5,
            textColor=colors.HexColor("#1E3A5F"),
            spaceAfter=3,
        ),
    }
    return styles


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#6B7280"))
    canvas.drawString(18 * mm, 12 * mm, "Game Production and Store Asset Prompt Runbook")
    canvas.drawRightString(192 * mm, 12 * mm, f"Page {doc.page}")
    canvas.restoreState()


def p(text, style):
    return Paragraph(escape(text).replace("\n", "<br/>"), style)


def bullet(text, styles):
    return Paragraph("- " + escape(text), styles["bullet"])


def code(text, styles):
    return Paragraph(escape(text).replace("\n", "<br/>"), styles["code"])


def prompt_block(title, text, styles):
    return KeepTogether([p(title, styles["label"]), code(text.strip(), styles)])


PRODUCTION_STEPS = [
    (
        "Step P1 - Strict Audit / Scope Lock",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\game-production-ready-prompt-pack.md`.

For the current repository, run Prompt P1.

Be strict. Inspect whether the game is actually production-ready or still prototype-level.

Check:
- Architecture mismatch.
- Incomplete gameplay.
- Placeholder/fake functionality.
- Missing screens/states.
- Missing levels/content/modes.
- Confusing controls or weak touch handling.
- Weak/missing animation and feedback.
- Weak game hub/dashboard.
- Generic level-list UX where the genre needs a better flow.
- Boring gameplay loop with no replay hook.
- Sound/haptics toggles exist but gameplay does not trigger feedback.
- Confusing onboarding or unclear first action.
- Weak UI polish.
- Screenshot-ready gameplay/screens missing.
- Missing save/progress.
- Missing AdMob/analytics.
- Missing ASO-friendly app name.
- Missing package name convention: `com.childhood.<game_slug>`.
- Release blockers.

Do not edit files yet.
Do not run `flutter pub get`, `dart pub get`, `flutter run`, `flutter build`, full `flutter analyze`, full `flutter test`, Gradle, install, emulator, or release packaging unless essential.

Expected output:
- Production v1 checklist.
- Blockers.
- Approved implementation order.
- Skipped heavy checks.
""",
    ),
    (
        "Step P2 - UI + Animation + Game Feel",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\game-production-ready-prompt-pack.md`.

All P1 production v1 scope items are authorized; do not request approval.

For the current repository, run Prompt P2.

You are approved to modify code/docs for UI, animation, controls, and gameplay polish only.

Fix:
- Architecture mismatch if it blocks game correctness.
- Broken/incomplete core gameplay.
- Placeholder/fake behavior.
- Confusing first-time flow.
- Childish, template-like, or placeholder-looking UI.
- Weak dashboard/home that does not feel like a real game hub.
- Generic level section where quick play, missions, challenges, rounds, waves, endless, or campaign flow would be better.
- Gameplay has no replay hook, score chase, combo, streak, mission, unlock, achievement, or progression motivation.
- Poor controls, small tap targets, bad drag/touch handling, or unclear hit areas.
- Missing/weak visual feedback for valid moves, invalid moves, score, win, loss, rewards, retry, and errors.
- Missing lightweight feedback sounds/haptics for tap, valid action, invalid action, score/reward, win, and loss.
- Missing/slow/meaningless animations.
- Missing menus, pause/restart, result screens, settings.
- Weak mobile UI, HUD readability, spacing, contrast, or small-screen layout.
- Missing simple onboarding, help, or hints where the game is not self-explanatory.

Do not add AdMob yet.
Do not touch unrelated files.
Do not ship a childish, template-like, or placeholder-looking UI.
Do not force every game into a generic levels screen.
Do not add slow decorative animation that blocks repeated play.
Use lightweight built-in/system feedback sounds and haptics for core moments without adding custom audio assets or new audio packages.
Add or verify sound and haptic toggles in settings.
Do not add custom sound assets, music, sound packs, or audio dependencies unless essential.
If built-in feedback sound cannot work reliably, report the exact blocker instead of claiming sound is done.
Do not let text, buttons, ads, HUD, or dialogs overlap active gameplay.
Do not run `flutter pub get`, `dart pub get`, `flutter run`, `flutter build`, full `flutter analyze`, full `flutter test`, Gradle, install, emulator, or release packaging unless essential.

Expected output:
- UX/game-feel checklist.
- Professional hub/dashboard changes.
- Animation and feedback changes.
- Feedback sound/haptic coverage.
- Engagement/replay hook changes.
- Skipped heavy checks.
- Manual QA steps for first-time user flow, controls, and small screens.
""",
    ),
    (
        "Step P2B - Pro Game Vibe Rescue",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\game-production-ready-prompt-pack.md`.

For the current repository, run Prompt P2B.

The current result still feels amateur. You are approved to fix professional game vibe, dashboard UX, gameplay feel, feedback, and screenshot-ready screens only.

Fix:
- Top reasons the game looks childish, generic, or prototype-like.
- Weak home/dashboard; make it a useful game hub.
- Generic level-list UX; replace it when the genre needs quick play, missions, challenges, rounds, waves, endless, campaign, or continue flow.
- Boring gameplay; add a small replay hook such as score chase, combo, streak, missions, stars, unlocks, achievements, or escalating challenge.
- Weak result screens; make retry/next/continue natural.
- Sound/haptic feedback not triggered during real gameplay.
- Missing screenshot-ready moments/screens.

Do not add AdMob.
Do not add login, online multiplayer, cloud sync, fake online opponents, fake rewards, or heavy economy systems.
Do not add custom audio assets or audio dependencies unless sound cannot work reliably with built-in feedback; then use the smallest practical local audio approach and report it.
Do not run `flutter pub get`, `flutter run`, `flutter build`, full `flutter analyze`, full `flutter test`, Gradle, install, emulator, or release packaging unless essential.

Expected output:
- Top 10 amateur-feel causes found.
- Professional hub/dashboard changes.
- Gameplay engagement changes.
- Sound/haptic trigger coverage.
- Screenshot-ready screens created or improved.
- Skipped heavy checks.
- Remaining risks.
""",
    ),
    (
        "Step P3 - Levels / Content / Modes",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\game-production-ready-prompt-pack.md`.

For the current repository, run Prompt P3 using the P1 production content target. All required work is authorized.

You are authorized to add enough production v1 content.

Add or complete:
- Genre-appropriate content: levels, missions, waves, boards, puzzles, modes, AI modes, rounds, challenges, achievements, or progression.
- Save/progress where needed.
- Replay goals such as score chase, stars, streaks, missions, unlocks, or achievements where appropriate.
- Validation/tests for game rules where practical.

Do not add AdMob yet.
Do not touch unrelated files.
Do not force a visible level section if quick play, missions, rounds, waves, endless mode, or challenge flow is better.
Do not run `flutter pub get`, `dart pub get`, `flutter run`, `flutter build`, full `flutter analyze`, full `flutter test`, Gradle, install, emulator, or release packaging unless essential.

Expected output:
- Content added.
- Skipped heavy checks.
- Remaining risks.
""",
    ),
    (
        "Step P2C - Visual Gameplay Iteration",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\game-production-ready-prompt-pack.md`.

For the current repository, run Prompt P2C.

Use available screenshots, screen recording, manual play notes, QA notes, or previous findings from this task.

Goal:
- Judge the actual first 10 seconds of play.
- Review home/dashboard, first play entry, gameplay screen, pause/settings, result screen, and retry/next flow.
- Check whether the game looks professional, fun, readable, and screenshot-ready.
- Check whether gameplay has a reason to continue: score chase, combo, streak, mission, stars, unlock, achievement, progression, or escalating challenge.
- Check whether sounds/haptics trigger from real gameplay events and respect settings.
- Score the game using the 95% Game Feel Gate: first 10 seconds 15, visual UI/hub/HUD/results 20, controls/touch/small-screen 15, gameplay/replay/progression 20, sound/haptics 10, content/modes 10, screenshot readiness 10.
- Fix the highest-impact 3-5 visual/gameplay feel issues only.

Rules:
- Do not claim real game feel is verified unless screenshots, recording, live app output, or manual play evidence was inspected.
- Do not claim 95%+ unless real visual/play evidence was inspected.
- If no visual evidence is available, run the smallest practical visual check when possible; otherwise mark visual gameplay feel as not verified and list exact manual checks.
- Do not run `flutter pub get`, `flutter run`, `flutter build`, full `flutter analyze`, full `flutter test`, Gradle, install, emulator, or device capture unless essential.
- When visual capture is essential, run only the smallest practical command needed.
- Do not add AdMob, login, cloud sync, fake online features, or unrelated systems.

Expected output:
- Evidence used.
- Visual/gameplay feel verdict.
- 95% Game Feel Gate score and pass/iterate/rescue decision.
- Top feel problems found.
- Fixes implemented this iteration.
- Sound/haptic verification status.
- Screenshot-readiness status.
- Skipped heavy checks.
- Next manual play checklist.
- Remaining risks.
""",
    ),
    (
        "Step P4 - AdMob + Analytics",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\game-production-ready-prompt-pack.md`.

For the current repository, run Prompt P4.

You are approved to implement production-safe AdMob and analytics.

Rules:
- Ads must not interrupt active gameplay.
- Use test/prod ad separation.
- Add frequency caps before interstitials.
- Ad failure must not block gameplay.
- Add analytics for gameplay, difficulty, retention, and ad impact.
- Keep package name as `com.childhood.<game_slug>` for new unpublished apps.
- Do not run `flutter pub get`, `dart pub get`, `flutter run`, `flutter build`, full `flutter analyze`, full `flutter test`, Gradle, install, emulator, or release packaging unless essential.
""",
    ),
    (
        "Step P5 - Store / ASO / Assets Plan",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\game-production-ready-prompt-pack.md`.

For the current repository, run Prompt P5.

Confirm:
- ASO-friendly app name.
- Package name: `com.childhood.<game_slug>`.
- Store listing copy.
- Screenshot plan.
- Screenshot asset production or exact screenshot capture blocker if assets are approved.
- Feature graphic brief.
- App icon brief.
- Preview video script.

Do not fake gameplay.
Do not show unavailable features.
Do not silently skip screenshots. Create assets, create source templates, or list exact real capture blockers.
Do not run `flutter pub get`, `flutter run`, `flutter build`, install, emulator, or device screenshot capture unless essential.
""",
    ),
    (
        "Step P6 - Final Release Check",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\game-production-ready-prompt-pack.md`.

For the current repository, run Prompt P6.

Be strict. Do not claim production-ready unless checks support it.
Do not recommend store asset production, AdMob rollout, or release if the latest real-evidence game feel score is below 95 unless I explicitly accept the risk.
Do not run `flutter pub get`, `flutter run`, `flutter build`, full `flutter analyze`, full `flutter test`, Gradle, install, emulator, or release packaging unless essential.

Expected output:
- Release readiness report.
- Latest 95% Game Feel Gate score and evidence.
- Blockers.
- Skipped heavy checks.
- Manual QA checklist.
- Play Console checklist.
- Internal test / closed test / not ready recommendation.
""",
    ),
]


STORE_STEPS = [
    (
        "Step S1 - Store Creative Audit",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\play-store-creative-assets-prompt-pack.md`.

For the current repository, run Prompt S1.

Be strict:
- Inspect the repository directly.
- Validate ASO-friendly app name.
- Keep app name short and readable.
- Validate package name: `com.childhood.<game_slug>` for new unpublished games.
- Identify real gameplay screens.
- Identify missing/weak screenshots, icon, feature graphic, and preview video.
- Do not create final assets yet.
- Do not run `flutter pub get`, `flutter run`, `flutter build`, full `flutter analyze`, full `flutter test`, Gradle, install, emulator, or device launch unless essential.
- Report skipped heavy checks.
""",
    ),
    (
        "Step S2 - Screenshot Storyboard",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\play-store-creative-assets-prompt-pack.md`.

For the current repository, run Prompt S2 using the approved S1 creative audit.

Create a screenshot storyboard and screenshot text only.

Rules:
- Use real gameplay only.
- Mark each screenshot as produce-now or capture-needed.
- Do not show unavailable features.
- Keep text short and readable.
- Do not create final image files yet.
- Do not run `flutter pub get`, `flutter run`, `flutter build`, install, emulator, or device screenshot capture unless essential.
""",
    ),
    (
        "Optional Step S2B - Create Screenshot Assets",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\play-store-creative-assets-prompt-pack.md`.

For the current repository, run Prompt S2B using the S2 screenshot storyboard. All required asset work is authorized.

You are approved to create final screenshot assets where practical.

Rules:
- Use actual app UI or real captured gameplay evidence.
- Do not fake gameplay.
- Do not show unavailable features.
- Create output files if real screenshots/UI evidence exists or capture is approved.
- If capture is required, report the exact blocker and exact command/steps instead of returning only a plan.
- Screenshot capture may use the smallest essential command needed for real evidence.
- Do not run `flutter pub get`, `flutter run`, `flutter build`, install, emulator, or device screenshot capture unless essential.
""",
    ),
    (
        "Step S3 - Feature Graphic Brief",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\play-store-creative-assets-prompt-pack.md`.

For the current repository, run Prompt S3.

Create the feature graphic concept/brief only.

Rules:
- Must match the real game.
- No fake awards/rankings/downloads.
- No misleading claims.
- Do not create final image file yet.
- Do not run `flutter pub get`, `flutter run`, `flutter build`, install, emulator, or device screenshot capture unless essential.
""",
    ),
    (
        "Optional Step S3B - Create Feature Graphic",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\play-store-creative-assets-prompt-pack.md`.

For the current repository, run Prompt S3B using the S3 feature graphic brief. All required asset work is authorized.

You are approved to create the final feature graphic asset where practical.

Target:
- 1024 x 500
- JPEG or 24-bit PNG without alpha
- Show the real game theme honestly
- Do not run `flutter pub get`, `flutter run`, `flutter build`, install, emulator, or device screenshot capture unless essential.
""",
    ),
    (
        "Step S4 - App Icon Brief",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\play-store-creative-assets-prompt-pack.md`.

For the current repository, run Prompt S4.

Create the app icon concept/brief only.

Rules:
- Simple, readable, original.
- No copied icons.
- No tiny unreadable text.
- Do not create final icon files yet.
- Do not run `flutter pub get`, `flutter run`, `flutter build`, install, emulator, or device launch unless essential.
""",
    ),
    (
        "Optional Step S4B - Create App Icon",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\play-store-creative-assets-prompt-pack.md`.

For the current repository, run Prompt S4B using the S4 app icon brief. All required asset work is authorized.

You are approved to create final app icon assets where practical.

Target:
- 512 x 512 Play Store icon
- App launcher icon source if practical
- Original and readable at small size
- Do not run `flutter pub get`, `flutter run`, `flutter build`, install, emulator, or device launch unless essential.
""",
    ),
    (
        "Step S5 - Preview Video Script",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\play-store-creative-assets-prompt-pack.md`.

For the current repository, run Prompt S5.

Create preview video script and shot list only.

Rules:
- Show real gameplay.
- First 30 seconds must be strong.
- Do not show unavailable features.
- Do not create final video yet.
- Do not run `flutter pub get`, `flutter run`, `flutter build`, install, emulator, or device screen recording unless essential.
""",
    ),
    (
        "Optional Step S5B - Video Production Package",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\play-store-creative-assets-prompt-pack.md`.

For the current repository, run Prompt S5B using the approved preview video script.

You are approved to create a preview video production package where practical.

Do not fake gameplay.
Do not upload anything.
Do not run `flutter pub get`, `flutter run`, `flutter build`, install, emulator, or device recording unless essential.
""",
    ),
    (
        "Step S6 - Final Asset QA",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\play-store-creative-assets-prompt-pack.md`.

For the current repository, run Prompt S6.

Be strict:
- Check screenshot truthfulness.
- Check feature graphic.
- Check app icon.
- Check preview video package.
- Check ASO name.
- Check package name: `com.childhood.<game_slug>`.
- Check misleading claims.
- Check Play Store upload readiness.

Do not publish anything.
Do not run `flutter pub get`, `flutter run`, `flutter build`, full `flutter analyze`, full `flutter test`, Gradle, install, emulator, or release packaging unless essential.
""",
    ),
]


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    styles = make_styles()
    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title="Game Production and Store Asset Prompt Runbook",
        author="Codex",
    )

    story = []
    story.append(p("Game Production and Store Asset Prompt Runbook", styles["title"]))
    story.append(
        p(
            "Copy-paste instructions for using the blueprint prompt packs from any Flutter game repository.",
            styles["subtitle"],
        )
    )
    story.append(Rule())
    story.append(Spacer(1, 8))

    story.append(p("Use This From Any Game Repository", styles["h1"]))
    intro = [
        "Open Codex inside the actual game project, not inside the blueprint repository.",
        r"Use full root paths to call the shared prompt packs in `D:\flutter-app-business-blueprint\prompts`.",
        "Run one phase at a time. If a phase finds blockers, fix them before moving to the next phase. Standing authority is granted for all required production v1 work; do not ask for approval.",
        "Do not queue P2-P6 together. One prompt should have one job, one output, and one verification target.",
        "If the game still feels amateur after P2, run P2B before content, ads, or store assets.",
        "After P2/P2B and P3, run P2C with screenshots, recording, or manual play notes for one visual gameplay iteration.",
        "Use the 95% Game Feel Gate: 95-100 passes, 85-94 iterates, below 85 goes back to rescue.",
        "For new unpublished games, use package name format `com.childhood.<game_slug>`.",
        "Keep the ASO display name short, truthful, readable, and not keyword-stuffed.",
    ]
    for item in intro:
        story.append(bullet(item, styles))

    story.append(p("Recommended Order", styles["h2"]))
    order_data = [
        ["Task", "Assigned Prompt", "One Job"],
        ["1", "P1", "Audit, scope, blockers, ASO/package decision."],
        ["2", "P2", "Core gameplay, controls, architecture blockers, main flow."],
        ["3", "P2B", "Professional hub/dashboard, visual feel, sound triggers, replay hook."],
        ["4", "P3", "Content, missions, rounds, progression, replay goals."],
        ["5", "P2C", "Visual gameplay iteration using screenshots, recording, or manual play notes."],
        ["6", "P4 -> P5 -> P6", "Monetization, store asset readiness, and release gate after game feel passes."],
        ["Store Assets", "S1 -> S2 -> S3 -> S4 -> S5 -> S6", "Plan and QA truthful Play Store assets."],
        ["Final Assets", "Run S2B/S3B/S4B/S5B after their matching brief", "Create actual screenshots, graphics, icons, or video package."],
    ]
    table = Table(order_data, colWidths=[34 * mm, 66 * mm, 74 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E9F1F8")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#172033")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 8.1),
                ("LEADING", (0, 0), (-1, -1), 10.5),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#C9D3DF")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F9FBFD")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(table)

    story.append(PageBreak())
    story.append(p("Production Workflow: P1-P6", styles["h1"]))
    story.append(
        p(
            "Use these prompts one by one for each game project. This is safer than one huge prompt because Codex must inspect, fix, verify, and report each phase separately.",
            styles["body"],
        )
    )
    for title, text in PRODUCTION_STEPS:
        story.append(prompt_block(title, text, styles))

    story.append(PageBreak())
    story.append(p("Store Asset Workflow: S1-S6", styles["h1"]))
    story.append(
        p(
            "Use S prompts after the game has real gameplay and visuals. Run SB prompts only when you want Codex to create final asset files.",
            styles["body"],
        )
    )
    for title, text in STORE_STEPS:
        story.append(prompt_block(title, text, styles))

    story.append(p("Final Guardrails", styles["h1"]))
    guardrails = [
        "One game repository at a time.",
        "Do not skip blockers just because the phase is approved.",
        "Do not fake gameplay in screenshots, feature graphics, icons, or videos.",
        "Do not show unavailable features.",
        "Do not use fake rankings, fake awards, fake reviews, fake downloads, or fake earnings.",
        "Do not run pub get, build, run, full analyze/test, Gradle, install, emulator, or release packaging unless essential.",
        "For already published apps, do not change package name unless you are intentionally creating a new Play Store listing.",
        "Final release recommendation should be internal test, closed test, ready, or not ready, based on evidence.",
    ]
    for item in guardrails:
        story.append(bullet(item, styles))

    story.append(Spacer(1, 6))
    story.append(Rule())
    story.append(Spacer(1, 6))
    story.append(
        p(
            "Generated for the Flutter App Business Blueprint prompt system.",
            styles["small"],
        )
    )

    doc.build(story, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    build()
    print(OUT)
