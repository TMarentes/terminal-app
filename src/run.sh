#!/bin/bash

./dependency_check.sh

echo "Starting Python Virtual Environment..."

python -m venv env

source env/Scripts/activate

pip install -r requirements.txt

python3 ./main.py

deactivate

rm -r env
