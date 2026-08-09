@echo off
title ESO Companion - Tester 3 Backend (port 8004)
cd /d "C:\Users\Covert\DEV\ESO_Build_Companion\eso-tracker\backend"
set ESO_DB_PATH=C:\Users\Covert\DEV\ESO_Build_Companion\eso-tracker\backend\data\tester3.db
"..\..\.venv\Scripts\uvicorn.exe" main:app --host 0.0.0.0 --port 8004
pause
