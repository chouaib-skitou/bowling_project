@echo off
REM Download Python 3.10.7 Installer
echo Downloading Python 3.10.7 Installer...
powershell -command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe -OutFile python-3.10.7-amd64.exe"

REM Install Python 3.10.7
echo Installing Python 3.10.7...
start /wait python-3.10.7-amd64.exe /quiet InstallAllUsers=1 PrependPath=1

REM Verify Python Installation
python --version
if %errorlevel% neq 0 (
    echo Python installation failed. Please install Python 3.10.7 manually.
    exit /b
)

REM Install Pytest
pip install pytest

echo Python and Pytest have been installed.
pause
