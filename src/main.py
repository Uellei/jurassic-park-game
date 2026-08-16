import pygame

from camera import Camera
from player import Player
from settings import WINDOW_HEIGHT, WINDOW_WIDTH
from world import World


class Game:
    def __init__(self):
        pygame.init()

        self.display_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )
        pygame.display.set_caption("Jurassic Park")

        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player((600, 300))
        self.camera = Camera((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.world = World((100, 100))

    def run(self):
        while self.running:
            # Calculate delta time (dt) for smooth movement
            # 60 FPS is the target frame rate, so we divide by 1000 to convert milliseconds to seconds
            dt = self.clock.tick(60) / 1000

            self.handle_events()
            self.update(dt)
            self.draw(dt)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt: float):
        # Player position -> Where the player is in the world
        # Camera position -> Where starts the region on the world that is being displayed on the screen
        # Screen position = player position - camera position -> Transform the player position from world coordinates to screen coordinates
        
        # Update playwer position based on input and delta time
        self.player.update(dt)
        
        # Update camera position to follow the player
        self.camera.update(self.player.position)
        self.world.update(dt, self.player.center)

    def draw(self, dt: float):
        self.display_surface.fill((30, 100, 30))

        self.world.draw(
            self.display_surface,
            dt,
            self.camera,
        )

        # Draw the player on the screen
        self.player.draw(
            self.display_surface,
            self.camera,
        )

        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()