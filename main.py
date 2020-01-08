import sys,pygame,time,random,math

pygame.init()

size = width, height = 900, 600
speed = [0.3, 0]
black = 0, 0, 0
white = 255, 255, 255
brown = 139,69,19
blue = 0,0,255
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
ball_x = 70
rect_speed = 0.2
iterate_one_time = 0
up = False
counter = 0
radius = 18
gap = 120


def check(x,y):
	font = pygame.font.SysFont("comicsansms", 40)
	text = font.render(".", True, blue)
	screen.blit(text,(x , y))
	
def crash(arg):
	print("arg",arg)
	font = pygame.font.SysFont("comicsansms", 80)
	text = font.render("YOU CRASHED", True, (255, 255, 255))

	time.sleep(2)
	screen.blit(text,(-1000,150))

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				counter = 0
				up = True
	
	if not up:
		# print("if")
		ball_height += 0.38

	else:
		# print("else")
		counter += 1
		ball_height -= 0.46
		if counter > 120 :
			counter = 0
			up = False

	x1 -= rect_speed
	x2 -= rect_speed
	x3 -= rect_speed

	y1 = h1 - 45 
	y2 = h2 - 45 
	y3 = h3 - 45 
	
	ball_right = ball_x + radius - 15 
	ball_left = ball_x - radius 
	ball_top = ball_height - 40 - radius 
	ball_bottom = ball_height -radius -10


	if (ball_right > x1 and ball_left < x1) and  (ball_top < y1 or  ball_bottom > y1 + gap):
		time.sleep(0.5)

	elif (ball_right > x2 and ball_left < x2) and  (ball_top < y2 or  ball_bottom > y2 + gap):
			time.sleep(0.5)

	elif (ball_right > x3 and ball_left < x3) and  (ball_top < y3 or  ball_bottom > y3 + gap):
		time.sleep(0.5)

		
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

	pygame.draw.rect(screen,black ,[x1,0,27,h1])
	pygame.draw.rect(screen,black ,[x1, h1 + gap , 27,500])
	pygame.draw.rect(screen,black ,[x2,0,27,h2])
	pygame.draw.rect(screen,black ,[x2,h2 + gap,27,500])
	pygame.draw.rect(screen,black ,[x3,0,27,h3])
	pygame.draw.rect(screen,black ,[x3,h3 + gap, 27,500])
	
	pygame.draw.circle(screen, brown , (ball_x,int(ball_height)), radius)
	check(x2,y2)


	pygame.display.flip()
	if iterate_one_time == 0:
		time.sleep(0.8)
	iterate_one_time = 1
	# time.sleep(0.2)
