
# -*- coding: utf-8 -*-

import speech_recognition as sr

def recognize_speech_from_mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak...")
        audio = r.listen(source)
        try:
            # Recognize Chinese speech
            text = r.recognize_google(audio, language="zh-CN")
            print(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")