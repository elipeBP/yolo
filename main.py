import cv2


from ultralytics import YOLO

# Carregar modelo pré-treinado
#model = YOLO("yolo11n.pt")  # detecção
#model = YOLO("yolo11n-seg.pt") # segmentação
#model = YOLO("yolo11n-pose.pt") # pose

# Seu modelo treinado para detectar peças de carro
model = YOLO("runs/detect/car_parts_treinado/weights/best.pt")

# Modelos pré-treinados (alternativas)
#model = YOLO("yolo11n.pt")  # detecção geral
#model = YOLO("yolo11n-seg.pt") # segmentação
#model = YOLO("yolo11n-pose.pt") # pose

# Abrir a webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Realizar inferência
    results = model(frame)

    # Exibir resultados
    frame = results[0].plot()
    cv2.imshow("Detecção de Peças de Carro", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Pressione 'q' para sair
        break

cap.release()
cv2.destroyAllWindows()
