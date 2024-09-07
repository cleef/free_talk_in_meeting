
# -*- coding: utf-8 -*-

from gtts import gTTS
import os

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    return tts