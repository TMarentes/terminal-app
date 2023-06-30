if ! [[ -x "$(command -v python3)" ]]; then
  echo 'Error: This program uses Python3, but it is not installed. To install it, go to: https://installpython3.com/' >&2
  exit 1
fi

if ! [[ -x "$(command -v pip)" ]]; then
  echo 'Error: This program requires Pip, but it is not installed. To install it, go to: https://pypi.org/project/pip/' >&2
  exit 1
fi

if python -c "import requests" &>/dev/null; then
  echo 'Requests is already installed.'
else
  echo 'Requests is not installed. Type "Y" to install requests, or enter anything else to exit.'
  read user_input
  if [ "$user_input" == "Y" ] || [ "$user_input" == "y" ]; then
    pip install requests
  else
    exit 1
  fi
fi

if python -c "import pytest" &>/dev/null; then
  echo 'Pytest is already installed.'
else
  echo 'Pytest is not installed. Type "Y" to install pytest, or enter anything else to exit.'
  read user_input
  if [ "$user_input" == "Y" ] || [ "$user_input" == "y" ]; then
    pip install pytest
  else
    exit 1
  fi
fi