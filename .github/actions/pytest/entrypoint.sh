#!/bin/bash
set -eu

python --version
omc --version

useradd -m user
sudo -u user python -m pip install ${GITHUB_WORKSPACE}
sudo -u user python -m pip install -r ${GITHUB_WORKSPACE}/tests/requirements.txt
sudo -u user /home/user/.local/bin/pytest -v ${GITHUB_WORKSPACE}
