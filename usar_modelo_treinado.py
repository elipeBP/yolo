"""
Script para usar o modelo treinado para detectar peça de carro
"""
import cv2
from ultralytics import YOLO
import os

# Caminho do modelo treinado
modelo_treinado = "runs/detect/peca_carro_mvp/weights/best.pt"

# Verificar se o modelo existe
if not os.path.exists(modelo_treinado):
    print("❌ Modelo treinado não encontrado!")
    print(f"   Procurando em: {modelo_treinado}")
    print("\n💡 Você precisa treinar o modelo primeiro:")
    print("   1. Execute: python preparar_dataset.py")
    print("   2. Execute: python treinar.py")
    exit(1)

print("🚀 Carregando modelo treinado...")
model = YOLO(modelo_treinado)

print("✅ Modelo carregado!")
print("📹 Abrindo webcam...")
print("💡 Pressione 'q' para sair\n")

# Abrir webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Realizar detecção
    results = model(frame)

    # Exibir resultados
    frame = results[0].plot()
    cv2.imshow("Detecção de Peça de Carro", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("\n✅ Programa finalizado!")

