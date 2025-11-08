# Guia Completo - Rodando YOLOv11 no Windows 11

Este guia irá ajudá-lo a configurar e executar o sistema de detecção YOLOv11 no Windows 11.

## 📋 Pré-requisitos

- Windows 11
- Python 3.10 ou superior (testado com Python 3.13.7)
- Webcam conectada ao computador
- Conexão com internet (para baixar dependências)

## 🚀 Instalação Rápida

### 1. Verificar Python

Abra o PowerShell ou Prompt de Comando e verifique se o Python está instalado:

```bash
python --version
```

Se não estiver instalado, baixe e instale o Python 3.10 ou superior de:
https://www.python.org/downloads/

**Importante:** Durante a instalação, marque a opção **"Add Python to PATH"**.

### 2. Criar e Ativar o Ambiente Virtual

Navegue até a pasta do projeto e crie o ambiente virtual:

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (PowerShell)
.\venv\Scripts\Activate.ps1

# OU (Prompt de Comando)
venv\Scripts\activate
```

Você saberá que o ambiente virtual está ativo quando ver `(venv)` no início da linha do terminal.

### 3. Instalar Dependências

Com o ambiente virtual ativado, atualize o pip e instale as dependências:

```bash
# Atualizar pip
python -m pip install --upgrade pip

# Instalar todas as dependências
pip install -r requirements.txt
```

Isso instalará automaticamente:
- PyTorch (framework de deep learning)
- Ultralytics (YOLOv11)
- OpenCV (processamento de vídeo)
- NumPy, Pillow e outras dependências

**Nota:** A instalação pode levar alguns minutos, especialmente o PyTorch.

### 4. Verificar Instalação

Para verificar se tudo foi instalado corretamente:

```bash
python -c "import torch; import ultralytics; import cv2; print('Tudo instalado com sucesso!')"
```

## 🎯 Executar o Sistema

### ⚠️ IMPORTANTE: Sempre Ative o Ambiente Virtual Primeiro!

**O erro mais comum é esquecer de ativar o ambiente virtual.** Se você receber um erro como `ModuleNotFoundError: No module named 'cv2'`, significa que você está usando o Python do sistema ao invés do Python do ambiente virtual.

### Executar o Script Principal

**Passo 1:** Ative o ambiente virtual:

```bash
# PowerShell
.\venv\Scripts\Activate.ps1

# OU Prompt de Comando
venv\Scripts\activate
```

**Passo 2:** Com o ambiente virtual ativado (você verá `(venv)` no início da linha), execute:

```bash
python main.py
```

### 🚀 Atalho Rápido (Script Batch)

Para facilitar, você pode usar o arquivo `executar.bat` que já faz tudo automaticamente:

```bash
# Basta clicar duas vezes no arquivo executar.bat
# OU executar no terminal:
executar.bat
```

O sistema irá:
1. Carregar o modelo YOLOv11 (pose detection)
2. Abrir a webcam (câmera 0)
3. Mostrar uma janela com as detecções em tempo real
4. Pressione **'q'** para sair

### Alterar o Modelo

Você pode alterar qual modelo usar editando o arquivo `main.py`:

```python
# Linha 9 - Descomente o modelo desejado:

# Detecção de objetos
model = YOLO("yolo11n.pt")

# Segmentação de objetos
# model = YOLO("yolo11n-seg.pt")

# Detecção de pose (padrão)
# model = YOLO("yolo11n-pose.pt")
```

## 📁 Estrutura do Projeto

```
unisenai_code/
│
├── venv/                 # Ambiente virtual (não versionar)
│
├── main.py               # Script principal
│
├── requirements.txt      # Dependências do projeto
│
├── executar.bat          # Script para executar (Windows - duplo clique)
├── executar.ps1          # Script para executar (PowerShell)
│
├── treinar.py            # Script para treinar modelo personalizado
├── preparar_dataset.py   # Script para organizar dataset
├── usar_modelo_treinado.py # Script para usar modelo treinado
├── usar_modelo_roboflow.py # Script para usar modelo do Roboflow
│
├── yolo11n.pt           # Modelo de detecção de objetos
├── yolo11n-pose.pt       # Modelo de detecção de pose
├── yolo11n-seg.pt        # Modelo de segmentação
│
├── README.md            # Este arquivo (guia completo)
└── .gitignore           # Arquivos ignorados pelo Git
```

## 🔧 Solução de Problemas

### Erro: "Python não é reconhecido como comando"

- Certifique-se de que o Python está instalado
- Verifique se o Python foi adicionado ao PATH durante a instalação
- Reinicie o terminal após instalar o Python

### Erro: "Não foi possível ativar o ambiente virtual"

**No PowerShell:**
Se receber um erro de política de execução, execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois tente ativar novamente.

### Erro: "Não foi possível abrir a câmera"

- Verifique se a webcam está conectada
- Certifique-se de que nenhum outro programa está usando a câmera
- Tente alterar o índice da câmera no código (linha 12):
  ```python
  cap = cv2.VideoCapture(1)  # Tente 1, 2, etc.
  ```

### Erro: "ModuleNotFoundError: No module named 'cv2'"

**Este é o erro mais comum!** Significa que você está usando o Python do sistema ao invés do Python do ambiente virtual.

**Solução:**
1. Certifique-se de que o ambiente virtual está ativado (deve aparecer `(venv)` no início da linha do terminal)
2. Se não estiver ativado, execute:
   ```bash
   # PowerShell
   .\venv\Scripts\Activate.ps1
   
   # OU Prompt de Comando
   venv\Scripts\activate
   ```
3. Depois execute novamente: `python main.py`

**Dica:** Use o script `executar.bat` ou `executar.ps1` que já faz tudo automaticamente!

### Performance Lenta

- O modelo está rodando na CPU por padrão
- Para usar GPU NVIDIA (CUDA), instale o PyTorch com suporte CUDA:
  - Visite: https://pytorch.org/get-started/locally/
  - Selecione sua configuração e instale a versão apropriada

## 💡 Dicas

1. **Sempre ative o ambiente virtual** antes de executar o script
2. **Use 'q' para sair** do programa quando a janela estiver aberta
3. **Feche outros programas** que possam estar usando a câmera
4. **Primeira execução** pode ser mais lenta (o modelo carrega na memória)

## 📚 Recursos Adicionais

- Documentação Ultralytics: https://docs.ultralytics.com/
- Documentação OpenCV: https://docs.opencv.org/
- Documentação PyTorch: https://pytorch.org/docs/

## ✅ Checklist de Instalação

- [ ] Python instalado e no PATH
- [ ] Ambiente virtual criado (`python -m venv venv`)
- [ ] Ambiente virtual ativado (aparece `(venv)` no terminal)
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Webcam conectada e funcionando
- [ ] Script executado com sucesso (`python main.py`)

## 🎓 Treinar Modelo Personalizado

**Resumo rápido:**
1. Execute `python preparar_dataset.py` para organizar
2. Execute `python treinar.py` para treinar
3. Use `python usar_modelo_treinado.py` para testar

---

**Desenvolvido para Windows 11** | **Python 3.10+** | **YOLOv11**

