# Changelog

## 1.8

- Translatable: the section name and the Control Center and Stratagem Hero binding names follow the game's Text Language when a translation is installed (see TRANSLATING.md).
- With Mod Bindings Menu v2.1 these names follow a language change the next time a binding page opens.
- Measured in live play: 0.021 ms per frame in missions and 0.077 ms on the ship while the game window is focused, the same as v1.7.

## 1.7

- Rename Galactic Menu Hotkey to Ship Station Hotkeys. The manager GUID, addon resource, binding IDs and log file name are unchanged, so managers treat it as an update and saved keys are kept.
- Group all six shortcuts under a SHIP STATION HOTKEYS section on the Mod Bindings Menu v2.0 MODS tab, where they can use any activation type and controller buttons.
- Seat your character in the Hellpod through the game's native instant seat entry after mission selection. The briefing opens without the 3.13-second entry animation, and the pod records you as its occupant.
- Open the briefing first and skip its 2-second intro wait, so the briefing UI appears immediately. The character is seated on the frame the briefing UI appears; seating later lets the pod entry camera replace the briefing's map camera. The move into the pod can show for a fraction of a second during the briefing's 0.2-second fade-in. If the intro is not observed, seating falls back to a 3-second delay. Closing the briefing before seating cancels the seat and is logged.
- Fix the 1.6 camera lock when backing out of the briefing. Version 1.6 opened the briefing without seating the character, so the game's exit sequence could not return the camera from the Galactic Map view.
- If you press F8 during the Hellpod ready animation, the shortcut waits up to ten seconds for the pod to open. Opening another menu or clearing the mission cancels the wait.
- Limit F8 to solo ship sessions. Pod ownership and seat replication with other players remain unverified.
- Live tests confirmed F8's instant entry and backing out of the briefing.

## 1.6 (unreleased test build)

- Register the Armory, Control Center, Ship Management, Stratagem Hero, and Hellpod shortcuts with Mod Bindings Menu v1.2.2 while retaining the fixed keys as fallback.
- Enter Hellpod Deployment through the native setup routine after verifying the idle presenter and matching active pod state. This path awaits live verification.
- Record that the observed process closure occurred without any shortcut press; its cause remains unconfirmed.

## 1.5 (unreleased test build)

- Require the local avatar to be within three world units of the Stratagem Hero cabinet before F7 starts the arcade. The live test confirmed that starting it from farther away leaves the camera transition unfinished.
- Disable F8 after the live test showed that opening the map presenter with a mission ready cancels deployment instead of entering the deployment screen.
- Keep F2-F4 free for the game's performance monitor. Version 1.4 is withdrawn.

## 1.4 (unreleased test build, withdrawn)

- Move Ship Management to F6 and Stratagem Hero to F7 because the game's performance monitor consumes F2-F4, even with Ctrl held. Keep Armory on F1 and Control Center on F5.
- Correct the Stratagem Hero idle check from the live test: the active-player field is zero while the cabinet is free and can retain the previous player in a separate field.
- Remove the direct Hellpod loadout presenter call after live testing showed it bypasses required ship camera state and can softlock entry and exit.
- Make F8 open the mission map so mission selection and deployment use the game's own flow.

## 1.3 (unreleased test build, withdrawn after live test)

- Add F1-F5 ship shortcuts for Armory, Ship Management, Stratagem Hero, Hellpod loadout, and Control Center.
- Start Stratagem Hero through its native arcade interaction after checking the cabinet and local avatar state.
- Keep Tab's saved Mod Bindings Menu binding and current-build native safety checks.
- F4 opens the game's normal loadout flow; deployment still uses the game's ready and launch controls.

## 1.2

- Update the shifted native map presenter address for Steam build 25480438.
- Keep saved keyboard bindings and Tab fallback.

## 1.1

- Integrate the saved keyboard shortcut from the separately installed Mod Bindings Menu.
- Retain Tab as the fallback when the binding addon is unavailable.
- Package as a standalone release for Bingus Shared Loader; also available as a Megapack option.

## 1.0

- Allow the native Hologram request only from the ship's observed idle menu state (presenter 0, stack depth 0). The 0.9 live log showed Tab was detected but blocked because its guard expected an already open Main menu.
- Live testing confirmed that Tab opens the Galactic Map from a clear spot away from the table, without moving the player or requiring the interaction prompt. The first opening had a noticeable delay; subsequent openings were smooth.

## 0.9

- Replace the enlarged table interaction and synthetic E input with the game's native Hologram presenter entry. The normal interaction prompt and player approach are no longer involved.
- Verify both current game modules by SHA-256 and the native presenter instruction prefix before binding the function.
- Attempt to open from Main presenter state aboard the Super Destroyer. The live game showed this guard did not match normal gameplay.
- Withdraw 0.8 after the live test showed that its larger radius still required targeting the table and moved the player.

## 0.8

- Continue probing the map template through the ship loading transition. Version 0.7 stopped after five searches before the game decrypted the template, leaving Tab inactive.
- Locate the current build's 46,616,576-byte decrypted entity region and validate the full map record before changing its four radii. This avoids repeatedly scanning its full contents during startup.

## 0.7

- Withdraw the 0.6 temporary-entity approach after a live Tab press crashed the game. The log stopped during that path, before it reported a successful spawn.
- Enlarge only the existing map interaction radius in the captured game template before the ship interaction is created. Keep view distances and priorities unchanged so normal nearby interactions retain their behavior.
- Send E only when the template was prepared before the current ship loaded. The map opening from a distance still needs an in-game check.

## 0.6 (withdrawn)

- Attempt to spawn `galactic_campaign_interact_point` at the local avatar's position on Tab, then remove it after the interaction window. A live Tab press crashed the game, so this version must not be used.
- Remove the static interaction-resource memory scan and patch. The previous version could send E at the table, but changing that template did not make the live interaction reachable from elsewhere on the ship.
- Log entity spawning, player-position lookup, input, and cleanup separately.

## 0.5

- Resolve `SendInput` from `user32.dll`, where Windows exports it. The live log showed that ship detection, interaction-record lookup, and Tab detection worked, but the previous `kernel32.dll` lookup left the synthetic interact key unavailable.
- Distinguish a missing `SendInput` export from a failed input call in the mod log.

## 0.4

- Detect the galaxy table unit placed in the ship hub.
- Remove the unrelated interaction-point resource check that never matched a placed unit.

## 0.3

- Pass the galaxy table's captured IdString64 to the engine's unit lookup.

## 0.2

- Check every active Stingray world for the ship's galaxy interaction point.
- Log callback, world detection, scan, and input stages for troubleshooting.

## 0.1

- Add a Tab shortcut for the Galactic War menu while aboard the Super Destroyer.
- Restore the galaxy table's captured interaction values after each shortcut.
- Restrict activation to the world containing the galaxy table.
- Package as a Bingus Shared Loader addon.

The 0.8 live test confirmed that the enlarged radius works but still requires
targeting the table and moves the player. The 0.9 live test confirmed that Tab
reached the addon, but its menu state guard blocked the native call.
