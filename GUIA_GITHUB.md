# 🚀 Guia: Criar Repositório no GitHub

Este guia irá ajudá-lo a criar um repositório no GitHub e fazer o upload do seu projeto.

## 📋 Pré-requisitos

- Conta no GitHub (se não tiver, crie em: https://github.com/signup)
- Git instalado (já está instalado ✅)

## 🔧 Passo a Passo

### 1. Criar o Repositório no GitHub

1. Acesse: https://github.com/new
2. Preencha os dados:
   - **Repository name**: `yolov11-detection` (ou outro nome de sua preferência)
   - **Description**: `Sistema de detecção YOLOv11 para Windows 11`
   - **Visibility**: Escolha **Public** ou **Private**
   - ⚠️ **NÃO marque** "Add a README file" (já temos um)
   - ⚠️ **NÃO marque** "Add .gitignore" (já temos um)
   - ⚠️ **NÃO marque** "Choose a license" (opcional)
3. Clique em **"Create repository"**

### 2. Conectar o Repositório Local ao GitHub

Após criar o repositório, o GitHub mostrará comandos. Use estes comandos (substitua `SEU_USUARIO` pelo seu nome de usuário do GitHub):

```bash
# Adicionar o repositório remoto (substitua SEU_USUARIO e NOME_DO_REPO)
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPO.git

# Renomear branch para main (se necessário)
git branch -M main

# Fazer o push
git push -u origin main
```

### 3. Autenticação

Se for a primeira vez, o GitHub pode pedir autenticação:

**Opção A: Personal Access Token (Recomendado)**
1. Vá em: https://github.com/settings/tokens
2. Clique em "Generate new token (classic)"
3. Dê um nome e selecione o escopo `repo`
4. Copie o token gerado
5. Quando o Git pedir senha, use o token ao invés da senha

**Opção B: GitHub CLI**
```bash
# Instalar GitHub CLI (se ainda não tiver)
# Baixe de: https://cli.github.com/

# Autenticar
gh auth login
```

## 🎯 Comandos Rápidos (Copie e Cole)

Depois de criar o repositório no GitHub, execute estes comandos (substitua `SEU_USUARIO` e `NOME_DO_REPO`):

```bash
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPO.git
git branch -M main
git push -u origin main
```

## 📝 Próximos Passos

Depois do primeiro push, para fazer atualizações futuras:

```bash
git add .
git commit -m "Descrição da alteração"
git push
```

## ✅ Verificação

Após o push, acesse seu repositório no GitHub e verifique se todos os arquivos foram enviados corretamente!

---

**Dica:** Se encontrar algum erro, verifique:
- Se o nome do repositório está correto
- Se você tem permissão para fazer push
- Se a autenticação está configurada corretamente

