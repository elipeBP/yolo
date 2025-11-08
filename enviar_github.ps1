# Script para enviar o projeto para o GitHub
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Enviar Projeto para GitHub" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se já existe um remote
$remoteExists = git remote -v 2>$null
if ($remoteExists) {
    Write-Host "Repositório remoto já configurado:" -ForegroundColor Yellow
    git remote -v
    Write-Host ""
    $opcao = Read-Host "Deseja adicionar um novo remote? (s/n)"
    if ($opcao -ne "s") {
        Write-Host "Fazendo push para o repositório existente..." -ForegroundColor Green
        git push -u origin main
        exit 0
    }
}

Write-Host "IMPORTANTE: Primeiro crie o repositório no GitHub!" -ForegroundColor Yellow
Write-Host "Acesse: https://github.com/new" -ForegroundColor Yellow
Write-Host ""
Write-Host "Depois de criar, informe:" -ForegroundColor Cyan
Write-Host ""

$usuario = Read-Host "Seu nome de usuário do GitHub"
$repo = Read-Host "Nome do repositório (ex: yolov11-detection)"

if ([string]::IsNullOrWhiteSpace($usuario) -or [string]::IsNullOrWhiteSpace($repo)) {
    Write-Host "[ERRO] Usuário e repositório são obrigatórios!" -ForegroundColor Red
    exit 1
}

$url = "https://github.com/$usuario/$repo.git"

Write-Host ""
Write-Host "Configurando repositório remoto..." -ForegroundColor Green
git remote add origin $url

Write-Host "Renomeando branch para main..." -ForegroundColor Green
git branch -M main

Write-Host ""
Write-Host "Fazendo push para o GitHub..." -ForegroundColor Green
Write-Host "Se pedir autenticação, use um Personal Access Token" -ForegroundColor Yellow
Write-Host "Crie um token em: https://github.com/settings/tokens" -ForegroundColor Yellow
Write-Host ""

git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ Projeto enviado com sucesso!" -ForegroundColor Green
    Write-Host "Acesse: $url" -ForegroundColor Cyan
} else {
    Write-Host ""
    Write-Host "❌ Erro ao fazer push. Verifique:" -ForegroundColor Red
    Write-Host "  1. Se o repositório foi criado no GitHub" -ForegroundColor Yellow
    Write-Host "  2. Se o nome do usuário e repositório estão corretos" -ForegroundColor Yellow
    Write-Host "  3. Se você tem permissão para fazer push" -ForegroundColor Yellow
    Write-Host "  4. Se a autenticação está configurada" -ForegroundColor Yellow
}

Write-Host ""
Read-Host "Pressione Enter para sair"

