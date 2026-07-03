import pandas as pd
from pathlib import Path
from src.config import PASTA_EXTRAIDOS, ARQUIVO_PARQUET

def consolida_parquet():
    print("\nConvertendo e salvando a base consolidada em formato Parquet...")
    
    ARQUIVO_PARQUET.parent.mkdir(parents=True, exist_ok=True)
    
    df_final = consolidar_dados()
    
    df_final.to_parquet(
        ARQUIVO_PARQUET, 
        engine='pyarrow', 
        compression='snappy',
        index=False 
    )
    
    print(f"\nSucesso! Base performática gerada em: {ARQUIVO_PARQUET}")

def distingue_conta(data_frame):
    data_frame["Função"] = None
    data_frame["Subfunção"] = None

    ultima_funcao_encontrada = None

    for index, linha in data_frame.iterrows():
        texto_conta = str(linha["Conta"])
        
        if texto_conta[2] == " ":
            ultima_funcao_encontrada = texto_conta
            data_frame.at[index, "Função"] = texto_conta
            
        elif texto_conta[2] == "." or texto_conta.startswith("FU"):
            data_frame.at[index, "Função"] = ultima_funcao_encontrada
            data_frame.at[index, "Subfunção"] = texto_conta

def consolidar_dados():
    pd.set_option('display.float_format', lambda x: '%.2f' % x)
    
    pasta_origem = PASTA_EXTRAIDOS
    arquivos_csv = list(pasta_origem.glob("*.csv"))
    
    if not arquivos_csv:
        print("Nenhum arquivo CSV encontrado em 'dados_extraidos'. Rode o 'extract_data.py' primeiro.")
        return

    lista_dataframes = []
    print(f"Encontrados {len(arquivos_csv)} arquivos para consolidação. Lendo dados...")

    for caminho_csv in arquivos_csv:
        ano = caminho_csv.stem.split("_")[1]
        
        print(f"Lendo e tratando o ano {ano}...")
        
        df_ano = pd.read_csv(
            caminho_csv,
            sep=";",           
            encoding="latin-1", 
            skiprows=3,        
            decimal=","        
        )
        
        df_ano["Ano"] = int(ano)
        
        distingue_conta(df_ano)
        
        lista_dataframes.append(df_ano)

    print("Juntando todos os anos em um único DataFrame...")
    df_consolidado = pd.concat(lista_dataframes, ignore_index=True)
    
    print(f"Sucesso! Dados consolidados com total de {df_consolidado.shape[0]} linhas.")
    print(f"Colunas identificadas: {list(df_consolidado.columns)}")
    
    return df_consolidado


if __name__ == "__main__":
    consolida_parquet()