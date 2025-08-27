#!/bin/bash

# Ensure Blender is installed before proceeding
if ! command -v blender >/dev/null 2>&1; then
  echo "Error: Blender executable not found. Install Blender to run interactive tests." >&2
  exit 1
fi

blender --addons CAD_Sketcher --python ./testing/__init__.py -- --interactive --log_level=INFO
