#!/bin/bash
set -eu

python --version
omc --version

cd ${GITHUB_WORKSPACE}

useradd -m ${USER}
sudo -u ${USER} python -m pip install poetry
sudo -u ${USER} python -m poetry install
sudo -u ${USER} python -m poetry run pytest
