# Import pygame module
import pygame
# Initialize pygame
pygame.init()
# Set initial window size
win = pygame.display.set_mode((500, 500))
# Set caption on display window
pygame.display.set_caption("Epic Game")
# Initialize character position, width, and height, vel
x = 50
y = 50
width = 40
height = 60
vel = 20
# Main loop that runs while game is running
run = True
while run:
    # .1 second timer delay
    pygame.time.delay(100)
    # Loop through every event and check if they have happened
    for event in pygame.event.get():
        # If quit button in top right corner is pressed
        if event.type == pygame.QUIT:
            run = False
    # Checks for key presses
    keys = pygame.key.get_pressed()
    # Checks for left key press
    if keys[pygame.K_LEFT]:
        x -= vel
    # Checks for right key press
    if keys[pygame.K_RIGHT]:
        x += vel
    # Checks for up key press
    if keys[pygame.K_UP]:
        y -= vel
    # Checks for down key press
    if keys[pygame.K_DOWN]:
        y += vel
    #Fill screen with black so your rectangle does not keep drawing
    win.fill((0,0,0))
    # Now draw our pygame rectangle character
    pygame.draw.rect(win, (255, 0, 0), (x,y,width,height))
    # Now we need to update our display
    pygame.display.update() 

pygame.quit()
