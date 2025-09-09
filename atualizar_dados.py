import requests

def baixar_arquivo(url, nome_arquivo):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(nome_arquivo, 'wb') as f:
            f.write(response.content)
        print(f"Arquivo salvo como {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao baixar {nome_arquivo}: {e}")

# URLs dos arquivos CSV
url_tarifas_aneel = "https://dadosabertos.aneel.gov.br/dataset/tarifas-distribuidoras-energia-eletrica/resource/fcf2906c-7c32-4b9b-a637-054e7a5234f4/download/tarifas-distribuidoras.csv"
url_pld_ccee = "https://www.ccee.org.br/documents/80426/211733/PLD_Medio_Submercado.csv"

# Nomes dos arquivos locais
arquivo_tarifas = "tarifas_aneel.csv"
arquivo_pld = "pld_ccee.csv"

# Baixar os arquivos
baixar_arquivo(url_tarifas_aneel, arquivo_tarifas)
baixar_arquivo(url_pld_ccee, arquivo_pld)
