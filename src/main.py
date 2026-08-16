import pygame

from camera import Camera
from player import Player
from rendering.grass import GrassManager


def main() -> None:
    pygame.init()
    
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Jurassic Park")
    
    clock = pygame.time.Clock()
    
    player = Player((600, 300))
    camera = Camera((1280, 720))
    grass = GrassManager(
        "../assets/grass",
        tile_size=15,
        place_range=[0,1]
    )
    
    for y in range(10):
        for x in range(10):
            grass.place_tile(
                (x, y),
                density=10,
                grass_options=[0]
            )
    
    running = True
    
    while running:
        # Calculate delta time (dt) for smooth movement
        # 60 FPS is the target frame rate, so we divide by 1000 to convert milliseconds to seconds
        dt = clock.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Player position -> Where the player is in the world
        # Camera position -> Where starts the region on the world that is being displayed on the screen
        # Screen position = player position - camera position -> Transform the player position from world coordinates to screen coordinates
        
        # Update playwer position based on input and delta time
        player.update(dt)
        
        # Update camera position to follow the player
        camera.update(player.position)
                
        screen.fill((30, 100, 30))
        
        grass.update_render(
            screen,
            dt,
            offset=camera.position
        )
        
        # Draw the player on the screen
        player.draw(screen, camera)
        
        pygame.display.flip()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()