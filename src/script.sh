#!/bin/bash

if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: This program uses Python3, but it is not installed. To install it, go to: https://installpython3.com/' >&2
  exit 1
fi

chmod +x ./script.sh 
# pip install requests
python3 ./main.py