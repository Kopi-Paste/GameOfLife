#!/usr/bin/python3

from typing import List
import pygame

CELL_SIZE = 10


def get_cell(gamefield : List[bool], x : int, y : int, width : int) -> bool:
    return gamefield[x + y * width]


def display_gamefield(gamefield : List[bool], screen : pygame.Surface, width : int, height : int):
    screen.fill((0, 0, 0))

    for y in range(height):
        for x in range(width):
            color = (255, 255, 255) if get_cell(gamefield, x, y, width) else (0, 0, 0)
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.update()


def get_neighbours(gamefield : List[bool], x : int, y : int, width : int, height : int) -> List[bool]:
    returned_list : List[bool] = []
    returned_list.append(get_cell(gamefield, (x - 1 + width) % width, (y - 1 + height) % height, width))
    returned_list.append(get_cell(gamefield, (x - 1 + width) % width, y, width))
    returned_list.append(get_cell(gamefield, (x - 1 + width) % width, (y + 1) % height, width))
    returned_list.append(get_cell(gamefield, x, (y - 1 + height) % height, width))
    returned_list.append(get_cell(gamefield, x, (y + 1) % height, width))
    returned_list.append(get_cell(gamefield, (x + 1) % width, (y - 1 + height) % height, width))
    returned_list.append(get_cell(gamefield, (x + 1) % width, y, width))
    returned_list.append(get_cell(gamefield, (x + 1) % width, (y + 1) % height, width))
    return returned_list

def count_alive_neighbours(gamefield : List[bool], x : int, y : int, width : int, height : int) -> int:
    return len(list(filter(lambda x: x, get_neighbours(gamefield, x, y, width, height))))
    
def should_live(gamefield : List[bool], x : int, y : int, width : int, height : int):
    alive_neighbours = count_alive_neighbours(gamefield, x, y, width, height)
    if alive_neighbours < 2:
        return False
    if alive_neighbours == 3:
        return True
    if alive_neighbours == 2:
        return get_cell(gamefield, x, y, width)
    return False
    
def is_initially_alive(x : int) -> bool:
    return (x // 5) % 2 == 1 and (x // 7) % 2 == 1

def main():
    pygame.init()
    width : int
    height : int
    width, height = map(int, input("Enter game size: 'width height'").split())
    screen = pygame.display.set_mode((width * CELL_SIZE, height * CELL_SIZE))
    total_size = width * height
    gamefield = list(map(is_initially_alive, range(total_size)))
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_gamefield(gamefield, screen, width, height)
        gamefield = list(map(lambda index : should_live(gamefield, index % width, index // width, width, height), range(len(gamefield))))
        clock.tick(10)
        
    pygame.quit()

if __name__ == '__main__':
    main()
