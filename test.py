import pygame
pygame.init()

tamanho_tela = (800, 800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Teste pygame")

fim_jogo = False
tamanho_jogador = 50
jogador = (85, 85, tamanho_jogador, tamanho_jogador)

cores = {
    "branco":(255, 255, 255),
    "azul": (0, 0, 200)
}

def desenhar():
     tela.fill(cores["branco"])
     pygame.draw.rect(tela, cores["azul"], jogador)

while not fim_jogo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True

    desenhar()
    pygame.display.flip()
    pygame.time.wait(1)

pygame.quit()

