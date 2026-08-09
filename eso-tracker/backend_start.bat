@echo off
title ESO Companion - Backend (port 8000)
cd /d "%~dp0backend"
"..\..\.venv\Scripts\uvicorn.exe" main:app --reload --host 0.0.0.0 --port 8000
pause
