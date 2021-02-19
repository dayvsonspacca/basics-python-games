import pygame
from pygame.locals import *
from classes import Pixel_walkable, Player
from random import randint
def main():
    """
    Função principal do script
    """
    try:
        # Variáveis \/
        map_width = map_height = 40
        # O TAMANHO DO MAPA TEM QUE SER IGUALLLLL
        sizes = (map_width*10, map_height*10)
        key_pressed = 0 # KEY PARA O TECLA UP
        # Variáveis /\
        pygame.init()
        window = pygame.display.set_mode(sizes)
        window.fill((255, 255, 255))
        pygame.display.set_caption('Walkable map')
        map_config = map_configuration(map_width, map_height)
        win_pixel = randint(0, len(map_config)) 
        map_config[win_pixel].win_pixel = True 
        map_config[win_pixel].walkable = True
        map_config[win_pixel].color = (0, 255, 0)
        map_config = create_walls(window, map_config, map_width, map_height)
        create_map(map_config, window)
        player = Player(int(map_width*10/2), int(map_height*10/2))
        pygame.draw.rect(window, (255, 0, 0),(player.pos,player.size))
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == KEYDOWN:
                    key_pressed = event.key
            if key_pressed == 32:
                map_config = player_power(window, map_config, map_width, player)
                create_map(map_config, window)
                pygame.draw.rect(window, (255, 0, 0),(player.pos,player.size))
            move_player(window, map_config, key_pressed, player, map_width, map_height, win_pixel)
            key_pressed = 0
            pygame.display.update()
    except Exception as erro:
        main()   
def create_map(map_config, window):
    """
    Função criadora do mapa com base no parametro map_config.
    map_configuration: Lista com a configuração de cada pixel_walkable
    return: O mapa pronto
    """
    for pixel in map_config:
        pygame.draw.rect(window, pixel.color, (pixel.pos, pixel.size))
def map_configuration(map_width, map_height):
    """
    Função que cria a configuração de cada pixel_walkable do mapa.
    map_width e map_height: Usado para calcular quantos pixel_walkables vão ter no mapa.
    retorn: Retorna essa configuração.
    """
    number_of_pixels = map_height * map_width
    map_config = []
    pos_x = pos_y = 0
    for pixel in range(number_of_pixels):
        if randint(0, 3) == 0:
            new_pixel = Pixel_walkable(pos_x, pos_y, walkable=False)
        else:
            new_pixel = Pixel_walkable(pos_x, pos_y)
        pos_x += 10
        if pos_x == map_width*10:
            pos_x = 0
            pos_y += 10
            if pos_y == map_height*10 and map_width == pos_x:
                break
        map_config.append(new_pixel)
    return map_config

def move_player(window, map_config, key_pressed, player, map_width, map_height, win_pixel):
    """
    Função que move o jogador pelo cenário utilizando com base o map_config.
    map_config: Lista da configuração do mapa
    key_pressed: Key pressionada pelo usuario no teclado
    """
    if map_config[win_pixel].pos == player.pos:
        pygame.quit()
        main()
    player_index = 0
    for pixel in map_config:
        if pixel.pos[0] == player.pos[0] and pixel.pos[1] == player.pos[1]:
            break
        player_index += 1
    moviments_keys = (273, 274, 275, 276, 32, 27)
    if key_pressed in moviments_keys:
        if key_pressed == moviments_keys[0] and map_config[player_index-map_height].walkable:
            pygame.draw.rect(window, (255, 255, 255),(player.pos, player.size))
            player.pos[1] -= 10
            pygame.draw.rect(window, (player.color),(player.pos, player.size))
        elif key_pressed == moviments_keys[1] and map_config[player_index+map_height].walkable:
            pygame.draw.rect(window, (255, 255, 255),(player.pos, player.size))
            player.pos[1] += 10
            pygame.draw.rect(window, (player.color),(player.pos, player.size))
        elif key_pressed == moviments_keys[2] and map_config[player_index+1].walkable:
            pygame.draw.rect(window, (255, 255, 255),(player.pos, player.size))
            player.pos[0] += 10
            pygame.draw.rect(window, (player.color),(player.pos, player.size))
        elif key_pressed == moviments_keys[3] and map_config[player_index-1].walkable:
            pygame.draw.rect(window, (255, 255, 255),(player.pos, player.size))
            player.pos[0] -= 10
            pygame.draw.rect(window, (player.color),(player.pos, player.size))
        elif key_pressed == 27:
            pygame.quit()
            exit()

def create_walls(window, map_config, map_width, map_height):
    """
    Função geradora das paredes do mapa
    return: Retorna o map_config com os pixels da parede com walkable = False
    """
    walls = map_width
    column = 0
    for i in range(walls):
        map_config[i].walkable = False
        map_config[len(map_config)-1-i].walkable = False
        map_config[i].color = (0, 0, 0)
        map_config[len(map_config)-1-i].color = (0, 0, 0)
        map_config[column].walkable = False
        map_config[column].color = (0, 0, 0)
        map_config[map_width-1 + column].walkable = False
        map_config[map_width-1 + column].color = (0, 0, 0)
        column += map_width
    return map_config

def player_power(window, map_config, map_width, player):
    """
    Função que utiliza o poder do player quer transformar os blocos ao seus lados e acima/abaixo em walkable = True
    """
    player_index = 0
    for pixel in map_config:
        if pixel.pos[0] == player.pos[0] and pixel.pos[1] == player.pos[1]:
            break
        player_index += 1
    map_config[player_index + 1].walkable = True
    map_config[player_index + 1].color = (255, 255, 255)
    map_config[player_index - 1].walkable = True
    map_config[player_index - 1].color = (255, 255, 255)
    map_config[player_index + map_width].walkable = True
    map_config[player_index + map_width].color = (255, 255, 255)
    map_config[player_index - map_width].walkable = True
    map_config[player_index - map_width].color = (255, 255, 255)
    return map_config
main()  
