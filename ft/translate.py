# -*- coding: utf-8 -*-

kimi = 'sk-your key'
from openai import OpenAI

client = OpenAI(api_key=kimi, base_url="https://api.moonshot.cn/v1")

def translate_text(text):
    response = client.chat.completions.create(
        model = "moonshot-v1-8k",
        messages=[
            {"role": "system", "content": "You are a translator. Translate the following Chinese text to English."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()


from google.cloud import translate_v2 as translate

def translate_text_google(text):
    client = translate.Client()
    result = client.translate(text, target_language='en', source_language='zh-cn')
    return result['translatedText']
