#!/usr/bin/env python3
"""Check that version in blender_manifest.toml matches bl_info in __init__.py."""
import re
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python <3.11 fallback
    import tomli as tomllib  # type: ignore

root = Path(__file__).resolve().parents[1]
manifest_path = root / "blender_manifest.toml"
init_path = root / "__init__.py"

# Read manifest version
with manifest_path.open("rb") as f:
    manifest_version = tomllib.load(f).get("version")

# Read __init__.py for version tuple
match = None
with init_path.open("r", encoding="utf-8") as f:
    content = f.read()
    match = re.search(r"\"version\"\s*:\s*\(([^)]+)\)", content)

if not match:
    print("Could not find version in __init__.py")
    sys.exit(1)

init_version = ".".join(part.strip() for part in match.group(1).split(","))

if manifest_version != init_version:
    print(
        f"Version mismatch: blender_manifest.toml has {manifest_version}, __init__.py has {init_version}"
    )
    sys.exit(1)

print(f"Version check passed: {manifest_version}")
