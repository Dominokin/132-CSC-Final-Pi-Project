##class Sprite:
##    def __init__(self, ):
##        pass

#importing pygame
import pygame
#initialize pygame
pygame.init()
#set screen dimention variables
screen_width = 640
screen_height = 640

#creating the class to access sprites
class SpriteSheet():
    def __init__(self):
        #image supplied when instantiating the class
        self.idle = idle
        self.attack = attack
        self.death= death

    #method for displaying the image on the screen
    #get_img has 5 arguments: the frame, IE. the starting position of the sprite sheet
    #Width and height of the sprite sheet, which in this case, is 64 x 64
    #the scale to make the image larger (In the actual arguments, if you don't want it bigger
    #... set it to 1
    #and the color, which removes the background color from the sprite sheet
    #This will be set to (113, 102, 79, 225), which is Red, green, blue, and transparency
    #respectivly
    def get_img(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        #This part of the method will take the following arguments, respectivly:
        #the sprite sheet instantiated by the SpriteSheet class
        #the origin on the screen it will be rendered
        #frame * width and 0 is what frame will be rendered from the sprite sheet
        #width and height is how much of the frame will be shown...
        #In this case, we want all of the image to show
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image

    
#set the background color    
bg = (50, 50, 50)
#BAckground removal color
BG_REMOVE = (113, 102, 79, 255)


#set up the screen to display the image
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Spritesheets')

#Load in the sprite sheet
#Individual sprite images are 64 x 64 (IN THE CASE OF THE, MAKE SURE YOU CHECK)
sprite_sheet = pygame.image.load('AllCharacters/Bat/BatAttack_strip.png').convert_alpha()

#Create animation list, with the amount of frames per specific animation
animation_list = []
animation_steps = 8
last_update = pygame.time.get_ticks()
animation_cooldown = 75
frame = 0
for x in range(animation_steps):
    animation_list.append((SpriteSheet.get_img(sprite_sheet, x, 64, 64, 2, BG_REMOVE)))

#make a while loop to keep the game running
run = True
while run:
    #check for exiting game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #fill the screen with the BG color (in this case, grey)
    screen.fill(bg)

    #update animation
    current_time = pygame.time.get_ticks()
    #if the time that has past since the last update is longer than the animation cooldown...
    if current_time - last_update >= animation_cooldown:
        #update the frame and reset the recent update to the last tick
        frame += 1
        last_update = current_time
        if frame >= animation_steps[Bat.attack]:
            frame = 0
        
    #show the animation on the screen
    screen.blit(animation_list[frame], (0,0))

    #update to show the image on screen
    pygame.display.update()

pygame.quit()
