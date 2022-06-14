import pygame
import math

class ball:
    def __init__(self,screen,color, posX, posY, radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.dx = 0
        self.dy = 0
        self.draw_ball()

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, (self.posX, self.posY), self.radius)

    def update(self):
        self.dx = 2
        self.dy = 1
    def move_ball(self):
        self.posX += self.dx
        self.posY += self.dy

    def player_collision(self):
        self.dx = -self.dx

    def wall_collision(self):
        self.dy = -self.dy

    def return_to_center(self):
        self.posX = 400
        self.posY = 200
        self.dx = 0
        self.dy = 0



class player:
    def __init__(self, screen,color, posX, posY, width, height):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.dy = 0
        self.state = 'stopped'
        self.draw_player()

    def update(self):
        self.dy = 2

    def move_player(self):
        if self.state == 'up':
            self.posY -= self.dy
        elif self.state == 'down':
            self.posY += self.dy

    def clamp(self):
        if self.posY <= 0:
            self.posY = 0
        elif self.posY + self.height >= 400:
            self.posY = 400 - self.height

    def draw_player(self):
        pygame.draw.rect(self.screen, self.color, (self.posX, self.posY, self.width, self.height))


class CollisionManager:
    def collision01(self, Ball, Player01):
        if Ball.posY >= Player01.posY and Ball.posY <= Player01.posY + Player01.height:
            if Ball.posX - Ball.radius == Player01.posX + Player01.width:
                return True
        return False

    def collision02(self, Ball, Player02):
        if Ball.posY >= Player02.posY and Ball.posY <= Player02.posY + Player02.height:
            if Ball.posX + Ball.radius == Player02.posX:
                return True
        return False
    def collision03(self, Ball):
        if Ball.posY - Ball.radius <= 0:
            return True
        elif Ball.posY + Ball.radius >= 400:
            return True
        return False

class check_win:
    def __init__(self, screen, posx1, posy1, posx2, posy2):
        self.screen = screen
        self.score01 = 0
        self.score02 = 0
        self.posx1 = posx1
        self.posy1 = posy1
        self.posx2 = posx2
        self.posy2 = posy2
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.label1 = self.font.render(str(self.score01), True, (255, 255, 255))
        self.label2 = self.font.render(str(self.score02), True, (255, 255, 255))
        self.show_score()

    def check_win(self, Ball):
        if Ball.posX + Ball.radius>= 800:
            self.score01 += 1
            self.label1 = self.font.render(str(self.score01), True, (255, 255, 255))
            return True
        if Ball.posX - Ball.radius <= 0:
            self.score02 += 1
            self.label2 = self.font.render(str(self.score02), True, (255, 255, 255))
            return True
        return False
    def show_score(self):
        self.screen.blit(self.label1, (self.posx1 - self.label1.get_rect().width // 2, self.posy1))
        self.screen.blit(self.label2, (self.posx2 - self.label2.get_rect().width // 2, self.posy2))
    
    def game_over(self):
        if self.score01 >= 5:
            return True
        elif self.score02 >= 5:
            return True
        
        return False


pygame.init()

width = 800
height = 400
white = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
black = (0, 0, 0)
pygame.display.set_caption("ping pong")
screen.fill(black)
pygame.draw.line(screen, white, (width // 2, 0), (width // 2, height), 10)

Ball = ball(screen, white, width // 2, height // 2, 15)
Player01 = player(screen, white, 15, (height // 2) - 60, 20, 120)
Player02 = player(screen, white, width - 35, (height // 2) - 60, 20, 120)
collision = CollisionManager()
win = check_win(screen, 100, 20, 700, 20)

def paint_back():
    screen.fill(black)
    pygame.draw.line(screen, white, (width // 2, 0), (width // 2, height), 10)

is_true = True
playing = False
fix = False

while is_true:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_true = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and fix == False:
                Ball.update()
                playing = True
                fix = True
            if event.key == pygame.K_q:
                Player01.update()
                Player01.state = 'up'
            if event.key == pygame.K_w:
                Player01.update()
                Player01.state = 'down'

            if event.key == pygame.K_UP:
                Player02.update()
                Player02.state = 'up'
            if event.key == pygame.K_DOWN:
                Player02.update()
                Player02.state = 'down'

            if event.key == pygame.K_r:
                paint_back()
                win.score01 = 0
                win.score02 = 0
                win.label1 = win.font.render(str(win.score01), True, (255, 255, 255))
                win.label2 = win.font.render(str(win.score01), True, (255, 255, 255))
                Ball.return_to_center()
                playing = True
                fix = False

            if event.key == pygame.K_s:
                playing = False
                fix = False

        if event.type == pygame.KEYUP:
            Player01.state = 'stopped'
            Player02.state = 'stopped'

        



    if playing == True:
        paint_back()
        Ball.move_ball()
        Ball.draw_ball()

        Player01.move_player()
        Player01.clamp()
        Player01.draw_player()

        Player02.move_player()
        Player02.clamp()
        Player02.draw_player()

        if collision.collision01(Ball, Player01):
            Ball.player_collision()

        if collision.collision02(Ball, Player02):
            Ball.player_collision()

        if collision.collision03(Ball):
            Ball.wall_collision()

        if win.check_win(Ball):
            fix = False
            Ball.return_to_center()

        if win.game_over():
            paint_back()
        
            
    win.show_score()
    pygame.display.update()
