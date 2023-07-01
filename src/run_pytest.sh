#!/bin/bash

./scripts/dependency_check.sh

echo "Starting Python Virtual Environment..."

python -m venv env

source env/Scripts/activate

pip install -r requirements.txt

python -m pytest ./scripts/test_employee.py

python -m pytest ./scripts/test_search.py

deactivate

rm -r env