# Todo App - Setup aur Troubleshooting Guide

## Quick Setup (Windows)

### 1. Backend Setup
```powershell
# PowerShell me run karein
.\setup-backend.ps1
```

### 2. Frontend Setup
```powershell
# PowerShell me run karein
.\setup-frontend.ps1
```

### 3. Servers Start Karein

**Backend (Terminal 1):**
```powershell
.\start-backend.ps1
```
Backend chalega: http://localhost:8000

**Frontend (Terminal 2):**
```powershell
.\start-frontend.ps1
```
Frontend chalega: http://localhost:3000

---

## Manual Setup (Agar scripts kaam na karein)

### Backend Setup (Manual)

1. **Server directory me jaayein:**
```powershell
cd apps/server
```

2. **Virtual environment banayein:**
```powershell
python -m venv .venv
```

3. **Virtual environment activate karein:**
```powershell
.\.venv\Scripts\Activate.ps1
```

4. **Dependencies install karein:**
```powershell
pip install -r requirements.txt
```

5. **Database initialize karein:**
```powershell
python init_db.py
```

6. **Server start karein:**
```powershell
python main.py
```

### Frontend Setup (Manual)

1. **Client directory me jaayein:**
```powershell
cd apps/client
```

2. **Dependencies install karein:**
```powershell
npm install
```

3. **Development server start karein:**
```powershell
npm run dev
```

---

## Common Errors aur Solutions

### Backend Errors

#### Error: "ModuleNotFoundError: No module named 'fastapi'"
**Solution:**
```powershell
cd apps/server
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

#### Error: "no such table: task" ya "no such table: user"
**Solution:** Database tables create nahi hue hain
```powershell
cd apps/server
.\.venv\Scripts\Activate.ps1
python init_db.py
```

#### Error: "Address already in use" (Port 8000)
**Solution:** Port already use ho raha hai
```powershell
# Process ko kill karein
netstat -ano | findstr :8000
# PID note karein aur kill karein
taskkill /PID <PID> /F
```

#### Error: "Missing authentication secret"
**Solution:** .env file check karein
```powershell
# apps/server/.env me ye hona chahiye:
DATABASE_URL=sqlite:///./todo_app.db
BETTER_AUTH_SECRET=super-secret-jwt-key-for-local-development-min-32-chars
```

### Frontend Errors

#### Error: "Registration failed" ya "Login failed"
**Possible Causes:**
1. Backend server nahi chal raha
2. CORS issue
3. Database tables nahi bane
4. Wrong API URL

**Solutions:**

**Step 1: Backend check karein**
```powershell
# Health check
curl http://localhost:8000/health
# Ya browser me: http://localhost:8000/health
```

**Step 2: Database tables check karein**
```powershell
cd apps/server
.\.venv\Scripts\Activate.ps1
python init_db.py
```

**Step 3: Backend logs check karein**
Backend terminal me errors dekho. Common errors:
- "no such table: user" → Database init nahi hua
- "CORS" error → CORS settings check karein

**Step 4: Frontend .env.local check karein**
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

**Step 5: Browser console check karein**
- F12 press karein
- Console tab me errors dekho
- Network tab me API calls dekho

**Step 6: Test backend directly**
```powershell
.\test-backend.ps1
```

#### Error: "Failed to connect to server"
**Solution:** Backend nahi chal raha hai
```powershell
# Backend start karein
.\start-backend.ps1
```

#### Error: "Cannot find module" ya dependency errors
**Solution:**
```powershell
cd apps/client
Remove-Item -Recurse -Force node_modules
Remove-Item package-lock.json
npm install
```

#### Error: "Port 3000 is already in use"
**Solution:**
```powershell
# Process ko kill karein
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

#### Error: "Failed to fetch" ya API connection error
**Solution:**
1. Backend chal raha hai ya nahi check karein: http://localhost:8000/health
2. CORS settings check karein backend me
3. Frontend .env.local file check karein:
```
NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:3000/api/auth
DATABASE_URL=file:./todo_app.db
BETTER_AUTH_SECRET=super-secret-jwt-key-for-local-development-min-32-chars
```

### Database Errors

#### Error: "database is locked"
**Solution:**
```powershell
# SQLite database file ko delete karke recreate karein
cd apps/server
Remove-Item todo_app.db
python init_db.py
```

---

## Testing

### Backend API Test
```powershell
# Automated test script
.\test-backend.ps1

# Manual tests
# Health check
curl http://localhost:8000/health

# API docs dekhein
# Browser me open karein: http://localhost:8000/docs
```

### Test Registration and Login

1. **Backend chal raha hai check karein:**
   - Open: http://localhost:8000/health
   - Should show: `{"status":"healthy"}`

2. **Frontend test karein:**
   - Open: http://localhost:3000
   - Click "Sign up" 
   - Email aur password enter karein
   - Account create hoga aur tasks page pe redirect hoga

3. **Automated test:**
```powershell
.\test-backend.ps1
```

### Frontend Test
```
Browser me open karein: http://localhost:3000
```

---

## Development Workflow

1. **Dono servers ko alag terminals me chalayein**
2. **Backend changes ke liye:** Server automatically reload hoga (uvicorn reload mode)
3. **Frontend changes ke liye:** Next.js automatically reload karega
4. **Database schema change ke liye:** `python init_db.py` dobara run karein

---

## Useful Commands

### Backend
```powershell
# Virtual environment activate
cd apps/server
.\.venv\Scripts\Activate.ps1

# Dependencies update
pip install -r requirements.txt

# Database reset
Remove-Item todo_app.db
python init_db.py

# Server start
python main.py
```

### Frontend
```powershell
# Dependencies update
cd apps/client
npm install

# Build production version
npm run build

# Start production server
npm start

# Development server
npm run dev
```

---

## Troubleshooting Checklist

- [ ] Python installed hai? (`python --version`)
- [ ] Node.js installed hai? (`node --version`)
- [ ] Backend virtual environment activate hai?
- [ ] Backend dependencies install hain? (`pip list`)
- [ ] Frontend dependencies install hain? (`npm list`)
- [ ] Database tables create hue hain? (`todo_app.db` file exist karti hai?)
- [ ] .env files sahi hain?
- [ ] Ports 3000 aur 8000 free hain?
- [ ] Backend server chal raha hai? (http://localhost:8000/health)
- [ ] CORS properly configured hai?

---

## Support

Agar koi error solve nahi ho raha, to:
1. Error message pura copy karein
2. Konsa command run kar rahe the wo note karein
3. Environment details share karein (Python version, Node version)
