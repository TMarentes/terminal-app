if ! [[ -x "$(command -v python3)" ]]; then
  echo 'Error: This program uses Python3, but it is not installed. To install it, go to: https://installpython3.com/' >&2
  exit 1
fi

if ! [[ -x "$(command -v pip)" ]]; then
  echo 'Error: This program requires Pip, but it is not installed. To install it, go to: https://pypi.org/project/pip/' >&2
  exit 1
fi


if python -c "import venv" &>/dev/null; then
  echo 'Venv is already installed.'
else
  echo 'Venv is not installed. Type "Y" to install venv, or enter anything else to exit.'
  read user_input
  if [ "$user_input" == "Y" ] || [ "$user_input" == "y" ]; then
    pip install venv
  else
    exit 1
  fi
fi