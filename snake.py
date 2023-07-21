import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((900, 900))
clock = pygame.time.Clock()
running = True
dt = 0

# Global 
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)



# Game start
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print(tiles)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("lightblue")



    # Create grid
    # Grid will be 12x12 with tiles being 75px
    # TILE STATES: 0 = blank, 1 = snakeBody, 2 = snakeHead, 3 = Food 
    tiles = {}
    for a in range(12):
        y = a * 75
        for b in range(12):
            tiles[(a*75, b*75)] = 0
            tileVector = pygame.Vector2(b * 75, y)
            tile = pygame.Rect(tileVector[0], tileVector[1], 75, 75)
            pygame.draw.rect(screen, 'black', tile)
    


    # Create grid lines

            



    pygame.draw.circle(screen, "red", player_pos, 20)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()