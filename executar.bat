@echo off
echo ========================================
echo   YOLOv11 - Executando Sistema
echo ========================================
echo.

REM Verificar se o ambiente virtual existe
if not exist "venv\Scripts\activate.bat" (
    echo [ERRO] Ambiente virtual nao encontrado!
    echo.
    echo Por favor, execute primeiro:
    echo    python -m venv venv
    echo    pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

REM Ativar ambiente virtual e executar
echo Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo.
echo Executando main.py...
echo Pressione 'q' na janela para sair.
echo.

python main.py

echo.
echo Programa finalizado.
pause

