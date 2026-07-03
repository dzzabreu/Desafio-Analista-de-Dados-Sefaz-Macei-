import duckdb
from src.config import ARQUIVO_PARQUET, BANCO_DUCKDB

def carregar_dados_duckdb():
    print("\nInicializando o banco de dados DuckDB...")
    
    # Garante que a pasta data/gold exista
    BANCO_DUCKDB.parent.mkdir(parents=True, exist_ok=True)
    
    # Conecta ao arquivo do banco (se não existir, ele cria automaticamente)
    conexao = duckdb.connect(str(BANCO_DUCKDB))
    
    try:
        print("Criando tabela otimizada a partir do arquivo Parquet...")
        
        # Cria uma Tabela direto do Parquet no banco de dados
        conexao.execute(f"""
            CREATE OR REPLACE TABLE despesas_funcao AS 
            SELECT * FROM read_parquet('{ARQUIVO_PARQUET.as_posix()}');
        """)
        
        # Validando a carga contando as linhas
        total_linhas = conexao.execute("SELECT COUNT(*) FROM despesas_funcao;").fetchone()[0]
        print(f"Sucesso! Banco de dados populado com {total_linhas} linhas na tabela 'despesas_funcao'.")
        return f"Banco DuckDB atualizado com sucesso ({total_linhas} linhas)."
        
    except Exception as e:
        print(f"Erro ao carregar dados no DuckDB: {e}")
        raise e
    finally:
        # É crucial fechar a conexão para salvar o arquivo no disco rigidamente
        conexao.close()

if __name__ == "__main__":
    carregar_dados_duckdb()