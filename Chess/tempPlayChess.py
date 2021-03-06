from chess import *
import os
import pygame
import math
import time


FPS = 30
grid = 60

game = Game(grid)
game.resetGame()

while(game.running):
    # print(currentPlayer)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:   

                if game.turn == 'black':
                    pieces = game.blackPieces
                else:
                    pieces = game.whitePieces

                clickX = event.pos[0]
                clickY = event.pos[1]   

                clickX += grid//2
                clickY += grid//2

                clickY //= grid
                clickX //= grid           

                coordX = clickY - 1
                coordY = clickX - 1

                print(coordX, coordY)

                if coordX < 8 and coordX >= 0 and coordY < 8 and coordY >= 0:
                    p = game.boardState[coordX][coordY]

                    if p != None and ((game.turn == 'white' and p.colour == 'W') or \
                        (game.turn == 'black' and p.colour == 'B')):
                        game.playingPiece = p
                        moving = True
                        mouse_x, mouse_y = event.pos
                        initialPosition = [p.x, p.y]
                        offset_x = p.x - mouse_x
                        offset_y = p.y - mouse_y


        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and moving:            
                moving = False
                prevBoard = game.boardState
                if game.updateCoord(): # switch sides

                    if game.turn == 'white':
                        game.turn = 'black'
                    else:
                        game.turn = 'white'
                else:
                    game.playingPiece.x = initialPosition[0]
                    game.playingPiece.y = initialPosition[1]

        elif event.type == pygame.MOUSEMOTION:
            if moving:
                mouse_x, mouse_y = event.pos
                game.playingPiece.x = mouse_x + offset_x
                game.playingPiece.y = mouse_y + offset_y

    if keys[pygame.K_q]:
        game.running = False

    if keys[pygame.K_r]:
        game.resetGame()

    game.refresh()    

# - end -
