import pygame
import sys
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Set up the screen
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, screen_width, 0, screen_height)
# glOrtho(-100, screen_width, -100, screen_height, -1, 1)
glMatrixMode(GL_MODELVIEW)

# Create block class
class Block:
    def __init__(self, mass, pos, vel, color):
        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.color = color
        if len(str(self.mass)) == 1:
            self.size = len(str(self.mass)) * 40
        else:
            self.size = len(str(self.mass)) * 10

    def render(self):
        pygame.draw.rect(screen, self.color, (self.pos, (screen_height/2) - self.size, self.size, self.size))

    def update(self, dt):
        self.pos += self.vel * dt

# Instantiate two blocks
b1Pos = 200  
b1Mass = 1

user_input = ''
user_prompt = True

while user_prompt:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                user_prompt = False
        elif event.type == KEYUP:
            if event.key == K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

    screen.fill((0, 0, 0))  # Set the background color to black
    font = pygame.font.Font(None, 30)
    text = font.render(f"Enter number of digits in pi (after 3.) you want to check: {user_input}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.update()

b2Mass = 100 ** int(user_input)
print(f"Second mass is {b2Mass}")
b2Pos = 300  
b2vel = -500

# Calculate the value of pi based on the user's input
digits = int(user_input)
pi_value = str(math.pi)[:2+digits]  # Get the specified number of digits from pi

block1 = Block(b1Mass, b1Pos, 0, (0, 0, 255))
block2 = Block(b2Mass, b2Pos, b2vel, (255, 0, 0))

# Main game loop
count = 0
dt = 0.001
running = True

# Add a horizontal line
line_y = screen_height // 2  # Adjust the y-coordinate of the line
line_color = (255, 255, 255)  # Set the color of the line to white

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update block positions
    block1.update(dt)
    block2.update(dt)

    # Check wall collision
    if block1.pos <= 0:
        block1.pos = 0
        block1.vel *= -1
        count += 1

    # Check block collision
    if block1.pos + block1.size >= block2.pos:
        block1.pos = block2.pos - block1.size

        m1 = block1.mass
        m2 = block2.mass
        v1i = block1.vel
        v2i = block2.vel

        mom1 = m1 * v1i + m2 * v2i

        v2f = (m1 * v2i - m1 * v1i - mom1) / (-1 * m2 - m1)
        v1f = v2i + v2f - v1i

        block1.vel = v1f
        block2.vel = v2f
        count += 1

    # Render the frame
    screen.fill((0, 0, 0))  # Set the background color to black
    font = pygame.font.Font(None, 30)
    text = font.render(f"Collisions: {count}", True, (255, 255, 255))  # Set text color to white
    screen.blit(text, (10, 10))

    # Render the pi value text
    text_pi = font.render(f"Expected pi value: {pi_value}", True, (255, 255, 255))
    screen.blit(text_pi, (10, 50))

    # Display mass value
    text = font.render(f"M1: {b1Mass}   M2: {b2Mass}", True, (255, 255, 255))
    screen.blit(text, (10, (screen_height/2) + 30))  # Adjusted text position

    # Draw the horizontal line
    pygame.draw.line(screen, line_color, (0, line_y), (screen_width, line_y), 1)

    block1.render()
    block2.render()

    pygame.display.flip()
    clock.tick(60)
