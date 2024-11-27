from transformers import pipeline
import os
import urllib3, socket
from urllib3.connection import HTTPConnection
import wave, math, contextlib
import speech_recognition as sr
import imageio
'''imageio.plugins.ffmpeg.download()'''
from moviepy.editor import *
from moviepy.editor import AudioFileClip
# from google.colab import drive
#from translate import Translator
# import gtts  
# from playsound import playsound
from googletrans import Translator, constants
# from pprint import pprint     
HTTPConnection.default_socket_options = ( HTTPConnection.default_socket_options + [(socket.SOL_SOCKET, socket.SO_SNDBUF, 1000000), (socket.SOL_SOCKET, socket.SO_RCVBUF, 1000000)])

def video_to_text(file_input):
  print('File Input : ' + file_input)
  transcribed_audio_file_name = "transcribed_speech.wav"
  audioclip = AudioFileClip(file_input)
  audioclip.write_audiofile(transcribed_audio_file_name)
  with contextlib.closing(wave.open(transcribed_audio_file_name,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
  total_duration = math.ceil(duration / 60)
  r = sr.Recognizer()
  os.remove("transcription.txt")
  for i in range(0, total_duration):
    with sr.AudioFile(transcribed_audio_file_name) as source:
        audio = r.record(source, offset=i*60, duration=60)
    f = open("transcription.txt", "a")
    f.write(r.recognize_google(audio))
    f.write(" ")
  f.close()
  f = open("transcription.txt", "r")
  content = f.read()
  f.close()
  print("END TRANSCRIPTION FUNCTION")
  return str(content)

def summarization():
  print("IN SUMMARIZATION FUNCTION")
  f = open("transcription.txt", "r")
  content = f.read()
  summarizer = pipeline('summarization', model = "facebook/bart-large-cnn")
  num_iters = int(len(content)/1000)
  summarized_text = []
  for i in range(0, num_iters + 1):
    start = 0
    start = i * 1000
    end = (i + 1) * 1000
    print("input text \n" + content[start:end])
    out = summarizer(content[start:end])
    print("OUT : ")
    print(out)
    print("Out[0]")
    print(out[0])
    out = out[0]
    out = out['summary_text']
    print("Summarized text\n"+out)
    summarized_text.append(out)
    f.close()
    print("END SUMMARIZATION FUNCTION")
    return summarized_text

def translate_func():
    translator = Translator()
    f = open("transcription.txt", "r")
    content = f.read()
    translation = translator.translate(content, dest="mr")
    tran_text=translation.text
    f.close()
    print(tran_text)  