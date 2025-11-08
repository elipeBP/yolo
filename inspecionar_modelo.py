"""
Script para inspecionar um arquivo .pt e ver o que tem dentro
"""
import os
import sys

def inspecionar_modelo(caminho):
    """Mostra informações sobre um modelo .pt"""
    
    if not os.path.exists(caminho):
        print(f"❌ Arquivo não encontrado: {caminho}")
        return
    
    # Tamanho do arquivo
    tamanho = os.path.getsize(caminho)
    tamanho_mb = tamanho / (1024 * 1024)
    
    print("=" * 60)
    print("  Informações do Modelo .pt")
    print("=" * 60)
    print(f"\n📁 Arquivo: {caminho}")
    print(f"📏 Tamanho: {tamanho_mb:.2f} MB ({tamanho:,} bytes)")
    
    # Tentar carregar com Ultralytics
    try:
        from ultralytics import YOLO
        
        print("\n🔄 Carregando modelo...")
        model = YOLO(caminho)
        
        print("\n✅ Modelo carregado com sucesso!")
        print("\n📊 Informações do Modelo:")
        print("-" * 60)
        
        # Informações básicas
        print(f"Tipo: {type(model).__name__}")
        
        # Tentar ver informações do modelo
        try:
            info = model.info(verbose=False)
            print(f"Parâmetros: {info.get('parameters', 'N/A')}")
        except:
            pass
        
        # Verificar se tem método para listar classes
        try:
            if hasattr(model, 'names'):
                print(f"\n🏷️  Classes detectadas: {len(model.names)}")
                for idx, nome in model.names.items():
                    print(f"   {idx}: {nome}")
        except:
            pass
        
        print("\n💡 Este modelo pode ser usado assim:")
        print("   from ultralytics import YOLO")
        print(f"   model = YOLO('{os.path.basename(caminho)}')")
        print("   results = model('imagem.jpg')")
        
    except ImportError:
        print("\n⚠️  Ultralytics não está instalado")
        print("   Instale com: pip install ultralytics")
        
    except Exception as e:
        print(f"\n❌ Erro ao carregar modelo: {e}")
        print("\n💡 O arquivo pode estar corrompido ou em formato incompatível")
    
    # Tentar carregar com PyTorch (mais técnico)
    try:
        import torch
        
        print("\n" + "=" * 60)
        print("  Detalhes Técnicos (PyTorch)")
        print("=" * 60)
        
        checkpoint = torch.load(caminho, map_location='cpu')
        
        print(f"\n📦 Chaves no arquivo:")
        for key in checkpoint.keys():
            tipo = type(checkpoint[key]).__name__
            if hasattr(checkpoint[key], '__len__'):
                try:
                    tamanho_item = len(checkpoint[key])
                    print(f"   - {key}: {tipo} (tamanho: {tamanho_item})")
                except:
                    print(f"   - {key}: {tipo}")
            else:
                print(f"   - {key}: {tipo}")
        
        # Tentar ver estrutura do modelo
        if 'model' in checkpoint or 'state_dict' in checkpoint:
            print("\n🧠 Estrutura da Rede Neural:")
            state = checkpoint.get('model', checkpoint.get('state_dict', {}))
            if isinstance(state, dict):
                print(f"   Camadas: {len(state)}")
                print("\n   Primeiras camadas:")
                for i, (nome, tensor) in enumerate(list(state.items())[:5]):
                    print(f"   - {nome}: {tensor.shape}")
                if len(state) > 5:
                    print(f"   ... e mais {len(state) - 5} camadas")
        
    except ImportError:
        print("\n⚠️  PyTorch não está instalado para análise detalhada")
    except Exception as e:
        print(f"\n⚠️  Não foi possível analisar com PyTorch: {e}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    print("=" * 60)
    print("  Inspecionar Arquivo .pt")
    print("=" * 60)
    print()
    
    if len(sys.argv) > 1:
        caminho = sys.argv[1]
    else:
        # Listar arquivos .pt disponíveis
        arquivos_pt = [f for f in os.listdir('.') if f.endswith('.pt')]
        
        if not arquivos_pt:
            print("❌ Nenhum arquivo .pt encontrado na pasta atual")
            caminho = input("\nDigite o caminho do arquivo .pt: ").strip()
        else:
            print("📁 Arquivos .pt encontrados:\n")
            for i, arquivo in enumerate(arquivos_pt, 1):
                tamanho = os.path.getsize(arquivo) / (1024 * 1024)
                print(f"   {i}. {arquivo} ({tamanho:.2f} MB)")
            
            print(f"\n   {len(arquivos_pt) + 1}. Digitar caminho manualmente")
            
            escolha = input("\nEscolha um arquivo (número): ").strip()
            
            try:
                idx = int(escolha) - 1
                if 0 <= idx < len(arquivos_pt):
                    caminho = arquivos_pt[idx]
                else:
                    caminho = input("Digite o caminho do arquivo .pt: ").strip()
            except:
                caminho = input("Digite o caminho do arquivo .pt: ").strip()
    
    inspecionar_modelo(caminho)

