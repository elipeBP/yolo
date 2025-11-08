"""
Script para organizar e preparar o dataset para treinamento
"""
import os
import shutil
from pathlib import Path
import random

def criar_estrutura():
    """Cria a estrutura de pastas necessária"""
    pastas = [
        "dataset/images/train",
        "dataset/images/val",
        "dataset/images/test",
        "dataset/labels/train",
        "dataset/labels/val",
        "dataset/labels/test"
    ]
    
    for pasta in pastas:
        os.makedirs(pasta, exist_ok=True)
    
    print("✅ Estrutura de pastas criada!")

def criar_data_yaml():
    """Cria o arquivo data.yaml necessário para o treinamento"""
    yaml_content = """# Dataset para treinamento de detecção de peça de carro
path: dataset  # Caminho relativo ao dataset
train: images/train  # Pasta de imagens de treino
val: images/val       # Pasta de imagens de validação
test: images/test     # Pasta de imagens de teste

# Nome da classe (sua peça de carro)
names:
  0: peca_carro  # Altere para o nome da sua peça (ex: para_choque, roda, etc)

# Número de classes
nc: 1
"""
    
    with open("dataset/data.yaml", "w", encoding="utf-8") as f:
        f.write(yaml_content)
    
    print("✅ Arquivo data.yaml criado!")

def organizar_imagens(pasta_origem, proporcao_train=0.7, proporcao_val=0.2):
    """
    Organiza imagens automaticamente dividindo em train/val/test
    
    Args:
        pasta_origem: Pasta com todas as imagens e labels
        proporcao_train: Proporção para treino (padrão 70%)
        proporcao_val: Proporção para validação (padrão 20%)
        # Teste será o restante (10%)
    """
    if not os.path.exists(pasta_origem):
        print(f"❌ Pasta '{pasta_origem}' não encontrada!")
        print("\n💡 Coloque todas as imagens e labels na pasta 'fotos_brutas'")
        return
    
    # Buscar todas as imagens
    extensoes = ['.jpg', '.jpeg', '.png', '.bmp']
    imagens = []
    
    for ext in extensoes:
        imagens.extend(Path(pasta_origem).glob(f"*{ext}"))
        imagens.extend(Path(pasta_origem).glob(f"*{ext.upper()}"))
    
    if not imagens:
        print(f"❌ Nenhuma imagem encontrada em '{pasta_origem}'!")
        return
    
    print(f"📸 Encontradas {len(imagens)} imagens")
    
    # Embaralhar
    random.shuffle(imagens)
    
    # Dividir
    total = len(imagens)
    train_count = int(total * proporcao_train)
    val_count = int(total * proporcao_val)
    
    train_imgs = imagens[:train_count]
    val_imgs = imagens[train_count:train_count + val_count]
    test_imgs = imagens[train_count + val_count:]
    
    print(f"📊 Divisão:")
    print(f"   Treino: {len(train_imgs)} imagens ({len(train_imgs)/total*100:.1f}%)")
    print(f"   Validação: {len(val_imgs)} imagens ({len(val_imgs)/total*100:.1f}%)")
    print(f"   Teste: {len(test_imgs)} imagens ({len(test_imgs)/total*1:.1f}%)")
    
    # Copiar imagens e labels
    def copiar_arquivos(lista_imgs, tipo):
        for img_path in lista_imgs:
            # Copiar imagem
            shutil.copy(img_path, f"dataset/images/{tipo}/{img_path.name}")
            
            # Copiar label correspondente (se existir)
            label_path = img_path.with_suffix('.txt')
            if label_path.exists():
                shutil.copy(label_path, f"dataset/labels/{tipo}/{label_path.name}")
            else:
                print(f"⚠️  Label não encontrado: {label_path.name}")
    
    print("\n📁 Copiando arquivos...")
    copiar_arquivos(train_imgs, "train")
    copiar_arquivos(val_imgs, "val")
    copiar_arquivos(test_imgs, "test")
    
    print("✅ Dataset organizado com sucesso!")

if __name__ == "__main__":
    print("=" * 50)
    print("  Preparação de Dataset para Treinamento")
    print("=" * 50)
    print()
    
    # Criar estrutura
    criar_estrutura()
    criar_data_yaml()
    
    # Organizar imagens (se existir pasta fotos_brutas)
    if os.path.exists("fotos_brutas"):
        print("\n📸 Organizando imagens de 'fotos_brutas'...")
        organizar_imagens("fotos_brutas")
    else:
        print("\n💡 Para organizar imagens automaticamente:")
        print("   1. Crie uma pasta chamada 'fotos_brutas'")
        print("   2. Coloque todas as imagens e labels (.txt) lá")
        print("   3. Execute este script novamente")
    
    print("\n" + "=" * 50)
    print("✅ Preparação concluída!")
    print("\n📋 Próximos passos:")
    print("   1. Anote suas imagens usando LabelImg (se ainda não fez)")
    print("   2. Execute: python treinar.py")
    print("=" * 50)

