import gtts
from playsound import playsound
import os

def speech(text:str,file_name:str):
    tts = gtts.gTTS(text)
    file_name=file_name+'.mp3'
    tts.save(file_name)
    playsound(file_name)
    os.remove(file_name)

text=str(input('Enter what you meant to say: '))
file_name=str(input('Enter the path where you mean to save file: '))
speech(text,file_name)