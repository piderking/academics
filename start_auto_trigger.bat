@echo off
title Academic Vector Store - Auto-Trigger Monitor
echo =======================================================
echo   Starting Academic Auto-Trigger File Watcher...
echo   Monitoring G:\My Drive\Academics for course updates
echo =======================================================
python .academic_engine\auto_trigger.py
pause
