import pygame 

# inicializar o pygame

pygame.init()

tamanho_tela = (600, 600)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Jogo Pegar Bolas")


tamanho_bola = 15

bola = pygame.Rect(100, 500, tamanho_bola, tamanho_bola)
tamanho_jogador = 100
jogador = pygame.Rect(0, 750, tamanho_jogador, 15)

qtd_blocos_linha = 8
qtd_linhas_blocos = 5
qtd_total_blocos = qtd_blocos_linha * qtd_linhas_blocos

def criar_blocos(qtd_blocos_linha, qtd_linhas_blocos):
    altura_tela = tamanho_tela[1]
    largura_tela = tamanho_tela[0]
    distancia_entre_blocos = 5
    largura_bloco = largura_tela / 8 - distancia_entre_blocos
    altura_bloco = 15
    distancia_entre_linhas = altura_bloco + 10

    blocos = []

    for j in range(qtd_linhas_blocos):
        for i in range(qtd_blocos_linha):
            bloco = pygame.Rect(i * (largura_bloco + distancia_entre_blocos), j * distancia_entre_linhas, largura_bloco,altura_bloco)
            blocos.append(bloco)
            return blocos

cores = {
         "branca": (255, 255, 255), 
         "preta": (0, 0, 0), 
         "amarela": (255, 255, 0),
         "azul": (0, 0, 255),
         "verde": (0, 255, 0)
         }

fim_jogo = False
pontuacao = 0
movimento_bola = [1, 1]

def desenhar_inicio_jogo():
    tela.fill(cores["preta"])
    pygame.draw.rect(tela,cores["azul"], jogador)
    pygame.draw.rect(tela,cores["branca"], bola)


def desenhar_blocos(blocos):
    for bloco in blocos:
        pygame.draw.rect(tela, cores["verde"], bloco)


def movimentar_jogador(evento):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RIGHT:
            jogador.x = jogador.x + 5
        if evento.key == pygame.K_LEFT:
            jogador.x = jogador.x - 5

def movimentar_bola():
    pass


desenhar_inicio_jogo()   
blocos = criar_blocos(qtd_blocos_linha, qtd_linhas_blocos)
desenhar_blocos(blocos)


while not fim_jogo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True

    pygame.time.wait(1)
    pygame.display.flip()

pygame.quit()









