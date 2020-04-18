# Copyright (C) 2020	Gagik Safaryan <safaryangagik0@gmail.com>, Vladimir Simonyan <simonyan.vlad@gmail.com>

import pygame
import sys
import random
from time import sleep

def NewGame():
	pygame.init()
	screen = pygame.display.set_mode((800,600))

	# === [TEXTURES*] ===
	bgcolor = (107, 198, 206)
	gamespeed = 12

	bg = pygame.image.load('img/bg.png')
	bgX = 0

	floor = pygame.image.load('img/floor.png')
	floorX = 0

	bird = pygame.image.load('img/bird1.png')
	birdX = 150
	birdY = 260
	bird_anim_1 = 0
	bird_anim_2 = 0
	bird_size = 65

	tube_length = 85
	tube_1 = pygame.image.load('img/tube.png')
	tube_1 = pygame.transform.scale(tube_1, (tube_length, 1500))
	tube_1X = 800
	tube_1Y = -650 + random.randint(0, 5)*50

	tube_2 = pygame.image.load('img/tube.png')
	tube_2 = pygame.transform.scale(tube_2, (tube_length, 1500))
	tube_2X = 1250
	tube_2Y = -650 + random.randint(0, 5)*45

	# === [VARIABLES] ===
	score = 0
	run_game = True
	gameover = 0

	while run_game:
		# === [FLY ANIM] ===
		bird_anim_1 += 1
		bird_anim_2 += 1

		if bird_anim_1 == 4:
			if bird_anim_2 < 3:
				bird = pygame.image.load('img/bird2.png')
			else:
				bird = pygame.image.load('img/bird4.png')
		
		elif bird_anim_1 == 8:
			if bird_anim_2 < 3:
				bird = pygame.image.load('img/bird1.png')
			else:
				bird = pygame.image.load('img/bird3.png')
			bird_anim_1 = 0

		bird = pygame.transform.scale(bird, (bird_size, bird_size))


		# === [SHOW OBJECTS] ===
		screen.fill(bgcolor)
		screen.blit(bg,(bgX, 0))
		screen.blit(tube_1, (tube_1X, tube_1Y))
		screen.blit(tube_2, (tube_2X, tube_2Y))
		screen.blit(floor,(floorX, 0))
		screen.blit(bird, (birdX, birdY))

		# === [EVENT HANDLING] ===
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if gameover == 0 and event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and birdY >= birdY - gamespeed * 7:
					birdY -= gamespeed * 7
					bird_anim_2 = 0
					bird = pygame.image.load('img/bird2.png')

		# === [BACKGROUND STEP] ===
		if bgX < -766:
			bgX = 0 - gamespeed // 3
		else:
			bgX -= gamespeed // 3

		# === [FLOOR STEP] ===
		if floorX < -766:
			floorX = 0 -  gamespeed // 3
		else:
			floorX -= gamespeed

		# === [TUBE STEP] ===
		if tube_1X + tube_length < 0:
			tube_1X = tube_2X + 450
			tube_1Y = -650 + random.randint(0, 5) * 50
			score += 1
		else:
			tube_1X -= gamespeed

		if tube_2X +tube_length < 0:
			tube_2X = tube_1X + 450
			tube_2Y = -650 + random.randint(0, 5) * 50
			score += 1
		else:
			tube_2X -= gamespeed

		# === [BIRD STEP] ===
		# checked whether the bird can go down
		if birdY + 55 <= 525:
			birdY += gamespeed
			# checked whether the bird touched the floor
			if gameover == 1:
				birdY += gamespeed * 3
		else:
			# printing a score and ending the game
			print("Score: " + str(score))
			GameOver()

		# check if the bird touched the tubes
		# tube1
		if (tube_1X < birdX + bird_size and tube_1X + tube_length > birdX) and (birdY < tube_1Y + 720 or birdY > tube_1Y + 720 + 107):
			gameover = 1
		# tube2
		elif (tube_2X < birdX + bird_size and tube_2X + tube_length > birdX) and (birdY < tube_2Y + 720 or birdY > tube_2Y + 720 + 107):
			gameover = 1

		pygame.display.update()
		# delay
		sleep(0.05)


def GameOver():
	sleep(1.5)
	NewGame()

# === [ MAIN ] ====
NewGame()
