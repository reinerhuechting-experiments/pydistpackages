#!/usr/bin/env bash

# This script installs the distribution package defined
# in distpackage1 into the VEvn in editable mode.

./_create_venv.sh
source .venv/bin/activate
pip install -e distpackage1
