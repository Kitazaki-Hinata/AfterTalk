@echo off
setlocal enabledelayedexpansion

REM ============================================================
REM   AfterTalk one-click launcher
REM   Just double-click this file. It will install uv (if
REM   needed), create the virtual environment, install all
REM   dependencies, and start the program. No manual setup.
REM ============================================================

REM Go to the directory of this script (project root)
cd /d "%~dp0"

REM Make sure uv's default install dir is on PATH for this session
set "PATH=%USERPROFILE%\.local\bin;%PATH%"

title AfterTalk Launcher

echo.
echo ============================================================
echo   Preparing AfterTalk runtime, please wait...
echo ============================================================
echo.

REM ------------------------------------------------------------
REM 1. Check whether uv is installed; if not, install it
REM ------------------------------------------------------------
where uv >nul 2>nul
if %errorlevel%==0 (
    echo [1/3] uv detected, skipping install.
) else (
    echo [1/3] uv not found, downloading and installing...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://astral.sh/uv/install.ps1 | iex"
    set "PATH=%USERPROFILE%\.local\bin;%PATH%"
)

REM Confirm uv is callable now
where uv >nul 2>nul
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] uv command still not found after install.
    echo Please close this window and double-click the script again.
    echo.
    goto :END
)

REM ------------------------------------------------------------
REM 2. Sync dependencies and create the virtual environment
REM    (uv installs the required Python version automatically)
REM ------------------------------------------------------------
echo.
echo [2/3] Installing dependencies / creating venv (first run may take a few minutes)...
uv sync
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Dependency install failed. Check your network and retry.
    echo.
    goto :END
)

REM ------------------------------------------------------------
REM 3. Launch the main program inside the virtual environment
REM ------------------------------------------------------------
echo.
echo [3/3] Starting AfterTalk...
echo ============================================================
echo.
uv run main.py
set "EXITCODE=%errorlevel%"

echo.
echo ============================================================
if "%EXITCODE%"=="0" (
    echo   Program exited normally (exit code 0).
) else (
    echo   [ERROR] Program exited with code %EXITCODE%.
    echo   Please send the messages above to the developer.
)
echo ============================================================

:END
echo.
echo Press any key to close this window...
pause >nul
endlocal
