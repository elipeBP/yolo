# 📦 Datasets Gratuitos para Treinamento

Lista de datasets gratuitos que podem ajudar no treinamento do seu modelo de detecção de peças de carro.

## 🎯 Melhores Opções

### 1. Roboflow Universe (RECOMENDADO)

**Site**: https://universe.roboflow.com/

**Vantagens:**
- ✅ Totalmente gratuito
- ✅ Já formatado para YOLO
- ✅ Interface visual fácil
- ✅ Muitos datasets de peças de carro

**Como usar:**
1. Acesse https://universe.roboflow.com/
2. Busque por: `car parts`, `automotive`, `car components`
3. Escolha um dataset público
4. Clique em "Download" → "YOLOv11"
5. Extraia o ZIP
6. Execute: `python preparar_dataset.py`

**Datasets recomendados:**
- `carparts-seg` - Segmentação de peças de carro
- `car-parts-detection` - Detecção de peças
- `automotive-parts` - Peças automotivas diversas

### 2. Kaggle

**Site**: https://www.kaggle.com/datasets

**Busque por:**
- "car parts detection"
- "automotive parts"
- "vehicle components"

**Como usar:**
1. Crie conta gratuita no Kaggle
2. Baixe o dataset
3. Converta para formato YOLO (pode precisar de conversão)

### 3. Open Images Dataset

**Site**: https://storage.googleapis.com/openimages/web/index.html

**Vantagens:**
- ✅ Milhões de imagens
- ✅ Inclui categorias de carros
- ✅ Gratuito

**Desvantagens:**
- ⚠️ Não é específico para peças
- ⚠️ Pode precisar filtrar e anotar

### 4. COCO Dataset

**Site**: https://cocodataset.org/

**Vantagens:**
- ✅ Dataset muito conhecido
- ✅ Inclui categoria "car"
- ✅ Bem anotado

**Desvantagens:**
- ⚠️ Não específico para peças individuais
- ⚠️ Focado em detecção de carros completos

## 🚀 Usando o Script Automático

Execute:
```bash
python baixar_dataset.py
```

O script vai:
1. Instalar Roboflow automaticamente
2. Listar datasets disponíveis
3. Tentar baixar automaticamente (se disponível)

## 💡 Dicas

1. **Combine datasets**: Use múltiplos datasets para mais variedade
2. **Filtre imagens**: Remova imagens ruins ou irrelevantes
3. **Adicione suas fotos**: Combine datasets públicos com suas próprias fotos
4. **Valide antes**: Use `python validar_dataset.py` antes de treinar

## 📊 Estrutura Esperada

Após baixar, o dataset deve ter:
```
dataset/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
├── labels/
│   ├── train/
│   ├── val/
│   └── test/
└── data.yaml
```

## ⚠️ Licenças

Sempre verifique a licença do dataset antes de usar:
- **CC0 / Public Domain**: Uso livre
- **CC BY**: Precisa dar crédito
- **CC BY-NC**: Não comercial
- **Custom**: Verificar termos específicos

## 🎯 Estratégia Recomendada

1. **Comece com Roboflow**: Baixe um dataset pronto
2. **Adicione suas fotos**: Complemente com imagens reais da sua peça
3. **Treine e ajuste**: Itere até ficar bom

---

**Tempo economizado**: De 6 horas para 1-2 horas! 🚀

