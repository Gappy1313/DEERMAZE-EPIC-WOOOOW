from pygame import *


red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
black = 0, 0, 0
white = 255, 255, 255
gray = 125, 125, 125

window = display.set_mode((700, 500))
display.set_caption('The Deer Maze')
background = transform.scale(image.load("darkWoodBG.png"), (700, 500))

clock = time.Clock()
FPS = 60

game = True
finish = False

font.init()
font = font.Font(None, 70)
win = font.render("YOU DEER!", True, (255, 215, 0))
lose = font.render("YOU LOSE!", True, (180, 0, 0))



playerImage = transform.scale(image.load("roomDeerP.png"), (70, 70))
enemyImage = transform.scale(image.load("deerSatanE.png"), (70, 70))
icon = transform.scale(image.load("icon.png"), (100, 100))
enemyImage2 = transform.scale(image.load("deerFutureE.png"), (70, 70))
deerAward = transform.scale(image.load("deerAward.png"), (70, 70))

display.set_icon(icon)

mixer.init()
mixer.music.load("DarkMusic.ogg")
mixer.music.set_volume(4)
mixer.music.play(-1)

money = mixer.Sound("money.ogg")
death = mixer.Sound("kick.ogg")

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.rect = self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def render(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(sprite.Sprite):
    def __init__(self, image, pos: tuple):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
    
    def render(self):
        window.blit(self.image, self.rect)

    def move(self):
        presskey = key.get_pressed()

        if presskey[K_w] and self.rect.y >= 5:
            self.rect.y -= 5
        if presskey[K_s] and self.rect.y <= 500-self.rect.width:
            self.rect.y += 5
        if presskey[K_a] and self.rect.x >= 5:
            self.rect.x -= 5
        if presskey[K_d] and self.rect.x <= 700-self.rect.width: 
            self.rect.x += 5
class Enemy(sprite.Sprite):
    def __init__(self, image, pos: tuple):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.direction = 1
    
    def render(self):
        window.blit(self.image, self.rect)

    def move(self):
        self.rect.x += self.direction * 12
        if self.rect.x <= 0 or self.rect.x >= 700 - self.rect.width:
            self.direction *= -1

    def moveP2(self):
        presskey = key.get_pressed()

        if presskey[K_UP]:
            self.rect.y -= 5
        if presskey[K_DOWN]:
            self.rect.y += 5
        if presskey[K_LEFT]:
            self.rect.x -= 5
        if presskey[K_RIGHT]:
            self.rect.x += 5
class Enemy2(sprite.Sprite):
    def __init__(self, image, pos: tuple):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.direction = 1
    
    def render(self):
        window.blit(self.image, self.rect)

    def move(self):
        self.rect.x += self.direction * 5
        if self.rect.x <= 0 or self.rect.x >= 700 - self.rect.width:
            self.direction *= -1

    def moveP3(self):
        presskey = key.get_pressed()

        if presskey[K_i]:
            self.rect.y -= 5
        if presskey[K_k]:
            self.rect.y += 5
        if presskey[K_j]:
            self.rect.x -= 5
        if presskey[K_l]:
            self.rect.x += 5
class Award(sprite.Sprite):
    def __init__(self, image, pos: tuple):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
    
    def render(self):
        window.blit(self.image, self.rect)

player = Player(playerImage, (50, 150))
enemy = Enemy(enemyImage, (250, 250))
enemy2 = Enemy2(enemyImage2, (450, 450))
enemy3 = Enemy2(enemyImage2, (50, 50))
award = Award(deerAward, (655, 450))
wall = Wall(125, 125 , 125, 100, 0, 10, 400)
wall2 = Wall(125, 125 , 125, 200, 100, 10, 400)
wall3 = Wall(125, 125 , 125, 300, 0, 10, 400)
wall4 = Wall(125, 125 , 125, 400, 100, 10, 400)
wall5 = Wall(125, 125 , 125, 500, 0, 10, 400)
wall6 = Wall(125, 125 , 125, 600, 100, 10, 400)
while game:
    presskey = key.get_pressed()
    if presskey[K_g]:
        background = transform.scale(image.load("secretWood.png"), (700, 500))
    
    window.blit(background,(0, 0))

    if finish != True:
        wall.render()
        wall2.render()
        wall3.render()
        wall4.render()
        wall5.render()
        wall6.render()

        award.render()

        player.render()
        player.move()

        enemy.render()
        enemy.move()

        enemy2.render()
        enemy2.move()

        enemy3.render()
        enemy3.move()
        

    if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, enemy2) or sprite.collide_rect(player, enemy3) or sprite.collide_rect(player, wall) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6):
        finish = True
        background = transform.scale(image.load("FAKE BLUE SCREEN.webp"), (700, 500))
        window.blit(lose, (200, 200))
        death.play()

    if sprite.collide_rect(player, award):
        finish = True
        window.blit(win, (200, 200))
        money.play()
    

    

    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()