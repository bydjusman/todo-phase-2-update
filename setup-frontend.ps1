# Frontend Setup Script for Windows
Write-Host "Setting up Frontend..." -ForegroundColor Green

# Navigate to client directory
Set-Location apps/client

# Check if Node.js is installed
try {
    $nodeVersion = node --version
    Write-Host "Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "Error: Node.js is not installed or not in PATH" -ForegroundColor Red
    exit 1
}

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
npm install

Write-Host "`nFrontend setup complete!" -ForegroundColor Green
Write-Host "To start the frontend server, run:" -ForegroundColor Cyan
Write-Host "  cd apps/client" -ForegroundColor White
Write-Host "  npm run dev" -ForegroundColor White
