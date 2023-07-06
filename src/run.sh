#!/bin/bash

./scripts/dependency_check.sh

echo "Starting Python Virtual Environment..."

python3 -m venv env

if [ -f "env/bin/activate" ]; then
  source env/bin/activate
fi
if [ -f "env/Scripts/activate" ]; then
  source env/Scripts/activate
fi

pip install -r requirements.txt

python3 ./scripts/main.py

deactivate

rm -r env
