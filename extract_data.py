import zipfile
from pathlib import Path

def descompactar_dados():
    pasta_origem = Path("dados_compactos")
    pasta_destino = Path("dados_extraidos")

    pasta_destino.mkdir(exist_ok=True)

    arquivos_zip = list(pasta_origem.glob("**/*.zip"))
    
    if not arquivos_zip:
        print("Nenhum arquivo .zip encontrado em 'dados_compactos'.")
        return

    print(f"Encontrados {len(arquivos_zip)} arquivos .zip. Iniciando extração...")

    for caminho_zip in arquivos_zip:
        ano = caminho_zip.parent.name
        
        with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
            for nome_arquivo in zip_ref.namelist():
                if nome_arquivo.endswith('.csv'):
                    conteudo = zip_ref.read(nome_arquivo)
                    
                    nome_final_csv = pasta_destino / f"finbra_{ano}.csv"
                    
                    nome_final_csv.write_bytes(conteudo)
                    print(f"Extraído: {nome_final_csv}")

if __name__ == "__main__":
    descompactar_dados()