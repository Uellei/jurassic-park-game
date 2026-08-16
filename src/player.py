import pygame


class Player:
    def __init__(self, pos: tuple[float, float]):
        self.pos = pygame.Vector2(pos)
        self.speed = 250
        
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
        
        self.pos += dir * self.speed * dt
        
    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(
            surface,
            (180, 180, 180),
            (self.pos.x, self.pos.y, 32, 32)
        )