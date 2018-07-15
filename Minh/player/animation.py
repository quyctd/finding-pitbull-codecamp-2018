import pygame


class Animation:

    def __init__(self, image_urls, loop=False):
        self.images = [pygame.image.load(image_url) for image_url in image_urls]
        self.image_index = 0
        self.time = 0
        self.allow = False
        self.finished = False
        self.loop = loop

    def render(self, canvas, x, y):
        if not self.finished or self.loop:
            current_image = self.images[self.image_index]
            render_pos = (x, y)
            canvas.blit(current_image, render_pos)
            now = pygame.time.get_ticks()
            if self.time == 0:
                self.time = now
            else:
                if now - self.time >= 200:
                    self.time = now
                    if self.image_index < len(self.images) - 1:
                        self.image_index += 1
                    elif self.loop:
                        self.image_index = 0
                    else:
                        self.finished = True
                        self.allow = True
