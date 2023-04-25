#!/bin/bash

#DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Open the Terminal app and navigate to the script's directory
#osascript -e "tell application \"Terminal\"" -e "activate" -e "do script \"cd $DIR; clear; 
#            source creative_env/bin/activate && export PATH=./creative_env/bin:$PATH && 
#               export PYTHONPATH=./creative_env/lib/python3.8/site-packages:$PYTHONPATH && 
#               python3 run.py\"" -e "end tell"
source creative_env/bin/activate
export PATH=./creative_env/bin:$PATH 
export PYTHONPATH=./creative_env/lib/python3.8/site-packages:$PYTHONPATH
python3 run.py
