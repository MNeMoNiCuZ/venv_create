@echo off
setlocal

:: Prompt for virtual environment name with default 'venv'
set VENV_NAME=venv
set /p VENV_NAME="Enter the name for your virtual environment (Press Enter for default 'venv'): "

:: Create the virtual environment
echo Creating virtual environment named %VENV_NAME%...
python3.11 -m venv %VENV_NAME%

:: Generate the activate_venv.bat file
echo Generating activate_venv.bat...
(
echo @echo off
echo cd %%~dp0
echo set VENV_PATH=%VENV_NAME%
echo.
echo echo Activating virtual environment...
echo call "%%VENV_PATH%%\Scripts\activate"
echo echo Virtual environment activated.
echo cmd /k
) > activate_venv.bat

echo Setup complete. Use 'activate_venv.bat' to activate the virtual environment.

:: Call activate_venv.bat to activate the virtual environment
echo Activating the virtual environment...
call activate_venv.bat

echo Virtual environment %VENV_NAME% is activated. You can reactivate it in the future by running 'activate_venv.bat'.
endlocal
