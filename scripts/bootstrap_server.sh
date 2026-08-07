#!/bin/bash

apt update

apt install -y \
    tesseract-ocr \
    poppler-utils

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt