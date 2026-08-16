import pygame


def main() -> None:
    pygame.init()
    
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Jurassic Park")
    
    clock = pygame.time.Clock()
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill((30, 100, 30))
        
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
    
if __name__ == "__main__":
    main()