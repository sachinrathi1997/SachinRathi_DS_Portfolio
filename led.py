import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D RGB LED Cube")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Cube dimensions
CUBE_SIZE = 200
NUM_LEDS = 3  # 3x3x3 cube

# Function to draw a single LED
def draw_led(x, y, color):
    radius = 10
    pygame.draw.circle(screen, color, (x, y), radius)

# Function to draw the LED cube
def draw_cube():
    offset = CUBE_SIZE // (NUM_LEDS - 1)
    for z in range(NUM_LEDS):
        for y in range(NUM_LEDS):
            for x in range(NUM_LEDS):
                # Calculate position
                pos_x = WIDTH // 2 + (x - 1) * offset - (z * 15)
                pos_y = HEIGHT // 2 + (y - 1) * offset - (z * 15)
                # Generate random color for demonstration
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                draw_led(pos_x, pos_y, color)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Draw the LED cube
    draw_cube()

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(2)  # 2 frames per second to slow down the color changes

pygame.quit()