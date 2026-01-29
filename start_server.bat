@echo off
echo ===============================
echo  Text2Video AI - Server Start
echo ===============================

python -m venv venv
call venv\Scripts\activate

pip install -r requirements.txt

echo -------------------------------
echo Server is starting...
echo Open: http://localhost:8000/docs
echo -------------------------------

uvicorn server:app --host 0.0.0.0 --port 8000

pause
