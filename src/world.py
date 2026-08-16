import pygame

from camera import Camera
from rendering.grass import GrassManager


class World:
    def __init__(self, size: tuple[int, int]):
        self.size = size
        
        self.grass = GrassManager(
            "../assets/grass",
            tile_size=15,
            place_range=[0,1]
        )
        
        self._create_grass()
        
        
    def _create_grass(self) -> None:
        for y in range(10):
            for x in range(10):
                self.grass.place_tile(
                    (x, y),
                    density=10,
                    grass_options=[0]
                )
                
    def update(self, dt: float) -> None:
        pass
    
    def draw(self, surface: pygame.Surface, dt: float, camera: "Camera") -> None:
        self.grass.update_render(
            surface,
            dt,
            offset=camera.position
        )