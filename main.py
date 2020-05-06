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
        self.turn_pos = []
        self.turn_dir = []
        

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
        self.turning = False

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

        return new_block

    def turn(self, pos, direction):
        """pos is a tuple with coords x and y which is where the turn occurs"""
        snake.direction = direction
        snake.turning = True

        for block in self.blocks:
            block.turn_pos.append(pos)
            block.turn_dir.append(direction)
        

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

    # turn left
    if keys[pygame.K_LEFT] and snake.direction != 'left' and snake.direction != "right":
        if snake.x >= 10:
            # two conditions to maintain distance between blocks
            if snake.direction == "down":
                snake.turn((snake.blocks[0].x, snake.blocks[0].y + 10), 'left')
            elif snake.direction == "up":
                snake.turn((snake.blocks[0].x, snake.blocks[0].y - 10,), 'left')

    # turn right
    elif keys[pygame.K_RIGHT] and snake.direction != "right" and snake.direction != "left":
        if snake.x <= 460:
            if snake.direction == 'down':
                snake.turn((snake.blocks[0].x, snake.blocks[0].y + 10,), 'right')
            elif snake.direction == 'up':
                snake.turn((snake.blocks[0].x, snake.blocks[0].y - 10,), 'right')
    # turn down
    elif keys[pygame.K_DOWN] and snake.direction != "down" and snake.direction != "up":
        if snake.y <= 460:
            if snake.direction == "right":
                snake.turn((snake.blocks[0].x + 10, snake.blocks[0].y), 'down')
            elif snake.direction == "left":
                snake.turn((snake.blocks[0].x - 10, snake.blocks[0].y), 'down')

    # turn up
    elif keys[pygame.K_UP] and snake.direction != "up" and snake.direction != "down":
        if snake.y >= 10:
            if snake.direction == "left":
                snake.turn((snake.blocks[0].x - 10, snake.blocks[0].y), 'up')
            elif snake.direction == "right":
                snake.turn((snake.blocks[0].x+ 10, snake.blocks[0].y), 'up')

    # for testing
    elif keys[pygame.K_SPACE]:
        snake.grow()
    
    for block in snake.blocks:
        # maintain a velocity in last direction
        if block.direction == 'left':
            if block.x >= 10:
                block.x -= snake.v
            # hit a wall
            else:
                run = False
                
        elif block.direction == "right":
            if block.x <= 460:
                block.x += snake.v
            else:
                run = False
                
        elif block.direction == "down":
            if block.y <= 460:
                block.y += snake.v
            else:
                run = False
        elif block.direction == "up":
            if block.y >= 10:
                block.y -= snake.v
            else:
                run = False


    # check for turning blocks
    if snake.turning:
        for block in snake.blocks:
            if snake.blocks.index(block) == 0 and len(block.turn_pos) != 0:
                print('1')
                block.direction = block.turn_dir[0]

                block.turn_dir.pop(0)
                block.turn_pos.pop(0)
        
            # secondary block turning
            elif len(block.turn_pos) != 0 and block.x == block.turn_pos[0][0] and block.y == block.turn_pos[0][1]:
                block.direction = block.turn_dir[0]

                block.turn_dir.pop(0)
                block.turn_pos.pop(0)

        # count non-turning blocks
        for block in snake.blocks:
            count = 0
            if len(block.turn_dir) == 0 and len(block.turn_pos) == 0:
                count += 1

        # there are no turns still active
        if count == len(snake.blocks):
            snake.turning = False
                
    drawWindow(win)
        

print('GAME OVER')

    
