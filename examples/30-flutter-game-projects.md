# 30 Flutter Game Projects

Compiled: 2026-10-01

This catalog brings together the original three batches of 10 game concepts from our discussion, in the same order. Each entry includes the original concept details and a suggested Android package name. Use it to choose and brief one game at a time.

Competitor links and cumulative download bands are preserved from the original research discussion; they were not reverified during this export. They are category references, not forecasts of a new game's downloads or revenue.

## How to use

1. Pick one project below. Copy its **Working title** and concept fields into the [Universal Flutter Game Prompt Builder](../output/prompt-copy/game-production-store-prompt-copy.html). Use **New game / Clear fields** before starting a different game.
2. Supply that game's own AdMob App ID and ad unit IDs in the builder. The package names below are for new, unpublished apps; preserve an existing published app's ID.
3. Send the generated Master prompt in that game's repository. Codex first creates or updates `docs/GAME_PLAN.md`; use **Continue** for subsequent phases and **Focus** for a specific area. Run the requested Flutter checks manually and provide results.

These are concept briefs, not completed PRDs or built games. The shared scope is offline core gameplay, local progress, manageable visuals, and no required multiplayer backend. Rewards must fit the game: hints and bonuses do not require inventing a life system.

## Project index

| # | Project | Development difficulty | Suggested Android package |
| --- | --- | --- | --- |
| 1 | [Parcel Perfect](#1-parcel-perfect) | Medium | `com.childhood.parcelperfect` |
| 2 | [Switchyard Minute](#2-switchyard-minute) | Medium | `com.childhood.switchyardminute` |
| 3 | [Bolt & Balance](#3-bolt--balance) | Medium-high | `com.childhood.boltbalance` |
| 4 | [Pocket Pinball Expedition](#4-pocket-pinball-expedition) | Medium-high | `com.childhood.pocketpinballexpedition` |
| 5 | [Twin Tower Drop](#5-twin-tower-drop) | Low-medium | `com.childhood.twintowerdrop` |
| 6 | [Tiny Conveyor Works](#6-tiny-conveyor-works) | Medium | `com.childhood.tinyconveyorworks` |
| 7 | [Night Market Minute](#7-night-market-minute) | Medium | `com.childhood.nightmarketminute` |
| 8 | [Pocket Habitat](#8-pocket-habitat) | Medium | `com.childhood.pockethabitat` |
| 9 | [The Room Changed](#9-the-room-changed) | Medium | `com.childhood.theroomchanged` |
| 10 | [Sum Foundry](#10-sum-foundry) | Low-medium | `com.childhood.sumfoundry` |
| 11 | [Cable Garden](#11-cable-garden) | Medium | `com.childhood.cablegarden` |
| 12 | [Lighthouse Relay](#12-lighthouse-relay) | Low-medium | `com.childhood.lighthouserelay` |
| 13 | [Fold & Stamp](#13-fold--stamp) | Medium | `com.childhood.foldstamp` |
| 14 | [Three-Shot Golf](#14-three-shot-golf) | Medium | `com.childhood.threeshotgolf` |
| 15 | [Domino Detour](#15-domino-detour) | Medium | `com.childhood.dominodetour` |
| 16 | [Lift Rush](#16-lift-rush) | Medium | `com.childhood.liftrush` |
| 17 | [Word Trail Expedition](#17-word-trail-expedition) | Medium | `com.childhood.wordtrailexpedition` |
| 18 | [Trail Solitaire](#18-trail-solitaire) | Low-medium | `com.childhood.trailsolitaire` |
| 19 | [Tidewalk](#19-tidewalk) | Medium | `com.childhood.tidewalk` |
| 20 | [Pocket Percussion](#20-pocket-percussion) | Medium-high | `com.childhood.pocketpercussion` |
| 21 | [Lantern Defense](#21-lantern-defense) | Medium | `com.childhood.lanterndefense` |
| 22 | [Pocket Depths](#22-pocket-depths) | Medium | `com.childhood.pocketdepths` |
| 23 | [Relic Sweep](#23-relic-sweep) | Medium-high | `com.childhood.relicsweep` |
| 24 | [Stencil Studio](#24-stencil-studio) | Low-medium | `com.childhood.stencilstudio` |
| 25 | [Loop Crew](#25-loop-crew) | Medium | `com.childhood.loopcrew` |
| 26 | [Magnet Warehouse](#26-magnet-warehouse) | Medium | `com.childhood.magnetwarehouse` |
| 27 | [Pocket Drift Circuit](#27-pocket-drift-circuit) | Medium-high | `com.childhood.pocketdriftcircuit` |
| 28 | [Carve the Shape](#28-carve-the-shape) | Medium | `com.childhood.carvetheshape` |
| 29 | [Meadow Claim](#29-meadow-claim) | Medium | `com.childhood.meadowclaim` |
| 30 | [Bridge Relay](#30-bridge-relay) | Medium-high | `com.childhood.bridgerelay` |

## 1. Parcel Perfect

**Working title: Parcel Perfect**

- **Suggested Android package:** `com.childhood.parcelperfect`
- **Genre:** Spatial packing and planning puzzle.
- **Gameplay concept:** Pack a delivery van so every parcel fits and can be removed through its loading door in the required delivery order.
- **Core gameplay loop:** Inspect shapes and delivery order -> rotate and place parcels -> simulate unloading -> revise or complete -> unlock another delivery.
- **Why players may replay it:** Different parcel sets, van layouts, and unloading sequences; replay for fewer rearrangements or better space efficiency.
- **Main monetization opportunity:** Optional rewarded placement hint after a failed attempt; interstitials between delivery batches.
- **Development difficulty:** **Medium.** Flutter with a grid-based board; the main work is validating packing solutions and unobstructed removal paths.
- **Main competitor/category:** Packing puzzles such as [Pack Master](https://apps.apple.com/gb/app/pack-master/id1457690430), available on the App Store; its [Google Play listing](https://play.google.com/store/apps/details?hl=fr&id=com.dmg.packmaster) shows **1M+ downloads**.
- **What makes it different:** Delivery order makes accessibility part of the puzzle: a tightly packed van can still be an incorrect solution.

## 2. Switchyard Minute

**Working title: Switchyard Minute**

- **Suggested Android package:** `com.childhood.switchyardminute`
- **Genre:** Railway routing and timing puzzle.
- **Gameplay concept:** Operate a tiny railway junction by switching tracks and timing departures to deliver a short train schedule without collisions.
- **Core gameplay loop:** Read the incoming schedule -> set junctions -> release trains -> manage crossings -> receive an efficiency score -> attempt another timetable.
- **Why players may replay it:** Reusable track layouts support different schedules, train speeds, and platform assignments; players can improve delays and perfect runs.
- **Main monetization opportunity:** Optional rewarded demonstration of one troublesome crossing after failure; interstitials between completed timetables.
- **Development difficulty:** **Medium.** Flame for movement, backed by discrete track and occupancy rules; timing clarity and fair collision detection are the main risks.
- **Main competitor/category:** [Train Conductor World](https://play.google.com/store/apps/details?id=com.thevoxelagents.tc3), with **10M+ Google Play downloads**.
- **What makes it different:** Compact, previewable timetable challenges make planning and dispatch efficiency the central progression system.

## 3. Bolt & Balance

**Working title: Bolt & Balance**

- **Suggested Android package:** `com.childhood.boltbalance`
- **Genre:** Mechanical physics puzzle.
- **Gameplay concept:** Remove marked bolts and support plates while keeping a fragile cargo box safely balanced on its destination platform.
- **Core gameplay loop:** Inspect supports -> predict movement -> remove a bolt -> let the structure settle -> preserve the cargo -> complete the dismantling.
- **Why players may replay it:** Different support arrangements, moving hinges, and removal orders; replay for fewer moves and clean solutions.
- **Main monetization opportunity:** Optional rewarded rewind to the previous settled state after failure.
- **Development difficulty:** **Medium-high.** Flame with Forge2D; stable physics, clear failure rules, and reproducible level solutions require careful testing.
- **Main competitor/category:** [Wood Nuts & Bolts Puzzle](https://play.google.com/store/apps/details?id=com.wood.nut.and.bolts.puzzle), with **50M+ Google Play downloads**; the broader screw-puzzle category has current market evidence.
- **What makes it different:** The player must preserve a load while dismantling its supports, creating a balance objective beyond clearing every plate.

## 4. Pocket Pinball Expedition

**Working title: Pocket Pinball Expedition**

- **Suggested Android package:** `com.childhood.pocketpinballexpedition`
- **Genre:** Arcade pinball with short-run upgrade choices.
- **Gameplay concept:** Use two flippers to complete a sequence of small pinball rooms, choosing a modifier between rooms that changes how the next table plays.
- **Core gameplay loop:** Launch ball -> hit room objectives -> open exit -> choose modifier -> enter next room -> finish expedition or retry.
- **Why players may replay it:** Flipper mastery, alternate room sequences, modifier combinations, and personal-best runs.
- **Main monetization opportunity:** One optional rewarded extra ball after the final drain; assisted runs recorded separately from unassisted records.
- **Development difficulty:** **Medium-high.** Flame with Forge2D; ball feel, flipper responsiveness, and preventing stuck-ball states dominate the work.
- **Main competitor/category:** [PinOut](https://play.google.com/store/apps/details?id=com.mediocre.pinout), with **10M+ Google Play downloads**. This demonstrates established pinball interest, not verified 2026 growth.
- **What makes it different:** Small reusable room modules and meaningful between-room choices produce varied expeditions without a large RPG content system.

## 5. Twin Tower Drop

**Working title: Twin Tower Drop**

- **Suggested Android package:** `com.childhood.twintowerdrop`
- **Genre:** One-touch precision arcade.
- **Gameplay concept:** Choose which of two towers receives each moving block, balancing tower heights so periodic bridge pieces can connect them.
- **Core gameplay loop:** Assess both towers -> choose landing side -> time the drop -> lose unsupported overhang -> complete bridges -> chase a higher score.
- **Why players may replay it:** Quick retries, timing mastery, changing block widths, and decisions about which tower needs the next piece.
- **Main monetization opportunity:** One optional rewarded recovery after a failed drop; interstitials after several completed runs.
- **Development difficulty:** **Low-medium.** Flame with deterministic overlap calculations; full rigid-body physics is unnecessary.
- **Main competitor/category:** [Stack by Ketchapp](https://apps.apple.com/us/app/stack/id1080487957?platform=ipad), an established App Store stacking game.
- **What makes it different:** Players manage two interdependent structures and bridge opportunities, adding planning to the familiar timing action.

## 6. Tiny Conveyor Works

**Working title: Tiny Conveyor Works**

- **Suggested Android package:** `com.childhood.tinyconveyorworks`
- **Genre:** Compact automation puzzle.
- **Gameplay concept:** Arrange conveyors and a small set of processing machines to manufacture a requested item within a fixed floor space.
- **Core gameplay loop:** Read order -> place machines and belts -> run the factory -> locate bottlenecks -> revise -> complete the contract.
- **Why players may replay it:** Multiple valid layouts, efficiency medals, tighter machine budgets, and new combinations of familiar processing rules.
- **Main monetization opportunity:** Interstitials between completed contracts; optional rewarded hints that identify a bottleneck.
- **Development difficulty:** **Medium.** Flutter board editing with Flame animation if useful; use a discrete simulation to simplify transport and processing.
- **Main competitor/category:** Factory automation games such as [Sandship: Crafting Factory](https://apps.apple.com/us/app/sandship-crafting-factory/id1440385758). This is an established niche reference, not evidence of mass-market growth.
- **What makes it different:** Each small factory is a self-contained puzzle with a clear finish, supporting brief sessions and efficient level production.

## 7. Night Market Minute

**Working title: Night Market Minute**

- **Suggested Android package:** `com.childhood.nightmarketminute`
- **Genre:** Time-management cooking.
- **Gameplay concept:** Choose a three-item menu, then operate a compact street-food stall through a 90-second rush where recipes compete for shared equipment.
- **Core gameplay loop:** Select menu -> prepare ingredients -> manage shared stations -> serve orders -> collect tips -> adjust the next shift's strategy.
- **Why players may replay it:** Different customer sequences, menu combinations, station priorities, and personal-best service streaks.
- **Main monetization opportunity:** Optional rewarded doubling of cosmetic tip rewards after a shift.
- **Development difficulty:** **Medium.** Flame or Flutter animations; recipe-state handling, touch responsiveness, and balancing workload are the main challenges.
- **Main competitor/category:** [Cooking Fever](https://play.google.com/store/apps/details?hl=en&id=com.nordcurrent.canteenhd), with **100M+ Google Play downloads**.
- **What makes it different:** Menu selection changes equipment contention before each short shift; a distinctive regional street-food identity can support the presentation.

## 8. Pocket Habitat

**Working title: Pocket Habitat**

- **Suggested Android package:** `com.childhood.pockethabitat`
- **Genre:** Cozy tile-placement strategy puzzle.
- **Gameplay concept:** Build a small wildlife habitat by placing terrain tiles so animals receive the combinations of water, shelter, and open space they need.
- **Core gameplay loop:** Choose a terrain tile -> place or rotate it -> satisfy habitat conditions -> attract animals -> complete the limited-tile board -> score the ecosystem.
- **Why players may replay it:** Different tile sequences, animal objectives, competing adjacency requirements, and daily boards.
- **Main monetization opportunity:** Optional rewarded extra tile choice in casual mode; daily challenge scores use a fixed, unassisted ruleset.
- **Development difficulty:** **Medium.** Flutter grid or hex rendering; transparent scoring and interesting tile distributions matter more than animation complexity.
- **Main competitor/category:** Relaxing landscape-placement games such as [Land Builder](https://apps.apple.com/us/app/land-builder/id6443774303).
- **What makes it different:** Small completed ecosystems have explicit animal needs and trade-offs, giving each board a measurable objective and ending.

## 9. The Room Changed

**Working title: The Room Changed**

- **Suggested Android package:** `com.childhood.theroomchanged`
- **Genre:** Observation and visual-memory puzzle.
- **Gameplay concept:** Inspect a small illustrated room, then identify objects that moved, vanished, or changed while the lights were out.
- **Core gameplay loop:** Observe room -> experience transition -> identify changes -> receive accuracy score -> try a new arrangement.
- **Why players may replay it:** Authored objects can support many validated change combinations; players improve accuracy and tackle additional change types.
- **Main monetization opportunity:** Optional rewarded replay of the original room when stuck.
- **Development difficulty:** **Medium**, with **higher artwork effort** than the abstract puzzles. Flutter is sufficient; readable changes and reliable object placement require QA.
- **Main competitor/category:** Observation games such as [Find Out: Find Hidden Objects](https://play.google.com/store/apps/details?hl=en&id=com.find.out.hidden.objects), with **50M+ Google Play downloads**.
- **What makes it different:** The challenge concerns changes to a previously observed scene, allowing compact rooms and reusable objects to drive replay.

## 10. Sum Foundry

**Working title: Sum Foundry**

- **Suggested Android package:** `com.childhood.sumfoundry`
- **Genre:** Number-placement logic puzzle.
- **Gameplay concept:** Place numbered chips on a small board so every row and column reaches its displayed target total.
- **Core gameplay loop:** Inspect targets and available chips -> choose placements -> resolve intersecting constraints -> finish the board -> attempt another puzzle.
- **Why players may replay it:** Solvable generated boards, different chip sets, optional move-efficiency goals, and a daily puzzle.
- **Main monetization opportunity:** Optional rewarded explanation of one forced placement; interstitials between puzzle sets.
- **Development difficulty:** **Low-medium.** Flutter alone; the important work is a generator and solver that validate boards and produce useful hints.
- **Main competitor/category:** Number logic games such as [Number Match](https://play.google.com/store/apps/details?hl=en_US&id=com.easybrain.number.puzzle.game), with **50M+ Google Play downloads**.
- **What makes it different:** Players construct intersecting target sums through placement, creating a different decision process from removing matching number pairs.

## 11. Cable Garden

**Working title: Cable Garden**

- **Suggested Android package:** `com.childhood.cablegarden`
- **Genre:** Untangling and spatial logic.
- **Gameplay concept:** Move connected garden lights between mounting points until their cables stop crossing, while respecting fixed anchors and cable-length limits.
- **Core gameplay loop:** Inspect crossings -> move a light -> resolve cable conflicts -> illuminate the completed arrangement -> unlock another layout.
- **Why players may replay it:** Different anchor layouts, minimum-move challenges, and daily puzzles generated from valid arrangements.
- **Main monetization opportunity:** Optional rewarded hint identifying a useful mounting point.
- **Development difficulty:** **Medium.** Flutter CustomPainter; use line-intersection and distance rules rather than simulated rope physics.
- **Main competitor/category:** [Tangle Master 3D](https://play.google.com/store/apps/details/?hl=en-US&id=com.rollic.tanglemaster3D), with **100M+ downloads**.
- **What makes it different:** Fixed anchors and cable reach create a network-planning puzzle with an instantly visible completion reward.

## 12. Lighthouse Relay

**Working title: Lighthouse Relay**

- **Suggested Android package:** `com.childhood.lighthouserelay`
- **Genre:** Light-routing logic puzzle.
- **Gameplay concept:** Rotate mirrors and position limited beam splitters to illuminate every lighthouse while keeping beams away from forbidden receivers.
- **Core gameplay loop:** Inspect emitters and targets -> arrange optical pieces -> trace beams -> fix conflicts -> activate the coastline.
- **Why players may replay it:** Multiple solutions, limited-piece challenges, and combinations of mirrors, shutters, and splitters.
- **Main monetization opportunity:** Optional rewarded placement hint; capped interstitials between completed puzzle sets.
- **Development difficulty:** **Low-medium.** Flutter with discrete beam tracing; detecting beam loops and validating solutions are the main technical tasks.
- **Main competitor/category:** [Laser: Relaxing and Satisfying](https://play.google.com/store/apps/details?id=com.tapanywhere.laseroverload), the listing associated with Laser Overload.
- **What makes it different:** Lighting required targets while avoiding forbidden ones introduces trade-offs beyond simply connecting every receiver.

## 13. Fold & Stamp

**Working title: Fold & Stamp**

- **Suggested Android package:** `com.childhood.foldstamp`
- **Genre:** Paper-folding and symmetry puzzle.
- **Gameplay concept:** Fold a sheet along marked creases, stamp through its layers, then unfold it to reproduce a target pattern.
- **Core gameplay loop:** Examine target -> choose folds -> position stamp -> unfold -> compare result -> revise or advance.
- **Why players may replay it:** Different crease sequences and stamp positions; optional challenges using fewer folds or stamps.
- **Main monetization opportunity:** Optional rewarded preview of the unfolded result before committing a stamp.
- **Development difficulty:** **Medium.** Flutter canvas and transforms; constrain folds to a grid and predefined creases to keep geometry manageable.
- **Main competitor/category:** [Paper Fold](https://play.google.com/store/apps/details?hl=en&id=com.game.foldpuzzle), with **100M+ downloads**.
- **What makes it different:** The player predicts how a mark repeats across folded layers, creating a symmetry puzzle rather than only revealing an illustration.

## 14. Three-Shot Golf

**Working title: Three-Shot Golf**

- **Suggested Android package:** `com.childhood.threeshotgolf`
- **Genre:** Mini-golf physics puzzle.
- **Gameplay concept:** Complete tiny courses within three shots, choosing where to place one movable bumper before taking the first stroke.
- **Core gameplay loop:** Inspect course -> place bumper -> aim and shoot -> adjust remaining shots -> finish -> improve the solution.
- **Why players may replay it:** Better shot counts, alternative bumper positions, daily courses, and mastery of bank shots.
- **Main monetization opportunity:** Optional rewarded extra practice shot after failure; assisted completions do not earn perfect-score medals.
- **Development difficulty:** **Medium.** Flame with simple circle collisions or Forge2D; consistent aiming, friction, and ball settling need tuning.
- **Main competitor/category:** Compact golf puzzles such as [Golf Peaks](https://apps.apple.com/us/app/golf-peaks/id1419542293?platform=ipad). It is a premium puzzle reference, not evidence for an ad-funded business.
- **What makes it different:** Players alter the course before playing, combining a small construction decision with shot execution.

## 15. Domino Detour

**Working title: Domino Detour**

- **Suggested Android package:** `com.childhood.dominodetour`
- **Genre:** Chain-reaction construction puzzle.
- **Gameplay concept:** Fill gaps in an incomplete domino course using a limited set of pieces so one push reaches every finish bell.
- **Core gameplay loop:** Inspect broken chain -> place missing pieces -> trigger first domino -> observe the failure or finish -> revise.
- **Why players may replay it:** Alternate routes, branching chains, limited-piece solutions, and the satisfaction of watching a successful sequence.
- **Main monetization opportunity:** Optional rewarded hint highlighting the first broken connection.
- **Development difficulty:** **Medium.** Flame with predefined topple interactions; avoid unrestricted 3D physics and arbitrary object placement.
- **Main competitor/category:** Chain-reaction games such as [Domino Smash](https://apps.apple.com/us/app/domino-smash/id1471607741).
- **What makes it different:** The challenge is constructing the missing connections and timing branches so multiple targets can be reached from one push.

## 16. Lift Rush

**Working title: Lift Rush**

- **Suggested Android package:** `com.childhood.liftrush`
- **Genre:** Elevator scheduling and time management.
- **Gameplay concept:** Operate two small elevators during a short building rush, grouping passengers by destination while managing capacity and waiting time.
- **Core gameplay loop:** Read queues -> assign elevator stops -> group passengers -> complete deliveries -> score the shift -> try a new rush pattern.
- **Why players may replay it:** Changing arrival patterns, express-floor restrictions, different capacities, and improving average waiting time.
- **Main monetization opportunity:** Optional rewarded doubling of cosmetic earnings after a shift.
- **Development difficulty:** **Medium.** Flutter or Flame; passenger queues, elevator state machines, and readable controls are the main work.
- **Main competitor/category:** Elevator and tower-management games; [Tiny Tower](https://apps.apple.com/us/app/tiny-tower-tap-idle-evolution/id422667065) is an adjacent reference rather than a direct mechanical match.
- **What makes it different:** Short dispatch challenges make elevator efficiency the entire game, with progression through new scheduling constraints.

## 17. Word Trail Expedition

**Working title: Word Trail Expedition**

- **Suggested Android package:** `com.childhood.wordtrailexpedition`
- **Genre:** Word search with route planning.
- **Gameplay concept:** Trace words through adjacent letter tiles to move an explorer across a small map and reach required checkpoints.
- **Core gameplay loop:** Inspect letters and checkpoints -> find a valid word -> travel along its tiles -> plan the next word -> reach the exit.
- **Why players may replay it:** Different letter boards, route-length goals, alternate word choices, and daily expeditions.
- **Main monetization opportunity:** Optional rewarded reveal of the first letters of a viable route word.
- **Development difficulty:** **Medium.** Flutter; dictionary licensing, word quality, and generating reachable boards are more demanding than the interface.
- **Main competitor/category:** [Wordscapes Search](https://play.google.com/store/apps/details?id=com.peoplefun.wordsearch), with **10M+ downloads**, and the broader word-puzzle category.
- **What makes it different:** A word's ending position affects the next move, so vocabulary and navigation must work together.

## 18. Trail Solitaire

**Working title: Trail Solitaire**

- **Suggested Android package:** `com.childhood.trailsolitaire`
- **Genre:** Solitaire and light route strategy.
- **Gameplay concept:** Clear cards one rank above or below your current card while choosing branches through a compact expedition map.
- **Core gameplay loop:** Inspect exposed cards -> clear a sequence -> choose a branch -> manage the remaining draw pile -> reach camp.
- **Why players may replay it:** Seeded deals, different branching layouts, optional objectives, and better use of a limited draw pile.
- **Main monetization opportunity:** One optional rewarded reserve draw when stuck; unlimited free restarts remain available.
- **Development difficulty:** **Low-medium.** Flutter; solvable-deal generation and balancing the draw pile are the key challenges.
- **Main competitor/category:** TriPeaks games such as [Solitaire Grand Harvest](https://play.google.com/store/apps/details?hl=en_US&id=net.supertreat.solitaire), with **50M+ downloads**.
- **What makes it different:** Visible route branches create decisions about which card sequences to pursue, within a short expedition with a clear ending.

## 19. Tidewalk

**Working title: Tidewalk**

- **Suggested Android package:** `com.childhood.tidewalk`
- **Genre:** Turn-based environmental puzzle.
- **Gameplay concept:** Cross a small island board where each step advances a predictable tide cycle, exposing or flooding different paths.
- **Core gameplay loop:** Read terrain and tide forecast -> move or wait -> update water level -> collect supplies -> reach the boat.
- **Why players may replay it:** Different island layouts, shorter-route challenges, optional pickups, and later mechanics such as floating platforms.
- **Main monetization opportunity:** Optional rewarded hint explaining a safe move and its timing.
- **Development difficulty:** **Medium.** Flutter with tile-based state transitions; the solver must account for position and tide phase.
- **Main competitor/category:** Turn-based environmental puzzles such as [Lara Croft GO](https://apps.apple.com/us/app/lara-croft-go/id971304016), a premium category reference.
- **What makes it different:** Waiting changes the available terrain, making the timing of each move as important as its direction.

## 20. Pocket Percussion

**Working title: Pocket Percussion**

- **Suggested Android package:** `com.childhood.pocketpercussion`
- **Genre:** Rhythm and pattern-memory arcade.
- **Gameplay concept:** Listen to a short two-drum phrase, reproduce it, then adapt when the next round adds a beat, changes tempo, or swaps the drum order.
- **Core gameplay loop:** Hear pattern -> repeat taps -> receive timing feedback -> add a variation -> continue the session.
- **Why players may replay it:** Accuracy improvement, progressively longer phrases, curated pattern combinations, and unlockable instrument sounds.
- **Main monetization opportunity:** Optional rewarded doubling of instrument-unlock progress after a completed session.
- **Development difficulty:** **Medium-high.** Flutter or Flame with audio-clock-based timing; device latency and calibration are the main risks. Original percussion samples keep music scope manageable.
- **Main competitor/category:** Compact rhythm challenges such as [A Dance of Fire and Ice](https://apps.apple.com/us/app/a-dance-of-fire-and-ice/id1456547302), a premium reference.
- **What makes it different:** Short call-and-response phrases combine listening, memory, and timing without requiring a large catalog of full songs.

## 21. Lantern Defense

**Working title: Lantern Defense**

- **Suggested Android package:** `com.childhood.lanterndefense`
- **Genre:** Compact tower defense.
- **Gameplay concept:** Defend a campsite through five short enemy waves using three lantern towers that you can reposition between waves.
- **Core gameplay loop:** Inspect incoming wave -> position lanterns -> defend -> choose an upgrade -> reposition -> survive the next wave.
- **Why players may replay it:** Different enemy sequences, tower combinations, map layouts, and limited-resource challenges.
- **Main monetization opportunity:** Optional rewarded doubling of cosmetic tokens after a completed run.
- **Development difficulty:** **Medium.** Flame with fixed enemy paths; balancing tower roles and enemy interactions is the main workload.
- **Main competitor/category:** [Bloons TD 6](https://play.google.com/store/apps/details?id=com.ninjakiwi.bloonstd6), with **5M+ Google Play downloads**, demonstrates established tower-defense demand.
- **What makes it different:** A small, movable defense makes repositioning between waves the central decision, keeping runs short and the upgrade system manageable.

## 22. Pocket Depths

**Working title: Pocket Depths**

- **Suggested Android package:** `com.childhood.pocketdepths`
- **Genre:** Fishing skill arcade.
- **Gameplay concept:** Steer a fishing line through underwater obstacles, choose a catch, then manage line tension while bringing it to the surface.
- **Core gameplay loop:** Choose depth -> guide lure -> hook a fish -> balance tension -> land catch -> complete collection objectives.
- **Why players may replay it:** Different fish movement patterns, depth zones, collection goals, and personal records for difficult catches.
- **Main monetization opportunity:** Optional rewarded bonus collection tokens after a successful catch.
- **Development difficulty:** **Medium.** Flame; fish movement, touch controls, and a readable tension mechanic matter more than realistic water physics.
- **Main competitor/category:** Arcade fishing games such as [Ridiculous Fishing](https://apps.apple.com/us/app/ridiculous-fishing-a-tale-of-redemption/id601831815?platform=ipad), a premium category reference.
- **What makes it different:** Each attempt combines careful descent with a different retrieval challenge; selecting a catch creates a visible risk-reward decision.

## 23. Relic Sweep

**Working title: Relic Sweep**

- **Suggested Android package:** `com.childhood.relicsweep`
- **Genre:** Deduction and excavation puzzle.
- **Gameplay concept:** Use numerical clues to excavate a connected route to buried relics while avoiding unstable ground.
- **Core gameplay loop:** Read revealed clues -> mark hazards -> excavate a safe adjacent tile -> reach relics -> exit the dig.
- **Why players may replay it:** Solver-validated boards, alternate safe routes, optional relics, and daily excavation challenges.
- **Main monetization opportunity:** Optional rewarded explanation of one logically safe move.
- **Development difficulty:** **Medium-high.** Flutter handles the board easily; generating connected, solvable boards without forced guessing is the demanding part.
- **Main competitor/category:** [Minesweeper GO](https://play.google.com/store/apps/details?hl=en_CA&id=com.EvolveGames.MinesweeperGo), with **1M+ downloads**.
- **What makes it different:** Players pursue a connected excavation route and specific objectives, giving deduction a spatial planning component.

## 24. Stencil Studio

**Working title: Stencil Studio**

- **Suggested Android package:** `com.childhood.stencilstudio`
- **Genre:** Layering and visual logic puzzle.
- **Gameplay concept:** Reproduce a target poster by choosing the order, rotation, and placement of reusable stencils and paint layers.
- **Core gameplay loop:** Inspect target -> select stencil -> position and paint -> apply another layer -> compare -> finish the poster.
- **Why players may replay it:** Different stencil combinations, multiple solutions, fewer-paint-pass challenges, and themed poster collections.
- **Main monetization opportunity:** Optional rewarded hint identifying the next useful stencil or layer.
- **Development difficulty:** **Low-medium.** Flutter canvas with grid-based masks; puzzle design is harder than rendering.
- **Main competitor/category:** Paint-order puzzles such as [Factory Balls Go!](https://play.google.com/store/apps/details?id=air.com.bartbonte.factoryballsgo).
- **What makes it different:** Reusing and rotating a small stencil set creates overlapping patterns, with layer order determining which shapes remain visible.

## 25. Loop Crew

**Working title: Loop Crew**

- **Suggested Android package:** `com.childhood.loopcrew`
- **Genre:** Cooperative time-loop puzzle for one player.
- **Gameplay concept:** Record one robot's short movement sequence, then control a second robot while the first repeats its actions to operate switches and deliver a package.
- **Core gameplay loop:** Plan room -> record first robot -> replay alongside second robot -> coordinate switches -> deliver package.
- **Why players may replay it:** Shorter solutions, optional deliveries, and new combinations of doors, pressure plates, and waiting points.
- **Main monetization opportunity:** Optional rewarded coordination hint; undo and re-recording remain free.
- **Development difficulty:** **Medium.** Flutter or Flame with discrete turns; deterministic replay and simultaneous-action rules need careful design.
- **Main competitor/category:** Temporal coordination games; [Does not Commute](https://play.google.com/store/apps/details?hl=en&id=com.mediocre.commute) is an adjacent reference with **10M+ downloads**.
- **What makes it different:** Previous actions become a cooperative partner that the player deliberately programs through ordinary movement.

## 26. Magnet Warehouse

**Working title: Magnet Warehouse**

- **Suggested Android package:** `com.childhood.magnetwarehouse`
- **Genre:** Box-moving logic puzzle.
- **Gameplay concept:** Guide a magnetic robot through a warehouse, using directional attraction and repulsion to move metal crates onto loading pads.
- **Core gameplay loop:** Inspect crate positions -> move robot -> choose push or pull pulse -> reposition cargo -> complete the warehouse.
- **Why players may replay it:** Different warehouse layouts, minimum-pulse solutions, obstacle combinations, and daily boards.
- **Main monetization opportunity:** Optional rewarded solution hint; unlimited undo prevents frustrating dead ends.
- **Development difficulty:** **Medium.** Flutter with deterministic grid rules; deadlock detection and level validation are the main challenges.
- **Main competitor/category:** Sokoban-style puzzles such as [Sokoban Original & Extra](https://play.google.com/store/apps/details?id=br.com.orangevoid.sokobanfree).
- **What makes it different:** Moving crates from a distance changes how players use corridors, corners, and the robot's position.

## 27. Pocket Drift Circuit

**Working title: Pocket Drift Circuit**

- **Suggested Android package:** `com.childhood.pocketdriftcircuit`
- **Genre:** Top-down arcade racing.
- **Gameplay concept:** Complete compact time-trial circuits where clean drifts build boost that can be spent on straights or shortcut gates.
- **Core gameplay loop:** Start lap -> link controlled drifts -> earn boost -> choose where to spend it -> finish -> race your saved ghost.
- **Why players may replay it:** Better racing lines, boost-management decisions, personal ghosts, and short daily track challenges.
- **Main monetization opportunity:** Optional rewarded doubling of cosmetic currency after a race.
- **Development difficulty:** **Medium-high.** Flame with simplified vehicle dynamics; responsive steering and consistent collision behavior are critical.
- **Main competitor/category:** Top-down racers such as [Reckless Racing 3](https://apps.apple.com/us/app/reckless-racing-3/id882453590), a premium reference.
- **What makes it different:** Boost also buys route opportunities, so players must choose between immediate speed and a potentially better shortcut.

## 28. Carve the Shape

**Working title: Carve the Shape**

- **Suggested Android package:** `com.childhood.carvetheshape`
- **Genre:** Precision crafting arcade.
- **Gameplay concept:** Shave a flat material block into a target silhouette using a limited number of continuous cutting strokes.
- **Core gameplay loop:** Inspect outline -> choose cutting tool -> carve -> measure accuracy -> finish the piece -> attempt another order.
- **Why players may replay it:** Improved accuracy, fewer-stroke solutions, different tool widths, and generated silhouette challenges.
- **Main monetization opportunity:** Optional rewarded doubling of decoration tokens after completing an order.
- **Development difficulty:** **Medium.** Flutter canvas or Flame with a material mask; accurate touch mapping and clear scoring need attention.
- **Main competitor/category:** [Woodturning](https://play.google.com/store/apps/details?hl=en-US&id=com.BallGames.Woodturning), with **100M+ downloads**.
- **What makes it different:** A constrained stroke budget makes tool choice and cutting order meaningful, while flat silhouettes keep asset production manageable.

## 29. Meadow Claim

**Working title: Meadow Claim**

- **Suggested Android package:** `com.childhood.meadowclaim`
- **Genre:** Territory-capture arcade.
- **Gameplay concept:** Draw trails from safe ground to enclose meadow patches while avoiding beetles that can cut an unfinished trail.
- **Core gameplay loop:** Inspect patrols -> leave safe territory -> draw boundary -> reconnect safely -> capture ground -> reach the area objective.
- **Why players may replay it:** Different patrol patterns, optional flower patches, faster completion, and riskier large-area captures.
- **Main monetization opportunity:** One optional rewarded rescue after a trail is cut; assisted scores are marked separately.
- **Development difficulty:** **Medium.** Flame with grid-based area filling and simple enemy patrols; boundary handling needs thorough testing.
- **Main competitor/category:** Territory-capture games such as [Paper.io 2](https://play.google.com/store/apps/details/?hl=en-US&id=io.voodoo.paper2), with **100M+ downloads**.
- **What makes it different:** Authored objectives and predictable local enemies support an offline puzzle-arcade experience, with no multiplayer infrastructure.

## 30. Bridge Relay

**Working title: Bridge Relay**

- **Suggested Android package:** `com.childhood.bridgerelay`
- **Genre:** Construction and resource-planning puzzle.
- **Gameplay concept:** Connect several islands with a limited kit of beams, then choose routes that safely carry light and heavy delivery vehicles.
- **Core gameplay loop:** Inspect destinations and loads -> allocate materials -> build crossings -> dispatch vehicles -> identify weak sections -> revise.
- **Why players may replay it:** Cheaper network designs, alternate delivery routes, heavier-load challenges, and different island arrangements.
- **Main monetization opportunity:** Optional rewarded hint identifying an overstressed connection.
- **Development difficulty:** **Medium-high.** Flame with a constrained structural simulation; believable failures and stable load calculations are the main risks.
- **Main competitor/category:** [Bridge Constructor](https://apps.apple.com/us/app/bridge-constructor/id503190232), an established construction-puzzle reference.
- **What makes it different:** One material budget must support an entire delivery network, making route selection part of the construction problem.
