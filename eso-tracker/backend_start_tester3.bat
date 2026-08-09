@echo off
title ESO Companion - Tester 3 Backend (port 8004)
cd /d "%~dp0backend"
set ESO_DB_PATH=%~dp0backend\data\tester3.db
"..\..\.venv\Scripts\uvicorn.exe" main:app --host 0.0.0.0 --port 8004
pause
