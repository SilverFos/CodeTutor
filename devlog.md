# Devlog - Project CodeTutor

## 22 August 2025

### Tasks completed:
- Created virtual environment for isolated installation of Flask
- created README.md, .gitignore, devlog.md
- created backend/app.py as an interface for Flask server
- created exercises/cpp and exercises/python for two courses
- created frontend folder
- created ForLoop.json for testing Flask
- created activ.bat to automate virtual environment activation and starting Flask server

### Problems faced
- failure in opening pythonForLoop.json in test server [404]: did not change python.json to pythonForLoop.json in app.py
- failure in opening exercise/pythonForLoop.json in test server [500: internal server error]: home folder found to have ex**c**ercise as name. Corrected to exercise.

### Next step
- generate an introduction page describing available courses
- expand topics for any one course
- make basic html interface

### Review
- Need to be careful with filenames. single spelling mistake breaks system

## 23 August 2025

### Tasks completed
- created notes.md to note down new topics and guides
- created exercises/intro.json for seperate introduction page
- updated activ.bat with checks to ensure venv activation
- updated app.py to hold seperate link for exercise introduction

### Problems faced
- faced 404 issue due to stray slash (additional / after link). can be resolved by including alternate route

### Next steps
- create json for verious python subtopics.
- create dynamic route to implement multiple subtopics
- make basic html inteface

### Review
- need to ensure multiple failsafes.