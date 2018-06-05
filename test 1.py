from datetime import datetime
from gtts import gTTS
import os
import speech_recognition as sr

name='clementine'
say=''
def stt(say):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        recognize = r.recognize_google(audio)
        recognize=recognize.lower()
        print(recognize)
        return(recognize)

def time():
    now = datetime.now()
    timenow = 'It is '+str(now.hour)+':'+str(now.minute)+'.'
    speak(timenow)

def speak (speak):
    tts = gTTS(text = speak, lang ='en')
    tts.save('hello.mp3')
    os.system('mpg321 hello.mp3')


while (1):
    stt(say)
    if name in say:
        print('why???')
        speak('why??')
        #say = input()
        stt(say)
        if 'time'in say:
            time()
