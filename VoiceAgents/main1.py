from dotenv import load_dotenv
import speech_recognition as sr
from openai import OpenAI
from gtts import gTTS
import pygame
import tempfile
import os

def speak(text):
    # Create temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        temp_filename = fp.name

    tts = gTTS(text=text, lang='en')
    tts.save(temp_filename)

    pygame.mixer.init()
    pygame.mixer.music.load(temp_filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.quit()
    os.remove(temp_filename)


def main():
    load_dotenv()
    key = os.getenv('GOOGLE_API_KEY')

    client = OpenAI(
        api_key=key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    r = sr.Recognizer()

    print("🚀 Voice Agent Started (Say 'exit' to stop)\n")

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=2
        while True:
            try:
                print("🎤 Listening...")
                audio = r.listen(source)

                print("🧠 Converting...")
                stt = r.recognize_google(audio)

                print("🗣️ You:", stt)

                # EXIT CONDITION
                if stt.lower() in ["exit", "quit", "stop"]:
                    speak("Goodbye! Have a great day.")
                    print("👋 Exiting...")
                    break

                # LLM CALL
                response = client.chat.completions.create(
                    model="gemini-3.1-flash-lite-preview",
                    messages=[
                        {"role": "system", "content": "You are a helpful and positive voice AI assistant."},
                        {"role": "user", "content": stt}
                    ]
                )

                ai_text = response.choices[0].message.content
                print("🤖 AI:", ai_text)

                # SPEAK RESPONSE
                speak(ai_text)

            except sr.UnknownValueError:
                print("😅 Didn't catch that, try again...")
            except sr.RequestError:
                print("❌ Speech service error")
            except Exception as e:
                print("❌ Error:", e)


if __name__ == "__main__":
    main()