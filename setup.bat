@echo off
setlocal EnableDelayedExpansion
title Regulatory Compliance Agent - Setup
color 0A

echo ============================================================
echo   Regulatory Compliance AI Agent - Windows Setup
echo   UAE and KSA - Real Estate and BFSI Sectors
echo   Powered by Google Gemini (FREE)
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
echo [4/4] Gemini API Key Configuration
echo.
echo This agent uses Google Gemini - 100%% FREE, no credit card needed.
echo.
echo To get your free Gemini API key:
echo   1. Go to: https://aistudio.google.com/apikey
echo   2. Sign in with your Google account
echo   3. Click "Create API key"
echo   4. Copy the key and paste it below
echo.

findstr /C:"AIza" .env >nul 2>&1
IF ERRORLEVEL 1 (
    echo Your .env file does not have a Gemini API key yet.
    echo.
    set /p APIKEY="Paste your Gemini API key here (or press Enter to skip): "
    IF NOT "!APIKEY!"=="" (
        echo GEMINI_API_KEY=!APIKEY!> .env
        echo [OK] API key saved to .env
    ) ELSE (
        echo [SKIP] Edit .env manually and add your key before running.
    )
) ELSE (
    echo [OK] Gemini API key already configured in .env
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
