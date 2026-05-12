@echo off
title Regulatory Compliance Agent - Setup
color 0A

echo ============================================================
echo   Regulatory Compliance AI Agent - Windows Setup
echo   UAE and KSA | Real Estate and BFSI Sectors
echo ============================================================
echo.

REM Check Python is installed
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo [ERROR] Python not found. Please install Python 3.11+ from https://python.org
    echo         Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo [OK] Python found:
python --version
echo.

REM Create virtual environment
echo [1/4] Creating virtual environment...
python -m venv venv
IF ERRORLEVEL 1 (
    echo [ERROR] Failed to create virtual environment.
    pause
    exit /b 1
)
echo [OK] Virtual environment created.
echo.

REM Activate virtual environment and install dependencies
echo [2/4] Installing dependencies (this may take a minute)...
call venv\Scripts\activate.bat
pip install --upgrade pip --quiet
pip install -r requirements.txt
IF ERRORLEVEL 1 (
    echo [ERROR] Failed to install dependencies.
    pause
    exit /b 1
)
echo [OK] Dependencies installed.
echo.

REM Create .env file if it doesn't exist
echo [3/4] Setting up environment file...
IF NOT EXIST .env (
    copy .env.example .env >nul
    echo [OK] Created .env file from template.
) ELSE (
    echo [OK] .env file already exists.
)
echo.

REM Prompt for API key
echo [4/4] API Key Configuration
echo.
echo You need an Anthropic API key to run the agent.
echo Get yours free at: https://console.anthropic.com
echo.

findstr /C:"sk-ant" .env >nul 2>&1
IF ERRORLEVEL 1 (
    echo Your .env file does not have a real API key yet.
    echo.
    set /p APIKEY="Paste your Anthropic API key here (or press Enter to skip): "
    IF NOT "!APIKEY!"=="" (
        echo ANTHROPIC_API_KEY=!APIKEY!> .env
        echo [OK] API key saved to .env
    ) ELSE (
        echo [SKIP] You can edit .env manually and add your key before running.
    )
) ELSE (
    echo [OK] API key already configured in .env
)

echo.
echo ============================================================
echo   Setup Complete!
echo ============================================================
echo.
echo To run the agent:
echo   Double-click run.bat
echo   OR open a terminal and type: run.bat
echo.
echo To run a quick demo:
echo   call venv\Scripts\activate.bat
echo   python demo.py
echo.
pause
