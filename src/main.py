import pygame

from player import Player


def main() -> None:
    pygame.init()
    
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Jurassic Park")
    
    clock = pygame.time.Clock()
    
    player = Player((600, 300))
    
    running = True
    
    while running:
        # Calculate delta time (dt) for smooth movement
        # 60 FPS is the target frame rate, so we divide by 1000 to convert milliseconds to seconds
        dt = clock.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update playwer position based on input and delta time
        player.update(dt)
                
        screen.fill((30, 100, 30))
        
        # Draw the player on the screen
        player.draw(screen)
        
        pygame.display.flip()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()