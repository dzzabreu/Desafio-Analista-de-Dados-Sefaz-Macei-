import sys
from src.extract_data import descompactar_dados
from src.merge_data import consolida_parquet
from src.load_duckdb import carregar_dados_duckdb

def main():
    print("==================================================")
    print("   Iniciando Pipeline de Dados - Sefaz Maceió")
    print("==================================================")
    
    try:
        # Passo 1: Executa a extração/descompactação
        descompactar_dados()
        
        # Passo 2 e 3: Consolidação dos dados em formato performático (Parquet)
        consolida_parquet()
        
        # Passo 4: Carga no DuckDB
        msg_duckdb = carregar_dados_duckdb()  # <-- NOVO PASSO
        print(f"{msg_duckdb}")
        
        print("\n==================================================")
        print("    Pipeline executado com sucesso absoluto!")
        print("==================================================")
        
    except Exception as e:
        print(f"\nErro crítico durante a execução do pipeline: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()