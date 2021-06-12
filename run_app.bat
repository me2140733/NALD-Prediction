  
CALL .env/Scripts/activate.bat

@echo off
SETLOCAL
set FLASK_APP= aki-prediction
set FLASK_ENV=development
CALL flask run -p 5000

cmd \k
