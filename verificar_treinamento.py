"""
Script para verificar o progresso do treinamento
"""
import sys
import os
from pathlib import Path

# Configurar encoding para Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

def verificar_progresso():
    """Verifica o progresso do treinamento"""
    caminho = Path("runs/detect/car_parts_treinado")
    
    if not caminho.exists():
        print("[INFO] Treinamento ainda nao comecou ou pasta nao criada ainda.")
        print("       Execute: python treinar_carparts.py")
        return
    
    # Verificar se tem weights
    weights_dir = caminho / "weights"
    if weights_dir.exists():
        best = weights_dir / "best.pt"
        last = weights_dir / "last.pt"
        
        if best.exists():
            tamanho = best.stat().st_size / (1024 * 1024)
            print(f"[OK] Modelo encontrado!")
            print(f"     Arquivo: {best}")
            print(f"     Tamanho: {tamanho:.2f} MB")
            print()
            print("Para usar:")
            print(f"  model = YOLO('{best}')")
            return True
        elif last.exists():
            tamanho = last.stat().st_size / (1024 * 1024)
            print(f"[EM ANDAMENTO] Treinamento rodando...")
            print(f"     Checkpoint atual: {last}")
            print(f"     Tamanho: {tamanho:.2f} MB")
            print()
            print("Dica: O modelo 'last.pt' e o checkpoint mais recente")
            print("      Voce pode usar mesmo durante o treinamento!")
            return False
    
    # Verificar resultados
    results_csv = caminho / "results.csv"
    if results_csv.exists():
        print("[EM ANDAMENTO] Treinamento rodando...")
        print(f"     Logs: {results_csv}")
        print()
        print("Dica: Abra o arquivo results.csv para ver metricas")
        
        # Tentar ler última linha do CSV
        try:
            with open(results_csv, 'r', encoding='utf-8') as f:
                linhas = f.readlines()
                if len(linhas) > 1:
                    print(f"     Epocas processadas: {len(linhas) - 1}")
                    print(f"     Ultima linha: {linhas[-1].strip()[:80]}...")
        except:
            pass
        
        return False
    
    print("[AGUARDANDO] Inicio do treinamento...")
    return False

if __name__ == "__main__":
    print("=" * 60)
    print("  Verificar Progresso do Treinamento")
    print("=" * 60)
    print()
    
    verificar_progresso()
    
    print()
    print("=" * 60)
    print("FORMAS DE ACOMPANHAR:")
    print("=" * 60)
    print()
    print("1. Execute este script periodicamente:")
    print("   python verificar_treinamento.py")
    print()
    print("2. Veja os logs em tempo real:")
    print("   Abra: runs/detect/car_parts_treinado/results.csv")
    print()
    print("3. Verifique os checkpoints:")
    print("   Pasta: runs/detect/car_parts_treinado/weights/")
    print("   - last.pt = checkpoint mais recente")
    print("   - best.pt = melhor modelo (quando terminar)")
    print()
    print("4. Veja os graficos (quando terminar):")
    print("   runs/detect/car_parts_treinado/results.png")
    print()

