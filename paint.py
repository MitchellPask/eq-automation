import pygame, os

draw_on = False # Check for left mouse button being pressed
last_pos = (0, 0)
black = (0, 0, 0)
white = (255,255,255)
radius = 20 # Size of brush
CWD = os.getcwd() # Currect working directory
IMG_DIR = CWD + '/saved_images'

# Create the folder to save images into if it does not already exist
if not os.path.exists(CWD + '/saved_images'):
    os.makedirs(CWD + '/saved_images')

# Open and fill a new pyGame paint screen
screen = pygame.display.set_mode((800,800))
screen.fill(black)

# Controls list in terminal
print("\n===== Controls =====")
print("Left click = draw \nSpacebar = clear screen \nEsc = close window \n'S' = save image \n")

# Draws a number of circles alone each point of the line, simulating a larger brush
def roundline(srf, color, start, end, radius=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int( start[0]+float(i)/distance*dx)
        y = int( start[1]+float(i)/distance*dy)
        pygame.draw.circle(srf, color, (x, y), radius)

# Counts the number of files in the saved image folder
def imgCount():
    img_count = len([name for name in os.listdir(IMG_DIR) if os.path.isfile(os.path.join(IMG_DIR, name))])
    return (img_count)

# This loop will handle all events while the paint program is active
try:
    while True:
        e = pygame.event.wait() # Keep program open
        # Exit if close window button pressed
        if e.type == pygame.QUIT:
            raise StopIteration
        # Exit if ESC key pressed
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                raise StopIteration
        # Toggle drawing on if left mouse button pressed
        if e.type == pygame.MOUSEBUTTONDOWN:
            color = (white)
            pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True
        # Toggle drawing off if left mouse button released
        if e.type == pygame.MOUSEBUTTONUP:
            draw_on = False
        # Draw line as cursor moves 
        if e.type == pygame.MOUSEMOTION:
            if draw_on:
                pygame.draw.circle(screen, color, e.pos, radius)
                roundline(screen, color, e.pos, last_pos,  radius)
            last_pos = e.pos
        # Reset screen if spacebar is pressed
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                screen.fill(black)
        # Save current drawing to saved_images folder if S key is pressed
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_s:
                newImage = '/img' + str(imgCount()) + '.png'
                pygame.image.save(screen, IMG_DIR +  newImage)
                print('Saved as: '+ newImage)
        pygame.display.flip() # Update the whole screen
# End the while cycle
except StopIteration:
    pass

# End the pyGame paint program
pygame.quit()
