@echo off
title ESO Companion - Backend (port 8000)
cd /d "C:\Users\Covert\DEV\ESO_Build_Companion\eso-tracker\backend"
"..\..\.venv\Scripts\uvicorn.exe" main:app --reload --host 0.0.0.0 --port 8000
pause

