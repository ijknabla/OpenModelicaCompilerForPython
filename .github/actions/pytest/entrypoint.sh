#!/bin/bash
set -eu

python --version
omc --version

useradd -m user
sudo -u user python -m pip install ${GITHUB_WORKSPACE}
