import sys,pygame,time,random,math

pygame.init()

size = width, height = 900, 600
speed = [0.3, 0]
black = 0, 0, 0
white = 255, 255, 255
brown = 139,69,19

screen = pygame.display.set_mode(size)

# ball = pygame.image.load("ball.png")
ball = pygame.image.load("rsz_3ball.jpg") 
ballrect = ball.get_rect()


x1 = 250
x2 = 550
x3 = 850
h1 = 200
h2 = 400
h3 = 200

ball_height = 300
rect_speed = 0.2
iterate_one_time = 0
up = False
counter = 0


def crash():
	font = pygame.font.SysFont("comicsansms", 80)
	text = font.render("YOU CRASHED", True, (255, 255, 255))
	gameDisplay.blit(text,(100,150))
	pygame.display.update()
	time.sleep(2)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				ball_height -= 40
				print("up",up)
				up = True
		# if event.type == pygame.KEYUP:
		# 	if event.key == pygame.K_UP:
		# 		ball_height += 1
		# if event.type == pygame.KEYUP:
		# 	if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
		# 		x_change = 0
	# print("up",up)
	if not up:
		# print("if")
		ball_height += 0.1
	else:

		counter += 1
		if counter > 5000:
			up = False

	x1 -= rect_speed
	x2 -= rect_speed
	x3 -= rect_speed


	if x1 < 0:
		h1 = random.randint(200, 400)
		x1 = width
	elif x2 < 0:
		h2 = random.randint(200, 400)
		x2 = width
	elif x3 < 0:
		h3 = random.randint(200, 400)
		x3 = width


	
	
	screen.fill(white)
	# screen.blit(ball, ballrect)

	pygame.draw.rect(screen,black ,[x1,0,27,h1])
	pygame.draw.rect(screen,black ,[x1, h1 + 80 , 27,500])
	pygame.draw.rect(screen,black ,[x2,0,27,h2])
	pygame.draw.rect(screen,black ,[x2,h2 + 80,27,500])
	pygame.draw.rect(screen,black ,[x3,0,27,h3])
	pygame.draw.rect(screen,black ,[x3,h3 + 80, 27,500])
	
	pygame.draw.circle(screen, brown , (70,int(ball_height)), 18)


	pygame.display.flip()
	# if iterate_one_time == 0:
	# 	time.sleep(0.8)
	iterate_one_time = 1
	# time.sleep(0.2)
