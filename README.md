# free_talk_in_meeting
use different language in meeting

# Free Talk in Meeting

This project allows you to speak in one language during a meeting while the other participants hear it in another language. It uses speech recognition, translation, and text-to-speech technologies to achieve this seamless communication.

## Process Overview

1. **Speech Recognition**: The system listens to your speech using the computer's microphone.
2. **Language Translation**: The recognized speech is translated from the source language to the target language.
3. **Text-to-Speech**: The translated text is converted into speech.
4. **Audio Output**: The generated speech is played through a virtual audio device.
5. **Zoom Integration**: The virtual audio device is set as the input for your Zoom meeting.

## Components

- `ft/mic.py`: Handles speech recognition using the `speech_recognition` library.
- `ft/tts.py`: Converts text to speech using the `gTTS` (Google Text-to-Speech) library.
- `ft/speaker.py`: Manages audio playback, including playing audio through the virtual device.

## Setup

1. Install the required dependencies (speech_recognition, gtts, sounddevice, pydub, pygame).
2. Install and configure the BlackHole 2ch virtual audio device.
3. Set up your Zoom meeting to use BlackHole 2ch as the audio input.

## Usage

1. Run the main script (not provided in the current context).
2. Speak in your preferred language (currently set to Chinese).
3. The system will recognize your speech, translate it to English, generate speech, and play it through BlackHole 2ch.
4. Participants in your Zoom meeting will hear the English translation of your speech.

Note: The current implementation supports Chinese to English translation. Modify the language settings in the code to support other language pairs.

