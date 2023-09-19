import pygame

from data.board import Board
from utils.boardColor import tileColor

def drawBoard(screen, width, height):
  game = Board(width, height)
  color = "white"

  for column in game.tiles.values():
    for tile in column.values():
      pygame.draw.rect(screen, color, tile)
      color = tileColor(color)
    color = tileColor(color)
      
  pygame.display.update()

def main():
  pygame.init()
  gameWidth, gameHeight = 1280, 720
  screen = pygame.display.set_mode((gameWidth,gameHeight))
  screen.fill("light blue")
  clock = pygame.time.Clock()
  running = True

  drawBoard(screen, gameWidth, gameHeight)

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    # pygame.display.flip()

    clock.tick(60)

  pygame.quit()

if __name__ == "__main__":
  main()