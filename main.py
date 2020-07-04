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

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
r4 = sr.Recognizer()
r5 = sr.Recognizer()
r6 = sr.Recognizer()
r7 = sr.Recognizer()

with sr.Microphone() as source:
    print('What do you want me to do?')
    print('Start speaking')
    audio = r1.listen(source)

if 'Google' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.google.com/search?q='
    with sr.Microphone() as source:
        print('search your query')
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print(error)
        except sr.RequestError as e:
            print('failed'.format(e))

if 'YouTube' in r3.recognize_google(audio):
    r3 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('search your query')
        audio = r3.listen(source)

        try:
            get = r3.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print(error)
        except sr.RequestError as e:
            print('failed'.format(e))

if 'Gmail' in r4.recognize_google(audio):
    r4 = sr.Recognizer()
    url = 'https://www.gmail.com/'
    with sr.Microphone() as source:
        print('Gmail is opening')
        audio = r4.listen(source)

        try:
            wb.get().open_new(url)
        except sr.UnknownValueError:
            print(error)
        except sr.RequestError as e:
            print('failed'.format(e))

if 'notepad' in r5.recognize_google(audio):
    r5 = sr.Recognizer()
    with sr.Microphone() as source:
        print('Notepad is opening')
        audio = r5.listen(source)

        try:
            subprocess.call('notepad.exe')
        except sr.UnknownValueError:
            print(error)
        except sr.RequestError as e:
            print('failed'.format(e))

if 'calculator' in r6.recognize_google(audio):
    r6 = sr.Recognizer()
    with sr.Microphone() as source:
        print('Calculator is opening')
        audio = r6.listen(source)

        try:
            subprocess.call('calc.exe')
        except sr.UnknownValueError:
            print(error)
        except sr.RequestError as e:
            print('failed'.format(e))

if 'paint' in r7.recognize_google(audio):
    r7 = sr.Recognizer()
    with sr.Microphone() as source:
        print('Paint is opening')
        audio = r7.listen(source)

        try:
            subprocess.call('mspaint.exe')
        except sr.UnknownValueError:
            print(error)
        except  sr.RequestError as e:
            print('failed'.format(e))