#!/bin/bash

# Ensure Blender is installed before proceeding
if ! command -v blender >/dev/null 2>&1; then
  echo "Error: Blender executable not found. Install Blender to run tests." >&2
  exit 1
fi

# Ensure addon and manifest versions are in sync before running tests
python3 scripts/check_versions.py || exit 1

blender --addons CAD_Sketcher --python ./testing/__init__.py -- --log_level=INFO
