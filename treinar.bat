@echo off
echo ========================================
echo   Iniciando Treinamento
echo ========================================
echo.

REM Ativar ambiente virtual e executar
call venv\Scripts\activate.bat
python treinar_carparts.py

pause

