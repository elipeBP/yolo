"""
Treinar modelo com dataset do Roboflow (carparts)
"""
from ultralytics import YOLO
import os

print("=" * 60)
print("  Treinamento - Detecção de Peças de Carro")
print("=" * 60)
print()

# Verificar se o dataset existe
if not os.path.exists("carparts/data.yaml"):
    print("❌ ERRO: Dataset não encontrado!")
    print("💡 Certifique-se que a pasta 'carparts' está na raiz do projeto")
    exit(1)

print("📊 Dataset encontrado!")
print("   - Train: 2.796 imagens")
print("   - Valid: 328 imagens")
print("   - Test: 167 imagens")
print("   - Classes: 20 peças de carro")
print()

# Carregar modelo base
print("🚀 Carregando modelo base YOLOv11n...")
model = YOLO("yolo11n.pt")

print("\n⚙️  Configurações de treinamento (otimizadas para seu hardware):")
print("   - Modelo: YOLOv11n (nano - rápido)")
print("   - Épocas: 50")
print("   - Imagens: 640x640")
print("   - Batch: 8 (reduzido para 12GB RAM + CPU)")
print("   - Device: CPU (sem GPU dedicada)")
print()
print("⏱️  Tempo estimado: 6-12 horas (CPU)")
print("💡 Dica: Deixe rodando durante a noite ou quando não usar o PC")
print()
print("🚀 Iniciando treinamento automaticamente...")
print()

print("\n" + "=" * 60)
print("  INICIANDO TREINAMENTO")
print("=" * 60)
print()
print("⏱️  Tempo estimado: 2-6 horas (depende do seu PC)")
print("💡 Você pode fechar este terminal, mas o treinamento vai parar")
print("💡 Para acompanhar, deixe aberto")
print()

# Treinar
try:
    results = model.train(
        data="carparts/data.yaml",
        epochs=50,
        imgsz=640,
        batch=8,  # Reduzido para 12GB RAM (era 16)
        name="car_parts_treinado",
        project="runs/detect",
        patience=10,
        save=True,
        plots=True,
        device='cpu',  # Força CPU (você não tem GPU dedicada)
        workers=4,  # Otimizado para Ryzen 7
    )
    
    print("\n" + "=" * 60)
    print("  ✅ TREINAMENTO CONCLUÍDO!")
    print("=" * 60)
    print()
    print(f"📊 Resultados salvos em: runs/detect/car_parts_treinado/")
    print(f"🎯 Melhor modelo: runs/detect/car_parts_treinado/weights/best.pt")
    print()
    print("💡 Para usar o modelo treinado:")
    print("   from ultralytics import YOLO")
    print("   model = YOLO('runs/detect/car_parts_treinado/weights/best.pt')")
    print()
    
except KeyboardInterrupt:
    print("\n\n⚠️  Treinamento interrompido pelo usuário.")
    print("💡 O modelo parcial está salvo em: runs/detect/car_parts_treinado/")
    
except Exception as e:
    print(f"\n\n❌ Erro durante o treinamento: {e}")
    print("\n💡 Possíveis soluções:")
    print("   - Reduza o batch para 8 ou 4")
    print("   - Verifique se tem espaço em disco")
    print("   - Verifique se o dataset está completo")

