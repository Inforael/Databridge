import pygame 

# inicializar o pygame

pygame.init()

tamanho_tela = (800, 800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Jogo Pegar Bolas")

tamanho_bola = 15
bola = pygame.rect(100, 500, tamanho_bola, tamanho_bola)
tamanho_jogador = 100
jogador = pygame.rect(0, 750, tamanho_jogador, 15)

qtd_blocos_linha = 8
qtd_linhas_blocos = 5
qtd_total_blocos = qtd_blocos_linha * qtd_linhas_blocos

def criar_blocos():
    blocos = []

    return blocos

cores = {"branca": (255, 0, 0), 
         1: (0, 255, 0), 
         2: (0, 0, 255),
         3: (0, 0, 255),
         4: (0, 0, 255)
         }









