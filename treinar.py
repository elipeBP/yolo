"""
Script de Treinamento YOLOv11 - MVP para Detecção de Peça de Carro
"""
from ultralytics import YOLO
import os

# Verificar se o dataset existe
if not os.path.exists("dataset"):
    print("❌ ERRO: Pasta 'dataset' não encontrada!")
    print("\n📁 Estrutura necessária:")
    print("   dataset/")
    print("   ├── images/")
    print("   │   ├── train/")
    print("   │   ├── val/")
    print("   │   └── test/")
    print("   └── labels/")
    print("       ├── train/")
    print("       ├── val/")
    print("       └── test/")
    print("\n💡 Use o script preparar_dataset.py para organizar automaticamente!")
    exit(1)

# Carregar modelo pré-treinado (transfer learning)
print("🚀 Iniciando treinamento...")
print("📦 Carregando modelo base YOLOv11n...")

# Usar modelo nano (mais rápido para MVP)
model = YOLO("yolo11n.pt")

# Configurações de treinamento para MVP
print("\n⚙️  Configurações:")
print("   - Modelo: YOLOv11n (nano - rápido)")
print("   - Épocas: 50 (ajuste conforme necessário)")
print("   - Imagens: 640x640")
print("   - Batch: 16 (reduza se der erro de memória)")

# Treinar
results = model.train(
    data="dataset/data.yaml",  # Arquivo de configuração do dataset
    epochs=50,                 # Número de épocas (iterações)
    imgsz=640,                 # Tamanho da imagem
    batch=16,                   # Tamanho do batch (reduza para 8 ou 4 se der erro)
    name="peca_carro_mvp",     # Nome do experimento
    project="runs/detect",      # Pasta de resultados
    patience=10,                # Parar se não melhorar em 10 épocas
    save=True,                  # Salvar checkpoints
    plots=True,                 # Gerar gráficos
)

print("\n✅ Treinamento concluído!")
print(f"📊 Resultados salvos em: runs/detect/peca_carro_mvp/")
print(f"🎯 Melhor modelo: runs/detect/peca_carro_mvp/weights/best.pt")
print("\n💡 Para usar o modelo treinado:")
print("   model = YOLO('runs/detect/peca_carro_mvp/weights/best.pt')")

