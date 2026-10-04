# Ship Station Hotkeys v1.9

*Formerly Galactic Menu Hotkey.* Use these shortcuts aboard the Super Destroyer while no other menu is open:

| Key | Ship station | Action |
| --- | --- | --- |
| Tab | Galactic Map | Opens the Galactic War Hologram. |
| F1 | Armory | Opens the equipment menu. |
| F5 | Control Center | Opens the information terminal. |
| F6 | Ship Management | Opens ship upgrades. |
| F7 | Stratagem Hero | Starts the arcade cabinet when your character is beside it. |
| F8 | Hellpod Deployment | After you select a mission, opens the briefing immediately and seats you in your Hellpod behind it. |

The addon calls the game's ship menu presenters and station interaction routines. F2-F4 are left free because the game's performance monitor uses them.

F8 opens the briefing and skips its 2-second intro wait so the briefing appears immediately. Once the briefing is up, hidden behind it, F8 seats your character using the game's instant seat entry, the routine that places a player directly in a seat. The game then records you as the pod's occupant and handles the exit normally when you back out. If you press F8 while the Hellpod is still opening, the shortcut waits up to ten seconds and then enters.

Requires [Bingus Shared Loader v17 or newer / API 1](https://github.com/CowboyBingus/BingusSharedLoader/releases/latest). Install [Mod Bindings Menu v2.0](https://github.com/CowboyBingus/ModBindingsMenu/releases/latest) separately to rebind all six shortcuts on the **MODS** tab of the Mouse & Keyboard and Controller binding pages, under **SHIP STATION HOTKEYS**. Mod Bindings Menu v2.0 also lets you choose Press, Hold, Double Tap and the other activation types, and assign controller buttons. Without it, the listed keys remain fixed fallbacks. With a Mod Bindings Menu release that offers `poll` (after v2.1), the six bindings are read in one call per frame while the game is focused aboard the ship: 8 reads of game memory instead of 18. Older releases are read binding by binding, as before. With Bingus Shared Loader v19 the shortcuts register with Mod Bindings Menu once every mod has started, before the first frame (the loader's `after_startup`); with older loaders, on the first frame.

Translatable: the section name and the CONTROL CENTER and STRATAGEM HERO bindings follow the game's Text Language when a translation is installed (with Mod Bindings Menu v2.1 or newer they also follow a language change; the other four bindings use the game's own translated names). [How to translate](TRANSLATING.md).

## Install

Import `Ship-Station-Hotkeys-v1.9.zip` into Arsenal or HD2MM, enable this addon and Bingus Shared Loader, then deploy. Enable Mod Bindings Menu v2.0 for saved and controller shortcuts. Keep Bingus Shared Loader as the winning startup replacement. Restart Helldivers 2 after replacing an older version.

Upgrading from Galactic Menu Hotkey: this is the same addon under a new name. Your mod manager treats it as an update, and your saved shortcut keys are kept. Remove the withdrawn Galactic Menu Hotkey v1.3 and v1.4 packages if they are still installed. Vanilla Plus Megapack bundles this addon as its Ship Station Hotkeys option; do not enable both the standalone addon and that option.

## Compatibility and test status

The native calls are guarded by the exact `game.dll` and `helldivers2.exe` SHA-256 values for Steam build **25480438** (EXE **1.8.46015.0**). They run only when the ship's galaxy table is present and no menu presenter is active. F7 also requires an idle arcade cabinet, a valid local avatar, and a world-position distance of at most three units. F8 requires a solo ship session, a selected mission, your own Hellpod (deployment slot 0) open and unoccupied, and your character not already seated. Pod ownership and seat replication with other players are unverified, so F8 stays inactive when another player is aboard. The per-frame update runs through Bingus Shared Runtime's update guard (`src/bingus_runtime.lua`, an unchanged copy): its own errors count in bursts and the 8th of a burst stops the shortcuts for the session. When the update of a mod below it fails, the shortcuts pause and resume after 60 frames without such an error; a key held through the pause must be pressed again, and a waiting F8 is cancelled. 8 such errors in a burst stop them too. The game's module files are hashed once per session for every mod together (`src/bingus_memory.lua`). A changed build, unavailable state, or another active menu leaves the shortcut inactive and writes the reason to `%LOCALAPPDATA%\CowboyBingus\Helldivers2\Logs\GalacticMenuHotkey.log` (the log keeps its original name).

Live tests confirmed Tab, F1, F5, F6, and F8's instant Hellpod entry and exit. The seat can show for a fraction of a second during the briefing's 0.2-second fade-in. F7's current distance guard and controller activation through Mod Bindings Menu v2.0 still need a live check. Offline tests check the current build's native entry bytes, the presenter mappings, the Hellpod and seat guards, the instant-entry request, and the saved binding dispatch.

## Build and validate

Clone BingusSharedLoader beside this repository, then run `python -B scripts/build.py` on Windows with Helldivers 2 installed. The entry it builds (`scripts/entry.py`) embeds `src/bingus_text.lua`, `locales/` and Bingus Shared Runtime's `src/bingus_runtime.lua` and `src/bingus_memory.lua` ahead of `src/galactic_menu_hotkey.lua`. Before it packages anything, the build runs every test (native dispatch guards, binding integration, per-frame call budgets, reading the bindings with Mod Bindings Menu's `poll` and with `is_down` alike over generated frames, registration in the loader's `after_startup` and without it, the update guard's bursts and pauses, translations, other mods declaring the same Windows functions first or later, with SDK prototypes or with `tests/hostile_vm.lua`'s `H.clash`) in LuaJIT and in the game's own `bin/lua51.dll`, and stops when one fails or when a `tests/test_*.lua` file is missing from its list. It takes LuaJIT from `HD2_LUAJIT`, else from `tools/src/LuaJIT/src/luajit.exe` in a folder above this repository, else from PATH; set `HD2_LUA51_DLL` when the game is installed elsewhere. To run one test in the game's LuaJIT by hand: `python tests/game_lua.py tests/test_hotkey.lua`. Optionally set `HD2_GAME_CAPTURE` to a local current-build game.dll memory capture to verify the native entry prefixes; captures are not distributed.

**AI disclosure:** Claude Opus 5.5 assisted with research, implementation, tests and documentation.

## License

Zero-Clause BSD (0BSD): use, copy, modify and distribute for any purpose, with no conditions. See `LICENSE`.
