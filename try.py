import speech_recognition as sr
import webbrowser as wb
import subprocess
from time import ctime
import time
import os
import playsound
from gtts import gTTS
import random
import pygame

SIZE = WIDTH, HEIGHT = 410 , 408
BACKGROUND_COLOR = pygame.Color('black')
FPS = 10

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        self.r = sr.Recognizer()
        self.FONT_SIZE = 15
        self.font_obj = pygame.font.Font('./fonts/GROBOLD.ttf', self.FONT_SIZE)
        self.screen = pygame.display.set_mode(SIZE)
        self.FONT_TOP_MARGIN = 50
        self.FONT_BOTTOM_MARGIN = 574
        self.clock = pygame.time.Clock()
        self.sec = 1
        self.background_image = pygame.image.load("robot1.png")
        self.try_text=''
        self.voice_data = ''
        self.images = []
        # self.images.append(pygame.image.load('images/assistant1.png'))
        # self.images.append(pygame.image.load('images/assistant2.png'))
        self.images.append(pygame.image.load('images/assistant3.png'))
        self.images.append(pygame.image.load('images/assistant4.png'))
        self.images.append(pygame.image.load('images/assistant5.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(10, 10, 400, 235)
        self.gem=True
    def record_audio(self,ask=False):
        with sr.Microphone() as source:
            if ask:
                self.odin_speak(ask)
            audio = self.r.listen(source)
            try:
                self.voice_data = self.r.recognize_google(audio)
                print(self.voice_data)
                user_talks = self.voice_data
                talk1 = self.font_obj.render(user_talks, True, (0, 0, 0))
                talk_pos1 = talk1.get_rect()
                talk_pos1.center = ((275,250))
                self.screen.blit(talk1, talk_pos1)
                self.update()
                pygame.display.update()
            except sr.UnknownValueError:
                self.odin_speak('Sorry I did not get it')
            except sr.RequestError:
                self.odin_speak('Sorry my service is down')
            pygame.draw.ellipse(self.screen, pygame.Color("white"), (110, 245, 250, 70))
            return self.voice_data

    def odin_speak(self,audio_string) :
        tts = gTTS(text=audio_string, lang='en')
        r = random.randint(1, 10000000)
        audio_file = 'audio-' + str(r) + '.mp3'
        tts.save(audio_file)
        print(audio_string)
        odin_talks = audio_string
        talk = self.font_obj.render(odin_talks, True, (0, 0, 0))
        talk_pos = talk.get_rect()
        talk_pos.center = ((270,63))
        self.screen.blit(talk, talk_pos)
        self.update()
        pygame.display.update()
        playsound.playsound(audio_file)
        os.remove(audio_file)
        pygame.draw.ellipse(self.screen, pygame.Color("white"), (150, 28, 250, 70))

    def greeting(self):
        self.odin_speak('Hey,this is Odin.')
        self.odin_speak('your personal virtual assistant.')
        self.odin_speak('How can I help you?')
        self.sec = self.sec + 1

    def respond(self,voice_data):
        if 'time' in voice_data:
            self.odin_speak(ctime())
        if 'Google' in voice_data:
            self.odin_speak('Your search result is ready')
            search = self.record_audio('What do you want to search')
            url = 'https://www.google.com/search?q='
            wb.get().open_new(url + search)
        if 'YouTube' in voice_data:
            self.odin_speak('Here is what I found')
            search = self.record_audio('What do you want to watch')
            url = 'https://www.youtube.com/results?search_query='
            wb.get().open_new(url + search)
        if 'Gmail' in voice_data:
            self.odin_speak('Opening Gmail...')
            url = 'https://www.gmail.com/'
            wb.get().open_new(url)
        if 'Notepad' in voice_data:
            self.odin_speak('Opening notepad...')
            subprocess.call('notepad.exe')
        if 'calculator' in voice_data:
            self.odin_speak('Opening calculator...')
            subprocess.call('calc.exe')
        if 'Paint' in voice_data:
            self.odin_speak('Opening paint...')
            subprocess.call('mspaint.exe')
        if 'exit' in voice_data:
            exit()

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


    def main(self):
        pygame.display.set_caption('Your Personal Assistant')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.update()
            self.screen.fill(BACKGROUND_COLOR)
            self.screen.blit(self.background_image, [0, 0])
            pygame.draw.ellipse(self.screen, pygame.Color("white"), (90, 100, 20, 10))
            pygame.draw.ellipse(self.screen, pygame.Color("white"), (115, 85, 45, 20))
            pygame.draw.ellipse(self.screen, pygame.Color("white"), (150, 28, 250, 70))
            pygame.draw.ellipse(self.screen, pygame.Color("white"), (110, 245, 250, 70))
            pygame.draw.ellipse(self.screen, pygame.Color("white"), (340, 310, 45, 20))
            pygame.draw.ellipse(self.screen, pygame.Color("white"), (390, 330, 20, 10))
            my_group = pygame.sprite.Group(self)
            my_group.draw(self.screen)
            self.update()
            pygame.display.update()
            if self.sec == 1 :
                self.greeting()
            self.voice_data = self.record_audio()
            self.respond(self.voice_data)
            # self.clock.tick(10)

if __name__ == '__main__':
    pygame.init()
    my_sprite = MySprite()
    my_sprite.main()
