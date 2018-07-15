import pygame


class ImageRenderer:
    def __init__(self, image_url):
        self.image = pygame.image.load(image_url)

    def render(self, canvas, x, y):
        width = self.image.get_width()
        height = self.image.get_height()
        render_pos = (x - width / 2, y - height / 2)
        canvas.blit(self.image, render_pos)
