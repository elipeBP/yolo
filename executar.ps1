# Script PowerShell para executar o YOLOv11
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  YOLOv11 - Executando Sistema" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se o ambiente virtual existe
if (-not (Test-Path "venv\Scripts\Activate.ps1")) {
    Write-Host "[ERRO] Ambiente virtual não encontrado!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Por favor, execute primeiro:" -ForegroundColor Yellow
    Write-Host "   python -m venv venv" -ForegroundColor Yellow
    Write-Host "   pip install -r requirements.txt" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Pressione Enter para sair"
    exit 1
}

# Ativar ambiente virtual
Write-Host "Ativando ambiente virtual..." -ForegroundColor Green
& .\venv\Scripts\Activate.ps1

Write-Host ""
Write-Host "Executando main.py..." -ForegroundColor Green
Write-Host "Pressione 'q' na janela para sair." -ForegroundColor Yellow
Write-Host ""

# Executar o script
python main.py

Write-Host ""
Write-Host "Programa finalizado." -ForegroundColor Green
Read-Host "Pressione Enter para sair"

