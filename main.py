import pygame

print("Start")
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
pygame.display.set_caption("Mountain Shooter")
print("End")

print("Start Loop")
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close window
            quit() #end pygame