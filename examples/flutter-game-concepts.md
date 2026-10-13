# Flutter Game Concepts

These names are proposed working titles. Check name uniqueness and Android package availability before release. Download figures below are the Google Play listing badges found during research on October 13, 2026; they are cumulative downloads, not active users or revenue forecasts.

## 1. Block Grove

**Working title: Block Grove**

- **Suggested Android package:** `com.childhood.blockgrove`
- **Genre:** Grid-based block placement and combo puzzle.
- **Gameplay concept:** Place differently shaped blocks on an 8×8 board and clear complete rows or columns. Alongside classic endless play, complete short garden challenges with specific clearing objectives.
- **Core gameplay loop:** Inspect three available blocks → drag and place them → clear lines and build combos → earn points or complete an objective → receive another set of blocks.
- **Why players may replay it:** Endless high-score runs, daily seeded challenges, themed boards, and objectives that reward different placement strategies.
- **Main monetization opportunity:** Optional rewarded continuation with a limited board rescue after losing; interstitials between completed runs; a paid remove-ads option.
- **Development difficulty:** **Medium.** Flutter with a grid-based board and animations. The main work is balancing block generation, implementing accurate drag previews, and making challenge levels consistently solvable.
- **Main competitor/category:** [Block Blast! — HungryStudio](https://play.google.com/store/apps/details?id=com.block.juggle), with **1B+ Google Play downloads**.
- **What makes it different:** A separate garden challenge mode adds planning objectives—for example, clear marked cells within a fixed number of placements—without changing the familiar rules of classic endless play.

## 2. Sudoku Lantern

**Working title: Sudoku Lantern**

- **Suggested Android package:** `com.childhood.sudokulantern`
- **Genre:** Classic Sudoku and guided logic puzzle.
- **Gameplay concept:** Solve Sudoku boards offline, with an optional learning mode that explains the logical reason behind a recommended move. Support Bengali and English explanations.
- **Core gameplay loop:** Choose a difficulty → inspect the board → enter numbers and pencil notes → use logical deductions or request an explanation → complete the puzzle → review progress.
- **Why players may replay it:** Verified puzzles across difficulty levels, daily challenges, personal bests, and a learning progression covering increasingly advanced solving techniques.
- **Main monetization opportunity:** Optional rewarded access to an additional detailed hint; interstitials after completed puzzles; a paid remove-ads option.
- **Development difficulty:** **Medium–High.** Flutter handles the board and interactions well. The main work is generating puzzles with exactly one solution, grading difficulty, and producing correct explanations rather than simply revealing answers.
- **Main competitor/category:** [Sudoku — Oakever Games](https://play.google.com/store/apps/details?id=easy.sudoku.puzzle.solver.free), with **100M+ Google Play downloads**.
- **What makes it different:** Hints teach the next deduction with highlighted cells and a short Bengali or English explanation. Players can practise a particular technique instead of only completing random boards.

## 3. Card Haven

**Working title: Card Haven**

- **Suggested Android package:** `com.childhood.cardhaven`
- **Genre:** Klondike Solitaire and daily card challenges.
- **Gameplay concept:** Play offline Klondike Solitaire with large, readable cards, responsive dragging, tap-to-move controls, unlimited undo, and verified solvable challenge deals.
- **Core gameplay loop:** Start a deal → uncover and arrange cards → move cards into foundations → undo or request a hint when stuck → finish the deal → compare moves and time.
- **Why players may replay it:** Draw-one and draw-three modes, daily deals, replayable deal codes, personal records, and cosmetic card collections.
- **Main monetization opportunity:** Interstitials between deals; paid remove-ads and cosmetic card packs. Basic undo and standard hints remain freely available.
- **Development difficulty:** **Medium.** Flutter with layered card widgets and animations. The main work is reliable drag handling, correct rules, useful hints, and validating the solvability of curated challenge deals.
- **Main competitor/category:** [Solitaire — MobilityWare](https://play.google.com/store/apps/details?id=com.mobilityware.solitaire), with **100M+ Google Play downloads**.
- **What makes it different:** A short “Challenge Trail” presents curated deals with optional goals, such as finishing within a move target. Shareable deal codes let friends attempt the same board without requiring online multiplayer.

## 4. Brain Wink

**Working title: Brain Wink**

- **Suggested Android package:** `com.childhood.brainwink`
- **Genre:** Interactive brain riddles and lateral-thinking puzzles.
- **Gameplay concept:** Solve illustrated puzzles through unexpected but understandable interactions: drag objects, combine items, move text, or notice something overlooked. Each puzzle is authored for both Bengali and English.
- **Core gameplay loop:** Read the prompt → inspect the scene → experiment with taps and dragging → discover the trick → see a short explanation → unlock another puzzle.
- **Why players may replay it:** New puzzle chapters, optional challenges, and alternate solutions in selected levels. Fresh content drives return visits more than replaying already-solved riddles.
- **Main monetization opportunity:** Optional rewarded progressive hints; interstitials between small groups of completed puzzles; paid remove-ads or additional chapter packs.
- **Development difficulty:** **Medium–High.** Flutter or Flame can handle scene interactions. The main work is original puzzle design, illustrations, fair clues, and making both language versions work without relying on untranslatable wordplay.
- **Main competitor/category:** [Brain Test: Tricky Puzzles — Unico Studio](https://play.google.com/store/apps/details?id=com.unicostudio.braintest), with **100M+ Google Play downloads**.
- **What makes it different:** Original scenes inspired by everyday situations—tea stalls, classrooms, markets, and household tasks—with explanations that make the solution feel discoverable rather than arbitrary.

## 5. Color Courtyard

**Working title: Color Courtyard**

- **Suggested Android package:** `com.childhood.colorcourtyard`
- **Genre:** Relaxing color-by-number and digital coloring.
- **Gameplay concept:** Complete numbered illustrations featuring original mandalas, nature, village courtyards, boats, and Bangladeshi seasonal scenes. Offer a separate free-color mode for choosing personal palettes.
- **Core gameplay loop:** Choose an illustration → select a numbered color → tap matching regions → complete the artwork → save or share it → unlock another collection.
- **Why players may replay it:** New artwork collections, daily pictures, saved unfinished projects, and alternate palettes in free-color mode.
- **Main monetization opportunity:** Optional rewarded region-finder hints or access to selected bonus pictures; interstitials after completed artwork; paid collection packs and remove-ads.
- **Development difficulty:** **Medium–High.** Flutter with vector paths or region masks. The main work is preparing artwork, accurate region hit-testing, handling tiny areas, and keeping zooming and panning smooth.
- **Main competitor/category:** [Happy Color — X-FLOW](https://play.google.com/store/apps/details?id=com.pixel.art.coloring.color.number), with **100M+ Google Play downloads**.
- **What makes it different:** A coherent collection of original Bengali cultural and seasonal artwork, paired with both guided color-by-number and creative free-color modes.
