import pygame

SIZE = WIDTH, HEIGHT = 410 , 408
BACKGROUND_COLOR = pygame.Color('black') 
FPS = 10 

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        self.FONT_SIZE = 15
        self.font_obj = pygame.font.Font('./fonts/GROBOLD.ttf', self.FONT_SIZE)
        self.screen = pygame.display.set_mode(SIZE)
        self.FONT_TOP_MARGIN = 50
        self.FONT_BOTTOM_MARGIN = 574
        self.clock = pygame.time.Clock()
        self.background_image = pygame.image.load("robot1.png")
        self.images = []
        # self.images.append(pygame.image.load('images/assistant1.png'))
        # self.images.append(pygame.image.load('images/assistant2.png'))
        self.images.append(pygame.image.load('images/assistant3.png'))
        self.images.append(pygame.image.load('images/assistant4.png'))
        self.images.append(pygame.image.load('images/assistant5.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(10, 10, 400, 235)

    def update(self):
        self.index += 1
        
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]

    def talks(self):
        odin_talks = main1.odin_speak()
        talk = self.font_obj.render(odin_talks, True, (255, 255, 255))
        talk_pos = talk.get_rect()
        talk_pos.centerx = self.background_image.get_rect().centerx
        talk_pos.centery = self.FONT_TOP_MARGIN
        self.screen.blit(talk, talk_pos)

        odin_talks = main1.respond()
        talk = self.font_obj.render(odin_talks, True, (255, 255, 255))
        talk_pos = talk.get_rect()
        talk_pos.centerx = self.background_image.get_rect().centerx+100
        talk_pos.centery = self.FONT_TOP_MARGIN+400
        self.screen.blit(talk, talk_pos)

    def main(self):

        pygame.display.set_caption('Your Personal Assistant')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.update()
            self.screen.fill(BACKGROUND_COLOR)
            pygame.draw.ellipse(self.screen, pygame.Color("white"), (90, 100, 20, 10))
            pygame.draw.ellipse(self.screen, pygame.Color("white"), (115, 85, 45, 20))
            pygame.draw.ellipse(self.screen, pygame.Color("white"), (160, 10, 180, 100))
            pygame.draw.ellipse(self.screen, pygame.Color("white"), (190, 210, 180, 100))
            pygame.draw.ellipse(self.screen, pygame.Color("white"), (340, 310, 45, 20))
            pygame.draw.ellipse(self.screen, pygame.Color("white"), (390, 330, 20, 10))
            # pygame.draw.circle(screen, white, (150,150), 75)
            self.screen.blit(self.background_image, [0, 0])
            my_group = pygame.sprite.Group(self)
            my_group.draw(self.screen)
            self.talks()
            pygame.display.flip()
            self.clock.tick(5)

if __name__ == '__main__':
    pygame.init()
    my_sprite = MySprite()
    my_sprite.main()