@echo off
title Academic Mentor - AGY Instance
cd /d "G:\My Drive\Academics"

echo =======================================================
echo   Launching Academic Mentor (Antigravity Instance)
echo   Workspace: G:\My Drive\Academics
echo   Conversation ID: 4fc7ef2c-dc26-4144-a761-288df9e3b360
echo =======================================================
echo.

:: Check if Study Portal is already running on port 8080
netstat -ano | findstr :8080 >nul
if %errorlevel% neq 0 (
    echo [*] Starting Study Portal server on http://localhost:8080...
    start /b python study_portal\serve.py >nul 2>&1
)

:: Check if auto_trigger file-watcher is already running
tasklist /fi "imagename eq python.exe" /v 2>nul | findstr /i "auto_trigger.py" >nul
if %errorlevel% neq 0 (
    echo [*] Starting auto_trigger file watcher...
    start /b python .academic_engine\auto_trigger.py >nul 2>&1
)

echo [*] Launching Antigravity interactive session...
echo.

"C:\Users\pider\AppData\Local\agy\bin\agy.exe" --conversation 4fc7ef2c-dc26-4144-a761-288df9e3b360

if %errorlevel% neq 0 (
    echo.
    echo [Notice] Session closed.
    pause
)
