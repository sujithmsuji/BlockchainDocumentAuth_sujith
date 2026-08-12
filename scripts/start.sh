#!/bin/bash

PROJECT_DIR="/home/ubuntu/devops-practice/projects/blockchain-document-auth"

cd "$PROJECT_DIR" || exit 1

source venv/bin/activate

python app.py

