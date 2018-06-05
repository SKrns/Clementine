from gtts import gTTS
import sys
import os
speak='start'
while 1:
	tts = gTTS(text = speak, lang ='en')
	tts.save('hello.mp3')
	if sys.platform=='linux2':
		os.system('mpg321 hello.mp3') # in linux (install mpg321)
	elif sys.platform=='win32':
		os.system('sWavPlayer hello.mp3') # in windows (install sWavPlayer)
	speak=input("input>>")
