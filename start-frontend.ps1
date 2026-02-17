# Start Frontend Server
Write-Host "Starting Frontend Server..." -ForegroundColor Green

Set-Location apps/client

# Check if node_modules exists
if (-not (Test-Path "node_modules")) {
    Write-Host "Error: Dependencies not installed. Run setup-frontend.ps1 first" -ForegroundColor Red
    exit 1
}

# Start the development server
Write-Host "Starting Next.js server on http://localhost:3000" -ForegroundColor Cyan
npm run dev
