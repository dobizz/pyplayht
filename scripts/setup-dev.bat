@echo off

:: Define the path to the requirements file
if exist "requirements-dev.txt" (
    set requirements_file=requirements-dev.txt
) else if exist "..\requirements-dev.txt" (
    set requirements_file=..\requirements-dev.txt
) else (
    echo No requirements file found. Please make sure requirements-dev.txt exists in the current directory or one level up.
    exit /b 1
)

:: Check if pip is installed
where pip >nul 2>&1
if errorlevel 1 (
    echo pip is not installed. Please install Python and try again.
    exit /b 1
)

:: Install requirements
pip install -r "%requirements_file%"

:: Check if the installation was successful
if %errorlevel% equ 0 (
    echo Requirements installed successfully.
) else (
    echo Failed to install requirements.
)

:: Install pre-commit hooks
pre-commit install
pre-commit install --hook-type commit-msg --hook-type pre-push
