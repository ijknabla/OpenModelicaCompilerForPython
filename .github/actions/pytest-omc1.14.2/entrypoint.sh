#!/bin/bash
set -eu

python --version
omc --version

useradd -m ${USER}
sudo -u ${USER} python -m pip install ${GITHUB_WORKSPACE}
sudo -u ${USER} python -m pip install -r ${GITHUB_WORKSPACE}/tests/requirements.txt
sudo -u ${USER} /home/${USER}/.local/bin/pytest -v ${GITHUB_WORKSPACE}
