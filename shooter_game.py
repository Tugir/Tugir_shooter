#Создай собственный Шутер!

from pygame import *
from random import *

class GameSprite(sprite.Sprite):
		def __init__(self, player_image, player_x, player_y, size_x, size_y, speed):
				sprite.Sprite.__init__(self)
				self.image = transform.scale(image.load(player_image), (size_x, size_y))
				self.rect = self.image.get_rect() #хитбокс
				self.rect.x = player_x
				self.rect.y = player_y
				self.speed = speed
				self.lifes = 3
				self.kills = 0
				self.timer = 0
				self.interval = 5

		def reset(self):
				window.blit(self.image, (self.rect.x, self.rect.y))

		def hero_update(self):
				keys = key.get_pressed()
				if keys[K_LEFT]:
					self.rect.x -= 10
				if keys[K_RIGHT]:
					self.rect.x += 10
				if keys[K_SPACE]:
					if self.timer == self.interval:
					  bullet = Bullet('bullet.png', self.rect.x + 20, self.rect.y, 20, 40, 10)
					  fire_bullet.play()
					  bullets.add(bullet)
					  self.timer = 0
					else:
					  self.timer += 1

		def enemy_update(self):
				self.speed = randint(5, 15)
				self.rect.y += self.speed
				if self.rect.y > 500:
					self.rect.x = randint(0, 640)
					self.rect.y = -60

class Bullet(GameSprite):
	def bullet_update(self):
		self.rect.y -= 10
		if self.rect.y < -60:
			self.kill()

window = display.set_mode((700, 500))
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
display.set_caption('стрелялка')

hero = GameSprite('rocket.png', 100, 420, 60, 60, 10)
enemy = GameSprite('ufo.png', randint(0, 640), -60, 60, 60, randint(5, 15))
enemies = sprite.Group()
enemy1 = GameSprite('ufo.png', randint(0, 640), -60, 60, 60, randint(5, 15))
enemy2 = GameSprite('ufo.png', randint(0, 640), -60, 60, 60, randint(5, 15))
enemy3 = GameSprite('ufo.png', randint(0, 640), -60, 60, 60, randint(5, 15))
enemy4 = GameSprite('ufo.png', randint(0, 640), -60, 60, 60, randint(5, 15))
enemy5 = GameSprite('ufo.png', randint(0, 640), -60, 60, 60, randint(5, 15))
enemies.add(enemy1)
enemies.add(enemy2)
enemies.add(enemy3)
enemies.add(enemy4)
enemies.add(enemy5)
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play(-1)
mixer.music.set_volume(0.1)
fire_bullet = mixer.Sound('shoot.ogg')
fire_bullet.set_volume(0.1)
crash = mixer.Sound('crash.ogg')
crash.set_volume(0.1)
damage = mixer.Sound('damage.ogg')
damage.set_volume(0.1)
bullets = sprite.Group()

font.init()
font1 = font.SysFont('Arial', 40)

game = True
while game:
	window.blit(background, (0, 0))
	text_life = font1.render('Жизни:' + str(hero.lifes), True, (255, 255, 255))
	window.blit(text_life, (10, 10))
	text_kills = font1.render('Павшие корабли:' + str(hero.kills), True, (255, 255, 255))
	window.blit(text_kills, (250, 10))
	for ev in event.get(): 
		if ev.type == QUIT:
			game = False
	
	if sprite.spritecollide(hero, enemies, True):
		damage.play()
		hero.lifes -= 1
		print('Осталось', hero.lifes, 'жизней!')
		enemy1 = GameSprite('ufo.png', randint(0, 640), -60, 60, 60, randint(5, 15))
		enemies.add(enemy1)
		hero.kills += 1

	
	


	if sprite.groupcollide(enemies, bullets, True, True):
		crash.play()
		enemy1 = GameSprite('ufo.png', randint(0, 640), -60, 60, 60, randint(5, 15))
		enemies.add(enemy1)
		hero.kills += 1

	if hero.lifes <= 0:
		break


	for bullet in bullets:
		bullet.bullet_update()
	for enemy in enemies:
		enemy.enemy_update()
	hero.hero_update()
	hero.reset()
	enemies.draw(window)
	bullets.draw(window)
	display.update()
	time.delay(50)
		