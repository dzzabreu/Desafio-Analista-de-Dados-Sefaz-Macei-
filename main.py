import sys
from src.extract_data import descompactar_dados
from src.merge_data import consolidar_dados

def main():
    print("==================================================")
    print("   Iniciando Pipeline de Dados - Sefaz Maceió")
    print("==================================================")
    
    try:
        # Passo 1: Executa a extração/descompactação
        descompactar_dados()
        
        # Passo 2 e 3: Consolidação dos dados em formato performático (Parquet)
        consolidar_dados()
        
        print("\n==================================================")
        print("    Pipeline executado com sucesso absoluto!")
        print("==================================================")
        
    except Exception as e:
        print(f"\nErro crítico durante a execução do pipeline: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()