"""Build the versioned standalone Ship Station Hotkeys addon.

The addon was named Galactic Menu Hotkey before v1.7. Its manager GUID and
resource path are unchanged so managers treat the rename as an update.
"""
from pathlib import Path
import json
import os
import sys
import zipfile

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, os.environ.get("BINGUS_SHARED_LOADER", str(HERE.parent / "BingusSharedLoader")) + "/scripts")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_addon import build_addon  # noqa: E402
from entry import entry_text, locale_files  # noqa: E402
import translations  # noqa: E402

VERSION = "1.8"


def build():
    # Bundled translations must be data only and free of errors.
    for path in locale_files(HERE)[1:]:
        problems = translations.check(HERE / "locales", path.stem, out=lambda line: None)
        if problems.errors:
            raise SystemExit(chr(10).join(problems.errors))
    output = HERE / "releases" / f"Ship-Station-Hotkeys-v{VERSION}.zip"
    build_addon("mods/cowboybingus/galactic_menu_hotkey", entry_text(HERE),
                "3d8fdb82-9df6-4dc9-a538-5f94fc60a2e7", output,
                display_name=f"Ship Station Hotkeys v{VERSION}")
    with zipfile.ZipFile(output) as archive:
        files = {name: archive.read(name) for name in archive.namelist()}
    manifest = json.loads(files["manifest.json"])
    manifest["Description"] = (
        "Ship shortcuts: Tab map, F1 Armory, F5 Control Center, F6 Ship Management, "
        "F7 Stratagem Hero when beside its cabinet, F8 instant Hellpod entry after mission selection. "
        "Requires Bingus Shared Loader v17+. Mod Bindings Menu v2.0 or newer can rebind all six shortcuts, "
        "including controller buttons. Formerly Galactic Menu Hotkey.")
    manifest["Options"][0]["Description"] = manifest["Description"]
    files["manifest.json"] = (json.dumps(manifest, indent=2) + "\n").encode()
    files["INSTALL.txt"] = (HERE / "INSTALL.txt").read_bytes()
    with zipfile.ZipFile(output, "w") as archive:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    return output


if __name__ == "__main__":
    print(build())
