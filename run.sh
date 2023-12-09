#!/bin/bash 

# check if python is install or not 

# check if venv exists

python3 -m venv .todo-venv
source .todo-venv/bin/activate
pip3 install colored
python3 main.py