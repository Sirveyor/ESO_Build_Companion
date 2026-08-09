# Tester 2 backend -- own database, own port.
cd C:\Users\Covert\DEV\ESO_Build_Companion\eso-tracker\backend
$env:ESO_DB_PATH="C:\Users\Covert\DEV\ESO_Build_Companion\eso-tracker\backend\data\tester2.db"
..\..\.venv\Scripts\uvicorn.exe main:app --host 0.0.0.0 --port 8003

# Tester 2 visits the frontend once with ?api_port=8003 appended to the URL.
