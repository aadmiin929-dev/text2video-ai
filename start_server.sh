#!/bin/bash

echo "==============================="
echo " Text2Video AI - Server Start"
echo "==============================="

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

echo "-------------------------------"
echo "Server is starting..."
echo "Open: http://localhost:8000/docs"
echo "-------------------------------"

uvicorn server:app --host 0.0.0.0 --port 8000
