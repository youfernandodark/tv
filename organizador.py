import os

# Configuração: Nome dos arquivos que você já tem no GitHub
arquivos_origem = ['https://raw.githubusercontent.com/youfernandodark/tv/refs/heads/main/tv_canais.m3u', 'https://raw.githubusercontent.com/youfernandodark/tv/refs/heads/main/FILMES%20.m3u', 'series.m3u']
arquivo_saida = 'lista_final.m3u'

def unir_listas():
    with open(arquivo_saida, 'w', encoding='utf-8') as f_saida:
        # Escreve o cabeçalho obrigatório apenas uma vez no topo
        f_saida.write("#EXTM3U\n\n")
        
        for nome_arquivo in arquivos_origem:
            if os.path.exists(nome_arquivo):
                with open(nome_arquivo, 'r', encoding='utf-8') as f_entrada:
                    linhas = f_entrada.readlines()
                    for linha in linhas:
                        # Pula o cabeçalho #EXTM3U dos arquivos individuais para não repetir
                        if not linha.strip().startswith("#EXTM3U") and linha.strip():
                            f_saida.write(linha)
                f_saida.write("\n") # Adiciona uma linha em branco entre as categorias
                print(f"✔ {nome_arquivo} adicionado com sucesso.")
            else:
                print(f"⚠ Aviso: {nome_arquivo} não encontrado. Pulando...")

if __name__ == "__main__":
    unir_listas()
    print(f"\n🚀 Pronto! Sua '{arquivo_saida}' foi gerada.")
