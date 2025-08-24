#!/bin/bash

# Ensure addon and manifest versions are in sync before running tests
python3 scripts/check_versions.py || exit 1

blender --addons CAD_Sketcher --python ./testing/__init__.py -- --log_level=INFO
