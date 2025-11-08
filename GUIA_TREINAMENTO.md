# 🎯 Guia de Treinamento MVP - Detecção de Peça de Carro

Este guia vai te ajudar a treinar um modelo YOLOv11 para reconhecer uma peça de carro específica.

## 📋 O que você precisa

1. **Imagens da peça** (mínimo 100, ideal 300+)
2. **Tempo**: 2-4 horas para coletar e anotar + tempo de treino
3. **Ferramenta de anotação**: LabelImg (gratuita)

## 🚀 Passo a Passo

### 1. Coletar Imagens

**Onde conseguir:**
- Tire fotos da peça em diferentes:
  - Ângulos (frente, lado, cima, baixo)
  - Iluminações (claro, escuro, sombra)
  - Fundos (diferentes ambientes)
  - Distâncias (perto, longe)
- **Mínimo**: 100 imagens
- **Ideal**: 300-500 imagens
- **Formato**: JPG ou PNG

**Dica**: Use seu celular e tire muitas fotos variadas!

### 2. Instalar LabelImg (Ferramenta de Anotação)

**Windows:**
```bash
pip install labelimg
```

Depois execute:
```bash
labelimg
```

**OU baixe direto:**
- https://github.com/HumanSignal/labelImg/releases
- Baixe o arquivo `.exe` para Windows

### 3. Anotar as Imagens

1. Abra o LabelImg
2. Abra a pasta com suas imagens
3. Para cada imagem:
   - Clique em "Create RectBox" ou pressione `W`
   - Desenhe um retângulo ao redor da peça
   - Digite o nome da classe (ex: `peca_carro`)
   - Salve (Ctrl+S)
4. Isso cria arquivos `.txt` com as coordenadas

**Dica**: Anote pelo menos 50-100 imagens para começar o MVP.

### 4. Organizar o Dataset

Coloque todas as imagens e labels na pasta `fotos_brutas`:

```
fotos_brutas/
├── imagem1.jpg
├── imagem1.txt
├── imagem2.jpg
├── imagem2.txt
...
```

Depois execute:
```bash
python preparar_dataset.py
```

Isso vai:
- Criar a estrutura de pastas
- Dividir automaticamente em treino/validação/teste
- Criar o arquivo `data.yaml`

### 5. Treinar o Modelo

Execute:
```bash
python treinar.py
```

**Tempo estimado:**
- CPU: 2-6 horas (dependendo do número de imagens)
- GPU: 15-60 minutos

### 6. Usar o Modelo Treinado

Após o treino, o melhor modelo estará em:
```
runs/detect/peca_carro_mvp/weights/best.pt
```

Para usar no seu código:
```python
from ultralytics import YOLO

# Carregar modelo treinado
model = YOLO("runs/detect/peca_carro_mvp/weights/best.pt")

# Usar para detecção
results = model("caminho/para/imagem.jpg")
```

## 📁 Estrutura Final

```
projeto/
├── fotos_brutas/          # Suas imagens e labels originais
├── dataset/                # Dataset organizado
│   ├── images/
│   │   ├── train/
│   │   ├── val/
│   │   └── test/
│   ├── labels/
│   │   ├── train/
│   │   ├── val/
│   │   └── test/
│   └── data.yaml
├── runs/                   # Resultados do treinamento
│   └── detect/
│       └── peca_carro_mvp/
│           └── weights/
│               └── best.pt  # Seu modelo treinado!
├── treinar.py
├── preparar_dataset.py
└── main.py
```

## ⚙️ Ajustes e Melhorias

### Se o modelo não estiver bom:

1. **Adicione mais imagens** (principal causa de problemas)
2. **Melhore as anotações** (certifique-se que estão corretas)
3. **Aumente as épocas** no `treinar.py` (mude `epochs=50` para `epochs=100`)
4. **Use modelo maior**: mude `yolo11n.pt` para `yolo11s.pt` ou `yolo11m.pt`

### Erros comuns:

**"Out of memory" (erro de memória):**
- Reduza o `batch` no `treinar.py` (de 16 para 8 ou 4)

**"No labels found":**
- Verifique se os arquivos `.txt` estão na pasta `labels/`
- Verifique se o formato está correto (YOLO format)

## 💡 Dicas para MVP

1. **Comece simples**: 50-100 imagens bem anotadas são melhores que 500 mal anotadas
2. **Foque na qualidade**: Imagens variadas são mais importantes que quantidade
3. **Teste rápido**: Treine com poucas épocas primeiro (20-30) para ver se funciona
4. **Itere**: Se não funcionar, adicione mais imagens e treine novamente

## 🎯 Resultado Esperado

Após o treinamento, você terá um modelo que:
- Detecta a peça de carro em novas imagens
- Mostra um retângulo ao redor da peça
- Funciona em tempo real com webcam (adaptando o `main.py`)

---

**Tempo total estimado para MVP**: 3-6 horas
- Coleta de imagens: 1-2h
- Anotação: 1-2h  
- Treinamento: 1-2h

Boa sorte! 🚀

