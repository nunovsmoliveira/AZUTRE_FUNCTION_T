@echo off
cd /d "%~dp0"

echo [1/3] A entrar na pasta do projeto...
cd .\AZURE\AZURE_FUNTION_T

echo [2/3] A ativar o ambiente virtual...
call .venv\Scripts\activate.bat

echo [3/3] A iniciar Azure Function...
func start

pause
