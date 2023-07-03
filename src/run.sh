#!/bin/bash

./scripts/dependency_check.sh

echo "Starting Python Virtual Environment..."

python3 -m venv env

FILE=env/Scripts/activate
if [ -f "$FILE" ]; then
  source env/Scripts/activate
else
  source env/bin/activate
fi

pip install -r requirements.txt

python3 ./scripts/main.py

deactivate

rm -r env
