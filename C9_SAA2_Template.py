# Import pygame
import pygame
# Initialize pygame
pygame.init() 
# Create a game screen with width=600 and height=600 and name it as "screen"
screen = pygame.display.set_mode((600,600))
# Set the game title as "Car Racing Game"
pygame.display.set_caption("Car Racing Game")
# Game loop
carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            carryOn = False
    
    # Store the background image name with extension in a variable "bgImg_name"
    bgImg_name = "road.png"
    # Load the background image and store it in a variable "bgImg"
    bgImg = pygame.image.load(bgImg_name).convert_alpha()
    # Scale the background image to fit the screen with (width, height) = (650, 600)
    # and store scaled image in a variable "bgImg_scaled"
    bgImg_scaled = pygame.transform.smoothscale(bgImg,(650,600))
    # Display scaled background image on screen at location (0, 0)
    screen.blit(bgImg_scaled,(0,0))
    
    # Store the yellow car image name with extension in a variable "yellow_car_name"
    yellow_car_name = "yellow_car.png"
    # Load the yellow car image and store it in a variable "yellow_car"
    yellow_car = pygame.image.load(yellow_car_name).convert_alpha()
    # Scale the yellow car image to fit the screen with (width, height) = (230, 150)
    # and store scaled image in a variable "yellow_car_scaled"
    yellow_car_scaled = pygame.transform.smoothscale(yellow_car,(230,150))
    # Display scaled yellow car image on screen at location (40,400)
    screen.blit(yellow_car_scaled,(40,400))
    
    # Store the red car image name with extension in a variable "red_car_name"
    red_car_name = "red_car.png"
    # Load the red car image and store it in a variable "red_car"
    red_car = pygame.image.load(red_car_name).convert_alpha()
    # Scale the red car image to fit the screen with (width, height) = (80,130)
    # and store scaled image it in a variable "red_car_scaled"
    red_car_scaled = pygame.transform.smoothscale(red_car,(80,130))
    # Display scaled red car image on screen at location (215,405)
    screen.blit(red_car_scaled,(215,405))
    
    # Store the stone image name with extension in a variable "stone_name"

    # Load the stone image and store it in a variable "stone"

    # Scale the stone image to fit the screen with (width, height) = (80,100)
    # and store scaled image in a variable "stone_scaled"

    # Display scaled stone image on screen at location (300,100)

    
    # Update the contents of the display
    pygame.display.flip()

# Quit the game 
pygame.quit()
