import os
import sys
from pygame import mixer
import urllib.request
client_id = "Z01Q58njd1DR51CGn2xN"
client_secret = "5zwzXooolL"

while (1):

    #read=input()
    read='기섭 지금 뭐하는 거니?'
    encText = urllib.parse.quote(read)
    data = "speaker=mijin&speed=0&text=" + encText;
    url = "https://openapi.naver.com/v1/voice/tts.bin"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()
    if(rescode==200):
        print("TTS mp3 저장")
        response_body = response.read()
        with open('1111.mp3', 'wb') as f:
            f.write(response_body)

    else:
        print("Error Code:" + rescode)
    mixer.init()
    mixer.music.load("1111.mp3")
    mixer.music.play()
