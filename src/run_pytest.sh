#!/bin/bash

./scripts/dependency_check.sh

echo "Starting Python Virtual Environment..."

python3 -m venv env

source env/Scripts/activate

pip install -r requirements.txt

python3 -m pytest ./scripts/test_employee.py

python3 -m pytest ./scripts/test_search.py

deactivate

rm -r env