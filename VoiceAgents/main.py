from dotenv import load_dotenv
import speech_recognition as sr
from openai import OpenAI
from gtts import gTTS
import pygame
import pyttsx3
import os
def main():
    load_dotenv()
    key = os.getenv('GOOGLE_API_KEY')
    #print(key)
    client = OpenAI(
    api_key=key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    
    # to build voice agent first we need to convert voice into text
    # am using chain architecture 
    # initzalize voice recognition
    r = sr.Recognizer()


    # now we need to access to user micro phone
    with sr.Microphone() as source:
        # first we need to remove nocie form voice
        r.adjust_for_ambient_noise(source)

        # now if user pause for 2 second
        r.pause_threshold=2

        print('Voice Listening..........')

        audio= r.listen(source)

        print('Your Voice into Text is...........')

        stt= r.recognize_google(audio)

        print("You Say : " , stt)

  
        # now sending this text into llm 
        System_Prompt="""
          You are an expert voice ai agent . you will always replay with postivate tone
           """
        response = client.chat.completions.create(
          model="gemini-3.1-flash-lite-preview",
          messages=[
        {"role":"system" , "content":System_Prompt},
        {"role": "user", "content": stt}
        ]
        )
        #print("Ai Response : " , response.choices[0].message.content)
        tts=response.choices[0].message.content
       # engine = pyttsx3.init()
       # engine.say(tts)
       # engine.runAndWait()

        tts_text = response.choices[0].message.content

# Convert text to speech
        tts = gTTS(text=tts_text, lang='en')
        tts.save("output.mp3")

# Play audio
        pygame.mixer.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()




main()