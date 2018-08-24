import pygame
import math
import random
pygame.init()
width, height = 640, 480
keys = [False, False, False, False]
playerpos = [100,100]

##These are the bad guys setting
badtimer = 100
badtimer1=0
badguys = [[640,100]]
healthvalue = 194

#acc takes account of the player's accuracy and second array tracks all the arrows. The accuracy variable is essentially a list of the number of shots fired and the nmber
acc=[0,0]
arrows=[]

screen = pygame.display.set_mode((width,height))
player = pygame.image.load("resources/images/dude.png")
arrow = pygame.image.load("resources/images/bullet.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
badguyimg1=pygame.image.load("resources/images/badguy.png")
badguyimg = badguyimg1

while 1:
	badtimer -= 1
	screen.fill(0)
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_width()+1):
			screen.blit(grass,(x*100,y*100))

	screen.blit(castle,(0,30))
	screen.blit(castle,(0,135))
	screen.blit(castle,(0,240))
	screen.blit(castle,(0,345))
			
	##Game character 
	position = pygame.mouse.get_pos()
	angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
	playerrot = pygame.transform.rotate(player, 360-angle*57.29)
	playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
	screen.blit(playerrot, playerpos1) 
	



	#Drawing the arrow
	for bullet in arrows:
		index=0
		velx=math.cos(bullet[0])*10
		vely=math.sin(bullet[0])*10
		bullet[1] += velx
		bullet[2] += vely
		if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2] > 480:
			arrows.pop(index)
		index += 1
	for projectile in arrows:
		arrow1 = pygame.transform.rotate(arrow,360-projectile[0]*57.29)
		screen.blit(arrow1, (projectile[1], projectile[2]))

	#BadGuyCharacter is being spawned here
	if badtimer == 0:
		badguys.append([640,random.randint(50,430)])
		badtimer = 100-(badtimer1*2)
		if badtimer1 >= 35:
			badtimer1 = 35
		else :
			badtimer1 += 5

	index=0
	for badguy in badguys :
		if badguy[0]<-64:
			badguys.pop(index)
		badguy[0] -= 7
		##Checking wether badguy is destroying the castle
		badrect=pygame.Rect(badguyimg.get_rect())
		badrect.top=badguy[1]
		badrect.left=badguy[0]
		if badrect.left<64:
			healthvalue -= random.randint(5,20)
			badguys.pop(index)

		index1 = 0
		for bullet in arrows:
			bullrect = pygame.Rect(arrow.get_rect())
			bullrect.left = bullet[1]
			bullrect.top = bullet[2]
			if badrect.colliderect(bullrect):
				print "JAMESSS"
				acc[0] += 1
				badguys.pop(index)
				arrows.pop(index1)
			index1 += 1
		index += 1
	for badguy in badguys:
		screen.blit(badguyimg,badguy)








	pygame.display.flip()


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.exit()
			exit(0)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				keys[0] = True
			elif event.key == pygame.K_a :
				keys[1] = True
			elif event.key == pygame.K_s:
				keys[2] = True
			elif event.key == pygame.K_d :
				keys[3] = True
		if event.type == pygame.KEYUP :
			if event.key == pygame.K_w:
				keys[0] = False
			elif event.key == pygame.K_a :
				keys[1] = False
			elif event.key == pygame.K_s:
				keys[2] = False
			elif event.key == pygame.K_d :
				keys[3] = False
		if event.type == pygame.MOUSEBUTTONDOWN :
			position = pygame.mouse.get_pos()
			acc[1] += 1
			arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
		if keys[0]:
			playerpos[1]-=5
		elif keys[2]:
			playerpos[1]+=5
		if keys[1]:
			playerpos[0]-=5
		elif keys[3]:
			playerpos[0]+=5
