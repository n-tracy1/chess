import pygame
import math

class Board:
  """Board class storing state of chess board and player's pieces"""
  def __init__(self, windowWidth, windowHeight):
    self.width = windowWidth
    self.height = windowHeight
    self.tiles = {}

    # Build board
    boardLength = min(self.width, self.height)
    xIndex, yIndex= 0, 0
    squareLength = math.floor(boardLength/8)

    while xIndex < boardLength:
      self.tiles[xIndex] = {}
      while yIndex < boardLength:
        self.tiles[xIndex][yIndex] = pygame.Rect(xIndex, yIndex, squareLength, squareLength)
        yIndex += squareLength
      xIndex += squareLength
      yIndex = 0

    # Build player information


    return