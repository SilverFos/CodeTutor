@echo off
echo Activating python virtual environment
call venv\Scripts\activate
call flask --app backend/app.py run