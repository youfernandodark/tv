import json

# Nome dos arquivos
arquivo_json = 'FILMES .json'
arquivo_m3u = 'filmes_enriquecido.m3u'

def converter_json_para_m3u():
    try:
        # 1. Carregar os dados do JSON original
        with open(arquivo_json, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        # 2. Criar/Abrir o arquivo M3U para escrita
        with open(arquivo_m3u, 'w', encoding='utf-8') as m3u:
            m3u.write("#EXTM3U\n\n")
            m3u.write("# -- Lista VOD Enriquecida via Python --\n\n")
            
            for filme in dados['movies']:
                # Extraindo informações detalhadas
                titulo = filme['title']
                id_filme = filme['id']
                logo = filme['poster_url']
                genero = ", ".join(filme['genre'])
                ano = filme['year']
                url_video = filme['stream_url']
                diretor = filme['director']
                # Preparando o elenco para o player (formatado com vírgulas)
                elenco = ", ".join(filme['cast'])

                # 3. Escrever a linha de metadados enriquecida
                # NOTA: Estas tags extras (tvg-director, tvg-actors) 
                # são suportadas por players mais modernos e podem ajudar
                # a preencher o "N/A" na sua tela.
                
                linha_inf = (
                    f'#EXTINF:-1 tvg-id="{id_filme}" '
                    f'tvg-name="{titulo}" '
                    f'tvg-logo="{logo}" '
                    f'group-title="{genero}" '
                    f'tvg-language="en" ' # Linguagem original (do JSON)
                    f'tvg-country="US" '   # País (pode adicionar ao JSON depois)
                    f'tvg-director="{diretor}" '
                    f'tvg-actors="{elenco}" '
                    f'tvg-year="{ano}",{titulo} ({ano})\n'
                )
                
                m3u.write(linha_inf)
                # Opcional: Alguns players usam tags especiais para descrição:
                # m3u.write(f"#EXTMY-DESC:{filme['synopsis']}\n") 
                # (Mas o suporte para descrição direta no M3U é raro)
                
                m3u.write(f"{url_video}\n\n")
        
        print(f"Sucesso! Arquivo M3U enriquecido '{arquivo_m3u}' gerado.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_json}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    converter_json_para_m3u()
