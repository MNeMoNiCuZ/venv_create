@echo off
echo Installing PyTorch, torchvision, and torchaudio using UV pip from the local cache...
echo.

:: Get the directory of the batch script itself and use it to run the Python script
python "%~dp0torchinstall.py"

echo.
uv pip install torch torchvision torchaudio --no-index --find-links=%USERPROFILE%\my-pip-cache
echo.
echo Installation completed successfully!
pause
