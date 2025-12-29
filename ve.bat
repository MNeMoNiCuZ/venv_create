:: Activates virtual environments
:: Version 1.0
@echo off
setlocal enabledelayedexpansion

:: Check if default 'venv' exists
if exist "venv\Scripts\activate.bat" (
    echo Activating virtual environment 'venv'...
    call "venv\Scripts\activate"
    echo Virtual environment activated.
    cmd /k
    goto end
)

:: If default 'venv' doesn't exist, ask for venv name
echo Default 'venv' folder not found.
echo.
set /p VENV_NAME="Enter the name of your virtual environment: "

:: Check if the provided venv exists
if exist "!VENV_NAME!\Scripts\activate.bat" (
    echo Activating virtual environment '!VENV_NAME!'...
    call "!VENV_NAME!\Scripts\activate"
    echo Virtual environment activated.
    cmd /k
) else (
    echo ERROR: Virtual environment '!VENV_NAME!' not found.
    echo Make sure the folder exists and contains Scripts\activate.bat
    pause
)

:end
endlocal