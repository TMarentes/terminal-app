#!/bin/bash

./py_and_venv_check.sh

echo "Starting Python Virtual Environment..."

python -m venv venv

./dependency_check.sh

python3 ./main.py

deactivate
# rm -r venv