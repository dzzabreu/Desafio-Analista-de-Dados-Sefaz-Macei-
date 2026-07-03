from pathlib import Path

# 1. Encontra a raiz do projeto (sobe dois níveis a partir deste arquivo config.py)
RAIZ_PROJETO = Path(__file__).resolve().parent.parent

# 2. Define os caminhos das pastas de dados mapeadas na estrutura Medalhão
PASTA_RAW = RAIZ_PROJETO / "data" / "raw"
PASTA_PROCESSED = RAIZ_PROJETO / "data" / "processed"

# 3. Define caminhos específicos para facilitar o uso nos scripts
PASTA_COMPACTOS = PASTA_RAW / "dados_compactos"
PASTA_EXTRAIDOS = PASTA_RAW / "dados_extraidos"
ARQUIVO_PARQUET = PASTA_PROCESSED / "finbra_consolidado.parquet"