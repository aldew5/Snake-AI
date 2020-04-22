import pygame

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

class Snake(object):
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.v = 10
        self.length = length
        self.direction = 'down'

    def grow(self):
        self.length += 1

    def draw(self):
        x, dist = 0, 0
        while x < self.length:
            if self.direction == "left":
                pygame.draw.rect(win, (50,205,50), ((self.x + dist, self.y), (30,30)))
                dist += 40
                
            elif self.direction == 'right':
                pygame.draw.rect(win, (50,205,50), ((self.x - dist, self.y), (30,30)))
                dist -= 40
                
            elif self.direction == 'down':
                pygame.draw.rect(win, (50,205,50), ((self.x, self.y - dist), (30,30)))
                dist -= 40
                
            elif self.direction == 'up':
                pygame.draw.rect(win, (50,205,50), ((self.x, self.y + dist), (30,30)))
                dist += 40


            x += 1
            

snake = Snake(40, 50, 2)
snake.direction = 'left'

def drawWindow(win):
    win.fill((0,0,0))
    snake.draw()
    
    pygame.display.update()

run = True

while run:
    clock.tick(27)

    keys = pygame.key.get_pressed()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    # move left
    if keys[pygame.K_LEFT] and snake.direction != 'left' and snake.direction != "right":
        if snake.x >= 10:
            snake.x -= snake.v
            snake.direction = 'left'

    # move right
    elif keys[pygame.K_RIGHT] and snake.direction != "right" and snake.direction != "left":
        if snake.x <= 460:
            snake.x += snake.v
            snake.direction = 'right'

    # move down
    elif keys[pygame.K_DOWN] and snake.direction != "down" and snake.direction != "up":
        if snake.y <= 460:
            snake.y += snake.v
            snake.direction = 'down'

    # move up
    elif keys[pygame.K_UP] and snake.direction != "up" and snake.direction != "down":
        if snake.y >= 10:
            snake.y -= snake.v
            snake.direction = 'up'


    # maintain a velocity in last direction
    if snake.direction == 'left':
        if snake.x >= 10:
            snake.x -= snake.v
            
    elif snake.direction == "right":
        if snake.x <= 460:
            snake.x += snake.v
            
    elif snake.direction == "down":
        if snake.y <= 460:
            snake.y += snake.v
    elif snake.direction == "up":
        if snake.y >= 10:
            snake.y -= snake.v


    

    drawWindow(win)
        



    
