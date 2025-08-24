# Contributing to CAD Sketcher

Thank you for considering contributing to CAD Sketcher!

## Getting Started
- Ensure you are using a supported version of Blender and Python.
- Install development dependencies as described in `README.md`.

## Development Workflow
1. Keep `blender_manifest.toml` and `__init__.py` version numbers in sync. Run:
   ```bash
   python scripts/check_versions.py
   ```
2. Run tests before submitting a pull request:
   ```bash
   bash run_tests.sh
   ```
3. Follow existing code style and prefer modular utilities over new global state.

## Pull Requests
- Describe your changes clearly.
- Include tests or examples where possible.
- Ensure your branch is rebased onto the latest `main`.

We appreciate your contributions!
