import pygame


class Camera:
    def __init__(self, screen_size: tuple[int, int]):
        self.position = pygame.Vector2(0, 0)
        self.screen_size = pygame.Vector2(screen_size)
        
    def update(self, target_position: pygame.Vector2) -> None:
        # Center the camera on the target position
        self.position = target_position - self.screen_size / 2