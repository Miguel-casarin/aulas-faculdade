from youtube_comment_downloader import YoutubeCommentDownloader

# Instanciar o downloader
downloader = YoutubeCommentDownloader()

# URL do vídeo do YouTube
video_url = 'https://www.youtube.com/watch?v=OkboNGQ9LU0&ab_channel=FabioAkita'

# Palavra a ser contabilizada
palavra = 'top'
contador = 0

# Iterar sobre os comentários e contar a ocorrência da palavra
for comment in downloader.get_comments_from_url(video_url):
    texto_comentario = comment['text'].lower()  # Converter para minúsculas para contagem case-insensitive
    contador += texto_comentario.count(palavra.lower())  # Contabilizar ocorrências da palavra no comentário

# Agora vamos contar o número total de comentários
contador_total = 0

# Segundo laço: simplesmente contar o número de comentários
for comment in downloader.get_comments_from_url(video_url):
    contador_total += 1  # Incrementa o contador total de comentários

# Exibir o número total de ocorrências da palavra
if contador > 0:
    print(f"A palavra '{palavra}' apareceu {contador} vezes nos comentários.")
else:
    print(f"A palavra '{palavra}' não foi encontrada nos comentários.")

# Exibir o número total de comentários processados
print(f"Total de comentários processados: {contador_total}")
