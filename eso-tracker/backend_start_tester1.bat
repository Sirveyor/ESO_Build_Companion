@echo off
title ESO Companion - Tester 1 Backend (port 8002)
cd /d "C:\Users\Covert\DEV\ESO_Build_Companion\eso-tracker\backend"
set ESO_DB_PATH=C:\Users\Covert\DEV\ESO_Build_Companion\eso-tracker\backend\data\tester1.db
"..\..\.venv\Scripts\uvicorn.exe" main:app --host 0.0.0.0 --port 8002
pause
