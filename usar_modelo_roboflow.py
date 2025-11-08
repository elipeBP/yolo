"""
Script para usar modelo treinado no Roboflow
"""
import cv2
from ultralytics import YOLO
import os

def baixar_modelo_roboflow():
    """Baixa o modelo treinado do Roboflow"""
    try:
        from roboflow import Roboflow
        
        print("=" * 60)
        print("  Download do Modelo Treinado do Roboflow")
        print("=" * 60)
        print()
        
        print("📋 Você precisa das seguintes informações do Roboflow:")
        print("   1. Workspace (ex: 'car-parts-o7dlr')")
        print("   2. Project (ex: 'car-parts')")
        print("   3. Version (ex: 1)")
        print()
        print("💡 Essas informações estão na URL do seu modelo:")
        print("   Model URL: car-parts-o7dlr-hrfvd/1")
        print("   └─ workspace: car-parts-o7dlr")
        print("   └─ project: car-parts")
        print("   └─ version: 1")
        print()
        
        workspace = input("Digite o workspace: ").strip()
        project = input("Digite o project: ").strip()
        version = input("Digite a version (número): ").strip()
        
        # API key (pode ser None para datasets públicos)
        api_key = input("Digite sua API key do Roboflow (ou Enter se for público): ").strip()
        if not api_key:
            api_key = None
        
        print("\n📥 Baixando modelo...")
        
        rf = Roboflow(api_key=api_key)
        project_obj = rf.workspace(workspace).project(project)
        model = project_obj.version(int(version)).model
        
        print("✅ Modelo baixado!")
        print(f"📁 Modelo salvo em: {model}")
        
        return str(model)
        
    except Exception as e:
        print(f"\n❌ Erro ao baixar modelo: {e}")
        print("\n💡 Alternativa: Baixe manualmente do Roboflow")
        print("   1. Vá na página do seu modelo treinado")
        print("   2. Clique em 'Download' → 'YOLOv11'")
        print("   3. Extraia o arquivo .pt")
        return None

def usar_modelo_local(caminho_modelo):
    """Usa o modelo baixado para detecção em tempo real"""
    if not os.path.exists(caminho_modelo):
        print(f"❌ Modelo não encontrado: {caminho_modelo}")
        return
    
    print("\n🚀 Carregando modelo...")
    model = YOLO(caminho_modelo)
    
    print("✅ Modelo carregado!")
    print("📹 Abrindo webcam...")
    print("💡 Pressione 'q' para sair\n")
    
    cap = cv2.VideoCapture(0)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Realizar detecção
        results = model(frame)
        
        # Exibir resultados
        frame = results[0].plot()
        cv2.imshow("Detecção de Peças de Carro - Roboflow", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print("\n✅ Programa finalizado!")

if __name__ == "__main__":
    print("=" * 60)
    print("  Usar Modelo Treinado no Roboflow")
    print("=" * 60)
    print()
    
    print("📌 IMPORTANTE: Aguarde o treinamento terminar no Roboflow!")
    print("   Você receberá um email quando estiver pronto.")
    print()
    
    resposta = input("O treinamento já terminou? (s/n): ").strip().lower()
    
    if resposta != 's':
        print("\n⏳ Aguarde o treinamento terminar no Roboflow.")
        print("   Quando receber o email, execute este script novamente.")
        exit(0)
    
    print("\n📥 Como você quer obter o modelo?")
    print("   1. Baixar automaticamente via API")
    print("   2. Já tenho o arquivo .pt baixado")
    
    opcao = input("\nEscolha (1 ou 2): ").strip()
    
    if opcao == "1":
        caminho = baixar_modelo_roboflow()
        if caminho:
            usar_modelo_local(caminho)
    elif opcao == "2":
        caminho = input("Digite o caminho do arquivo .pt: ").strip()
        usar_modelo_local(caminho)
    else:
        print("❌ Opção inválida!")

