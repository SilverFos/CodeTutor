@echo off
echo Activating python virtual environment
call venv\Scripts\activate
where python
call flask --app backend/app.py run