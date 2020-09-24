# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
animCount = 0

class snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8*facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def game():
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('cubes game')

    playerStand = pygame.image.load('pygame_idle.png')
    walkRight =[pygame.image.load('pygame_right_1.png'), pygame.image.load('pygame_right_2.png'),
                pygame.image.load('pygame_right_3.png'),pygame.image.load('pygame_right_4.png'),
                pygame.image.load('pygame_right_5.png'),pygame.image.load('pygame_right_6.png')]
    walkLeft =[pygame.image.load('pygame_left_1.png'), pygame.image.load('pygame_left_2.png'),
                pygame.image.load('pygame_left_3.png'),pygame.image.load('pygame_left_4.png'),
                pygame.image.load('pygame_left_5.png'),pygame.image.load('pygame_left_6.png')]

    bg = pygame.image.load('pygame_bg.jpg')

    clock = pygame.time.Clock()
    x = 50
    y = 400
    width = 60
    height = 71
    speed = 15

    left = False
    right = False

    isJump = False
    jumpCount = 10

    def drawWindow():
        global animCount

        win.blit(bg, (0, 0))

        if animCount + 1 >= 30:
            animCount = 0

        if left:
            win.blit(walkLeft[animCount//5], (x, y))
            animCount+=1
        elif right:
            win.blit(walkRight[animCount // 5], (x, y))
            animCount += 1
        else:
            win.blit(playerStand, (x, y))

        for bullet in bullets:
            bullet.draw(win)

        pygame.display.update()

    run = True
    bullets = []
    lastMove = 1

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for bullet in bullets:
            if bullet.x <= 500 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_f]:
            if len(bullets) < 5:
                bullets.append(snaryad(round(x+width/2), round(y+height/2),5, (255, 0, 0), lastMove))

        if keys[pygame.K_LEFT] and x > 5:
            x -= speed
            left = True
            right = False
            lastMove = -1
        elif keys[pygame.K_RIGHT] and x < 500 - width - 5:
            x += speed
            left = False
            right = True
            lastMove = 1
        else:
            left = False
            right = False
            animCount = 0

        if not isJump:
            if keys[pygame.K_SPACE]:
                isJump = True
        else:
            if jumpCount >= -10:
                if jumpCount >= 0:
                    y -= (jumpCount**2)/2
                else:
                    y += (jumpCount ** 2) / 2
                jumpCount -=1
            else:
                isJump = False
                jumpCount = 10

        drawWindow()




    pygame.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
