# Start Backend Server
Write-Host "Starting Backend Server..." -ForegroundColor Green

Set-Location apps/server

# Activate virtual environment
if (Test-Path ".venv\Scripts\Activate.ps1") {
    .\.venv\Scripts\Activate.ps1
    Write-Host "Virtual environment activated" -ForegroundColor Green
} else {
    Write-Host "Error: Virtual environment not found. Run setup-backend.ps1 first" -ForegroundColor Red
    exit 1
}

# Start the server
Write-Host "Starting FastAPI server on http://localhost:8000" -ForegroundColor Cyan
python main.py
