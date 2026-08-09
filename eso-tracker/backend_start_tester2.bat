@echo off
title ESO Companion - Tester 2 Backend (port 8003)
cd /d "%~dp0backend"
set ESO_DB_PATH=%~dp0backend\data\tester2.db
"..\..\.venv\Scripts\uvicorn.exe" main:app --host 0.0.0.0 --port 8003
pause
