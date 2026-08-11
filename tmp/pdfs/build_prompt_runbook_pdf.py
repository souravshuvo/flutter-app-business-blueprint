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
- Weak UI polish.
- Missing save/progress.
- Missing AdMob/analytics.
- Missing ASO-friendly app name.
- Missing package name convention: `com.childhood.<game_slug>`.
- Release blockers.

Do not edit files yet.

Expected output:
- Production v1 checklist.
- Blockers.
- Approved implementation order.
""",
    ),
    (
        "Step P2 - UI + Gameplay Polish",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\game-production-ready-prompt-pack.md`.

All P1 production v1 scope items are approved.

For the current repository, run Prompt P2.

You are approved to modify code/docs for UI and gameplay polish only.

Fix:
- Architecture mismatch if it blocks game correctness.
- Broken/incomplete core gameplay.
- Placeholder/fake behavior.
- Missing menus, pause/restart, result screens, settings.
- Weak mobile UI and feedback.

Do not add AdMob yet.
Do not touch unrelated files.
Do not run heavy build/install/emulator unless essential.
""",
    ),
    (
        "Step P3 - Levels / Content / Modes",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\game-production-ready-prompt-pack.md`.

For the current repository, run Prompt P3 using the approved production content target.

You are approved to add enough production v1 content.

Add or complete:
- Levels, missions, waves, boards, puzzles, modes, AI modes, or progression.
- Save/progress where needed.
- Validation/tests for game rules where practical.

Do not add AdMob yet.
Do not touch unrelated files.
Do not run heavy build/install/emulator unless essential.
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
- Feature graphic brief.
- App icon brief.
- Preview video script.

Do not fake gameplay.
Do not show unavailable features.
""",
    ),
    (
        "Step P6 - Final Release Check",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\game-production-ready-prompt-pack.md`.

For the current repository, run Prompt P6.

Be strict. Do not claim production-ready unless checks support it.

Expected output:
- Release readiness report.
- Blockers.
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
- Validate package name: `com.childhood.<game_slug>` for new unpublished games.
- Identify real gameplay screens.
- Identify missing/weak screenshots, icon, feature graphic, and preview video.
- Do not create final assets yet.
- Do not run build/install/emulator unless essential.
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
- Do not show unavailable features.
- Keep text short and readable.
- Do not create final image files yet.
""",
    ),
    (
        "Optional Step S2B - Create Screenshot Assets",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\play-store-creative-assets-prompt-pack.md`.

For the current repository, run Prompt S2B using the approved screenshot storyboard.

You are approved to create final screenshot assets where practical.

Rules:
- Use actual app UI or real captured gameplay evidence.
- Do not fake gameplay.
- Do not show unavailable features.
- Do not run emulator/device unless essential and approved.
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
""",
    ),
    (
        "Optional Step S3B - Create Feature Graphic",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\play-store-creative-assets-prompt-pack.md`.

For the current repository, run Prompt S3B using the approved feature graphic brief.

You are approved to create the final feature graphic asset where practical.

Target:
- 1024 x 500
- JPEG or 24-bit PNG without alpha
- Show the real game theme honestly
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
""",
    ),
    (
        "Optional Step S4B - Create App Icon",
        r"""
Use the prompt pack at `D:\flutter-app-business-blueprint\prompts\play-store-creative-assets-prompt-pack.md`.

For the current repository, run Prompt S4B using the approved app icon brief.

You are approved to create final app icon assets where practical.

Target:
- 512 x 512 Play Store icon
- App launcher icon source if practical
- Original and readable at small size
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
        "Run one phase at a time. If a phase finds blockers, fix them before moving to the next phase.",
        "For new unpublished games, use package name format `com.childhood.<game_slug>`.",
        "Keep the ASO display name truthful, readable, and not keyword-stuffed.",
    ]
    for item in intro:
        story.append(bullet(item, styles))

    story.append(p("Recommended Order", styles["h2"]))
    order_data = [
        ["Workflow", "Run Order", "Purpose"],
        ["Production", "P1 -> P2 -> P3 -> P4 -> P5 -> P6", "Turn a game repo into production-ready v1."],
        ["Store Assets", "S1 -> S2 -> S3 -> S4 -> S5 -> S6", "Plan and QA truthful Play Store assets."],
        ["Final Assets", "Add S2B/S3B/S4B/S5B when approved", "Create actual screenshots, graphics, icons, or video package."],
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
        "Do not run heavy build, install, emulator, or release packaging unless essential.",
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
