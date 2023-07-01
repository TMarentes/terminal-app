#!/bin/bash

./dependency_check.sh

python -m pytest ./test_employee.py

python -m pytest ./test_search.py
