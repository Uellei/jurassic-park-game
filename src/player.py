import pygame

from camera import Camera


class Player:
    def __init__(self, position: tuple[float, float]):
        self.position = pygame.Vector2(position)
        self.speed = 250
        self.size = 32
        
    def update(self, dt: float):
        dir = pygame.Vector2()
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            dir.y -= 1
        if keys[pygame.K_a]:
            dir.x -= 1
        if keys[pygame.K_s]:
            dir.y += 1
        if keys[pygame.K_d]:
            dir.x += 1
            
        if dir.length_squared() > 0:
            dir = dir.normalize()
        
        self.position += dir * self.speed * dt
        
    def draw(self, surface: pygame.Surface,camera: "Camera") -> None:
        screen_position = self.position - camera.position
        
        pygame.draw.rect(
            surface,
            (180, 180, 180),
            (screen_position.x, screen_position.y, self.size, self.size)
        )