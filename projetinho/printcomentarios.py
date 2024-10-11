from youtube_comment_downloader import YoutubeCommentDownloader

# Instanciar o downloader
downloader = YoutubeCommentDownloader()

# URL do vídeo do YouTube ou ID do vídeo
video_url = 'https://www.youtube.com/watch?v=OkboNGQ9LU0&ab_channel=FabioAkita'

# Iterar sobre os comentários
for comment in downloader.get_comments_from_url(video_url):
    print(comment['text'])  # Imprime o texto de cada comentário
