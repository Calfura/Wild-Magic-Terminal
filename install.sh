#!/bin/bash

# Check for python install
# Installs virtual environment
# Install Colored Module
# Install D20 Module

python3 -m venv .venv
source .venv/bin/activate
pip3 install colored
pip3 install -U d20