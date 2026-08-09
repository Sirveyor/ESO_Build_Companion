# Tester 1 backend -- own database, own port. Run alongside the other tester
# backends and the single shared frontend (frontend_start.bat).
cd C:\Users\Covert\DEV\ESO_Build_Companion\eso-tracker\backend
$env:ESO_DB_PATH="C:\Users\Covert\DEV\ESO_Build_Companion\eso-tracker\backend\data\tester1.db"
..\..\.venv\Scripts\uvicorn.exe main:app --host 0.0.0.0 --port 8002

# Tester 1 then visits the frontend once with ?api_port=8002 appended to the URL
# (e.g. http://eso-companion:5173/?api_port=8002) -- the browser remembers
# it after that via localStorage, no need to keep the query param on later visits.
