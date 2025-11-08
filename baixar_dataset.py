"""
Script para baixar datasets gratuitos de peças de carro
"""
import os
import subprocess
import sys

def instalar_roboflow():
    """Instala a biblioteca roboflow se não estiver instalada"""
    try:
        import roboflow
        print("✅ Roboflow já está instalado!")
        return True
    except ImportError:
        print("📦 Instalando Roboflow...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "roboflow"])
            print("✅ Roboflow instalado com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao instalar Roboflow: {e}")
            return False

def listar_datasets_uteis():
    """Lista datasets úteis disponíveis"""
    print("\n" + "=" * 60)
    print("  DATASETS GRATUITOS DISPONÍVEIS")
    print("=" * 60)
    print()
    
    datasets = [
        {
            "nome": "Car Parts Segmentation",
            "workspace": "roboflow-universe-1",
            "projeto": "carparts-seg",
            "versao": 1,
            "descricao": "Dataset de segmentação de peças de carro (Roboflow Universe)",
            "tipo": "segmentação"
        },
        {
            "nome": "Car Parts Detection",
            "workspace": "roboflow-universe-1", 
            "projeto": "car-parts-detection",
            "versao": 1,
            "descricao": "Dataset de detecção de peças de carro",
            "tipo": "detecção"
        },
        {
            "nome": "Automotive Parts",
            "workspace": "roboflow-universe-1",
            "projeto": "automotive-parts",
            "versao": 1,
            "descricao": "Peças automotivas diversas",
            "tipo": "detecção"
        }
    ]
    
    print("📋 Opções disponíveis:\n")
    for i, ds in enumerate(datasets, 1):
        print(f"{i}. {ds['nome']}")
        print(f"   Tipo: {ds['tipo']}")
        print(f"   Descrição: {ds['descrição']}")
        print(f"   Workspace: {ds['workspace']}/{ds['projeto']}")
        print()
    
    return datasets

def baixar_dataset_roboflow(workspace, projeto, versao=1):
    """Baixa dataset do Roboflow"""
    try:
        from roboflow import Roboflow
        
        print(f"\n📥 Baixando dataset: {workspace}/{projeto}...")
        print("💡 Isso pode levar alguns minutos dependendo do tamanho...")
        
        # Roboflow permite acesso público sem API key para datasets públicos
        rf = Roboflow()
        project = rf.workspace(workspace).project(projeto)
        dataset = project.version(versao).download("yolov11")
        
        print(f"\n✅ Dataset baixado com sucesso!")
        print(f"📁 Localização: {dataset.location}")
        
        return dataset.location
        
    except Exception as e:
        print(f"\n❌ Erro ao baixar dataset: {e}")
        print("\n💡 Possíveis causas:")
        print("   - Dataset não existe ou não é público")
        print("   - Problema de conexão")
        print("   - Nome do workspace/projeto incorreto")
        return None

def preparar_dataset_baixado(caminho_origem):
    """Prepara dataset baixado para usar com nosso sistema"""
    import shutil
    from pathlib import Path
    
    print("\n🔄 Preparando dataset...")
    
    # Estrutura típica do Roboflow
    # dataset/
    #   train/
    #   valid/
    #   test/
    #   data.yaml
    
    caminho = Path(caminho_origem)
    
    # Verificar estrutura
    if not (caminho / "train").exists():
        print("❌ Estrutura do dataset não reconhecida!")
        return False
    
    # Criar estrutura do nosso sistema
    os.makedirs("dataset/images/train", exist_ok=True)
    os.makedirs("dataset/images/val", exist_ok=True)
    os.makedirs("dataset/images/test", exist_ok=True)
    os.makedirs("dataset/labels/train", exist_ok=True)
    os.makedirs("dataset/labels/val", exist_ok=True)
    os.makedirs("dataset/labels/test", exist_ok=True)
    
    # Copiar arquivos
    def copiar_pasta(origem, destino_img, destino_label):
        origem_path = caminho / origem
        if origem_path.exists():
            # Copiar imagens
            for img in origem_path.glob("*.jpg"):
                shutil.copy(img, destino_img / img.name)
            for img in origem_path.glob("*.png"):
                shutil.copy(img, destino_img / img.name)
            
            # Copiar labels
            for label in origem_path.glob("*.txt"):
                shutil.copy(label, destino_label / label.name)
    
    copiar_pasta("train", Path("dataset/images/train"), Path("dataset/labels/train"))
    copiar_pasta("valid", Path("dataset/images/val"), Path("dataset/labels/val"))
    copiar_pasta("test", Path("dataset/images/test"), Path("dataset/labels/test"))
    
    # Copiar data.yaml se existir
    if (caminho / "data.yaml").exists():
        shutil.copy(caminho / "data.yaml", "dataset/data.yaml")
        print("✅ Arquivo data.yaml copiado!")
    else:
        # Criar data.yaml básico
        with open("dataset/data.yaml", "w", encoding="utf-8") as f:
            f.write("""path: dataset
train: images/train
val: images/val
test: images/test

names:
  0: peca_carro

nc: 1
""")
        print("✅ Arquivo data.yaml criado!")
    
    print("✅ Dataset preparado com sucesso!")
    return True

if __name__ == "__main__":
    print("=" * 60)
    print("  Download de Datasets Gratuitos")
    print("=" * 60)
    
    # Instalar roboflow
    if not instalar_roboflow():
        print("\n❌ Não foi possível instalar Roboflow.")
        print("💡 Tente manualmente: pip install roboflow")
        exit(1)
    
    # Listar opções
    datasets = listar_datasets_uteis()
    
    print("\n" + "=" * 60)
    print("💡 COMO USAR:")
    print("=" * 60)
    print()
    print("1. Acesse: https://universe.roboflow.com/")
    print("2. Busque por 'car parts' ou 'automotive'")
    print("3. Escolha um dataset público")
    print("4. Clique em 'Download' → 'YOLOv11'")
    print("5. Extraia o arquivo ZIP")
    print("6. Execute este script novamente com o caminho")
    print()
    print("OU use diretamente pelo código Python:")
    print()
    print("```python")
    print("from roboflow import Roboflow")
    print("rf = Roboflow()")
    print("project = rf.workspace('roboflow-universe-1').project('carparts-seg')")
    print("dataset = project.version(1).download('yolov11')")
    print("```")
    print()
    
    # Perguntar se quer baixar automaticamente
    resposta = input("Deseja tentar baixar o dataset 'Car Parts Segmentation' automaticamente? (s/n): ")
    
    if resposta.lower() == 's':
        caminho = baixar_dataset_roboflow("roboflow-universe-1", "carparts-seg", 1)
        if caminho:
            preparar_dataset_baixado(caminho)
            print("\n✅ Pronto! Agora você pode executar: python treinar.py")
    else:
        print("\n💡 Para usar um dataset baixado manualmente:")
        print("   1. Baixe o dataset do Roboflow Universe")
        print("   2. Extraia na pasta do projeto")
        print("   3. Execute: python preparar_dataset.py")
    
    print("\n" + "=" * 60)

