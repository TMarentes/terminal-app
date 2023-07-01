#!/bin/bash

./py_and_venv_check.sh

echo "Starting Python Virtual Environment..."

python -m venv env
source env/Scripts/activate

./dependency_check.sh

python3 ./main.py

deactivate
rm -r env