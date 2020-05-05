import pygame

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

class Block(object):
    def __init__(self, x, y, l, direction):
        self.x = x
        self.y = y
        self.l = l
        self.direction = direction

    def draw(self):
        pygame.draw.rect(win, (50,205,50), ((self.x, self.y), (self.l,self.l)))
            

class Snake(object):
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.v = 10
        self.length = length
        self.direction = 'down'
        self.blocks = [Block(self.x, self.y, 30, self.direction)]
        self.turn = False

    def grow(self):
        self.length += 1
        
        if self.direction == "left":
            new_block = Block(self.blocks[0].x + 40*(snake.length), self.blocks[0].y, 30, 'left')
        elif self.direction == "right":
            new_block = Block(self.blocks[0].x - 40*(snake.length), self.blocks[0].y, 30, 'right')
        elif self.direction == 'down':
            new_block = Block(self.blocks[0].x, self.blocks[0].y - 40*(snake.length), 30, 'down')
        else:
            new_block = Block(self.blocks[0].x, self.blocks[0].y + 40*(snake.length), 30, 'up')

        snake.blocks.append(new_block)

    def turn(self, pos, direction):
        """Start is a tuple of x and y which is where the turn occurs"""
        self.turn = True
        snake.direction = direction
            
            

    def draw(self):
        for block in self.blocks:
            block.draw()
            

snake = Snake(40, 50, 1)

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
            snake.turn((snake.x, snake.y), 'left')

    # move right
    elif keys[pygame.K_RIGHT] and snake.direction != "right" and snake.direction != "left":
        if snake.x <= 460:
            snake.turn((snake.x, snake.y), 'right')

    # move down
    elif keys[pygame.K_DOWN] and snake.direction != "down" and snake.direction != "up":
        if snake.y <= 460:
            snake.turn((snake.x, snake.y), 'down')
            snake.grow()

    # move up
    elif keys[pygame.K_UP] and snake.direction != "up" and snake.direction != "down":
        if snake.y >= 10:
            snake.turn((snake.x, snake.y), 'up')


    for block in snake.blocks:
        # maintain a velocity in last direction
        if block.direction == 'left':
            if block.x >= 10:
                block.x -= snake.v
                
        elif block.direction == "right":
            if block.x <= 460:
                block.x += snake.v
                
        elif block.direction == "down":
            if block.y <= 460:
                block.y += snake.v
        elif block.direction == "up":
            if block.y >= 10:
                block.y -= snake.v

    print('snake pos is', snake.x, snake.y)
    drawWindow(win)
        



    
