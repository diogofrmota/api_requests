python3 -m venv .venv
source .venv/bin/activate
pip3 install requests
# json module is already built-in
pip3 freeze > requirements.txt
deactivate # leave venv
