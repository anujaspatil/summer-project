'''import speech_recognition as sr

r=sr.Recognizer()
print(sr.Microphone.list_microphone_names())
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1)
    # r.energy_threshold()
    print("say anything : ")
    audio= r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
    except:
        print("sorry, could not recognise")'''

import pyaudio
import speech_recognition as sr
import webbrowser as wb
import subprocess
from time import ctime
import time
import os
import playsound
from gtts import gTTS
import random

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            odin_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            odin_speak('Sorry I did not get it')
        except sr.RequestError:
            odin_speak('Sorry my service is down')
        return voice_data

def odin_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    print(audio_string)
    playsound.playsound(audio_file)
    os.remove(audio_file)

def respond(voice_data):
    if 'time' in voice_data:
        odin_speak(ctime())
    if 'Google' in voice_data:
        odin_speak('Your search result is ready')
        search = record_audio('What do you want to search')
        url = 'https://www.google.com/search?q='
        wb.get().open_new(url + search)
    if 'YouTube' in voice_data:
        odin_speak('Here is what I found')
        search = record_audio('What do you want to watch')
        url = 'https://www.youtube.com/results?search_query='
        wb.get().open_new(url + search)
    if 'Gmail' in voice_data:
        odin_speak('Opening Gmail')
        url = 'https://www.gmail.com/'
        wb.get().open_new(url)
    if 'Notepad' in voice_data:
        odin_speak('Opening notepad')
        subprocess.call('notepad.exe')
    if 'calculator' in voice_data:
        odin_speak('Opening calculator')
        subprocess.call('calc.exe')
    if 'Paint' in voice_data:
        odin_speak('Opening paint')
        subprocess.call('mspaint.exe')
    if 'exit' in voice_data:
        exit()

time.sleep(1)
odin_speak('Hey this is Odin, your personal virtual assistant. How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)