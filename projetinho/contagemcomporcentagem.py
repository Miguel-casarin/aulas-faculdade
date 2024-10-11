from youtube_comment_downloader import YoutubeCommentDownloader

class ContadorComentariosYouTube:
    def __init__(self, video_url, palavra):
        self.video_url = video_url
        self.palavra = palavra.lower()  # Palavra para contagem, convertida para minúsculas
        self.downloader = YoutubeCommentDownloader()
    
    def contar_ocorrencias(self):
        contador_palavra = 0
        contador_total = 0
        
        # Iterar sobre os comentários e contar as ocorrências da palavra e o número total de comentários
        for comment in self.downloader.get_comments_from_url(self.video_url):
            texto_comentario = comment['text'].lower()  # Converter o comentário para minúsculas
            contador_palavra += texto_comentario.count(self.palavra)  # Contabilizar ocorrências da palavra
            contador_total += 1  # Incrementa o contador total de comentários

        return contador_palavra, contador_total


class Porcentagem:
    def __init__(self):
        pass

    @staticmethod
    def calculo_porcentagem(montante, parte):
        if montante == 0:  # Prevenção de divisão por zero
            return 0
        porcentagem = (parte * 100) / montante
        return porcentagem


# URL do vídeo e palavra para busca
video_url = 'https://www.youtube.com/watch?v=OkboNGQ9LU0&ab_channel=FabioAkita'
palavra = 'top'

# Contar comentários e ocorrências da palavra
contador_comentarios = ContadorComentariosYouTube(video_url, palavra)
contador_palavra, contador_total = contador_comentarios.contar_ocorrencias()

# Calcular a porcentagem
porcentagem = Porcentagem().calculo_porcentagem(contador_total, contador_palavra)

# Exibir a porcentagem
print(f"A palavra '{palavra}' apareceu em {porcentagem:.2f}% dos comentários.")
