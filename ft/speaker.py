
# -*- coding: utf-8 -*-

from io import BytesIO
import wave
import sounddevice as sd
import numpy as np
from pydub import AudioSegment
import pygame

def play_audio(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def play_audio_zoom_in_memory(tts):
    # Convert gTTS object to BytesIO
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    
    # Load audio from BytesIO
    audio = AudioSegment.from_mp3(fp)
    samples = np.array(audio.get_array_of_samples())
    
    # Play audio through BlackHole
    sd.play(samples, audio.frame_rate, device='BlackHole 2ch')
    sd.wait()


def play_audio_zoom(file):
    audio = AudioSegment.from_mp3(file)
    audio.export("temp.wav", format="wav")
    
    # Read the WAV file
    audio = AudioSegment.from_wav(file)
    
    # Convert to numpy array
    samples = np.array(audio.get_array_of_samples())
    sd.play(samples, audio.frame_rate, device='BlackHole 2ch')
    sd.wait()