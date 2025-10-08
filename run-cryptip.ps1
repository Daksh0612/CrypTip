# ==============================
# Cryptip One-Click Run Script
# ==============================

# 1️⃣ Set project paths
$backendPath = "C:\Projects\Cryptip\backend"
$frontendPath = "C:\Projects\Cryptip\frontend"

# 2️⃣ Move to backend
Write-Host "`n[INFO] Starting backend..."
Set-Location $backendPath

# 3️⃣ Activate Python venv
if (Test-Path ".\venv\Scripts\activate.ps1") {
    Write-Host "[INFO] Activating virtual environment..."
    . .\venv\Scripts\activate.ps1
} else {
    Write-Host "[INFO] Virtual environment not found. Creating venv..."
    python -m venv venv
    . .\venv\Scripts\activate.ps1
}

# 4️⃣ Install required Python packages
Write-Host "[INFO] Installing backend dependencies..."
pip install --upgrade pip
pip install fastapi uvicorn sqlalchemy pydantic

# 5️⃣ Start backend in a new window
Write-Host "[INFO] Launching backend on http://127.0.0.1:8000..."
Start-Process "python" " -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000"

# Wait 5 seconds for backend to start
Start-Sleep -Seconds 5

# 6️⃣ Move to frontend
Write-Host "`n[INFO] Starting frontend..."
Set-Location $frontendPath

# 7️⃣ Install frontend dependencies if node_modules missing
if (-not (Test-Path ".\node_modules")) {
    Write-Host "[INFO] Installing frontend dependencies..."
    npm install
}

# 8️⃣ Start frontend dev server in new window
Write-Host "[INFO] Launching frontend on http://localhost:5173..."
Start-Process "npm" "run dev"

Write-Host "`n🎉 Cryptip is now running! Visit frontend at http://localhost:5173 and backend at http://127.0.0.1:8000"
