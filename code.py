# -*- coding: utf-8 -*-
"""Btech_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NuRtpuC_gevKNrCJ2xuj0cV59muXkkNA

## **Video to text**
"""

"""pip install Wave
pip install moviepy
pip install SpeechRecognition

!pip3 install imageio==2.4.1

!pip install --upgrade imageio-ffmpeg
"""
import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip
from google.colab import drive
from transformers import pipeline
import urllib3, socket
from urllib3.connection import HTTPConnection
from translate import Translator
import gtts  
from playsound import playsound

drive.mount('/content/drive',force_remount=True)

transcribed_audio_file_name = "transcribed_speech.wav"
video_file_name = "/Dest/ProJect/static/SampleVideo.mp4"

audioclip = AudioFileClip(video_file_name)
audioclip.write_audiofile(transcribed_audio_file_name)

with contextlib.closing(wave.open(transcribed_audio_file_name,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)

total_duration = math.ceil(duration / 60)

r = sr.Recognizer()

for i in range(0, total_duration):
    with sr.AudioFile(transcribed_audio_file_name) as source:
        audio = r.record(source, offset=i*60, duration=60)
    f = open("transcription.txt", "w")
    f.write(r.recognize_google(audio))
    f.write(" ")
f.close()

#Checking the generated text
f = open("transcription.txt", "r")
content = f.read()
print(content)
f.close()

"""## **Text Summarization**"""

"""!pip install transformers"""


    
HTTPConnection.default_socket_options = ( HTTPConnection.default_socket_options + [(socket.SOL_SOCKET, socket.SO_SNDBUF, 1000000), (socket.SOL_SOCKET, socket.SO_RCVBUF, 1000000)])

summarizer = pipeline('summarization')

num_iters = int(len(content)/1000)
summarized_text = []
for i in range(0, num_iters + 1):
  start = 0
  start = i * 1000
  end = (i + 1) * 1000
  print("input text \n" + content[start:end])
  out = summarizer(content[start:end])
  out = out[0]
  out = out['summary_text']
  print("Summarized text\n"+out)
  summarized_text.append(out)

#print(summarized_text)

len(str(summarized_text))

str(summarized_text)

"""## **Translation**

!pip install translate"""
translator= Translator(from_lang="english",to_lang="marathi")
translation = translator.translate("good morning")
print(translation)

'''pip install googletrans==3.1.0a0'''

from googletrans import Translator, constants
from pprint import pprint

translator = Translator()

translation = translator.translate(content, dest="mr")
tran_text=translation.text
print(tran_text)

type(tran_text)

"""## **Text to audio**

!pip install gTTS

!pip install playsound==1.2.2

! pip install pyttsx3

pip install pygobject"""



t1 = gtts.gTTS("Welcome to javaTpoint",lang="en")

# save the audio file  
t1.save("welcome.mp3")

playsound("welcome.mp3")