import speech_recognition as sr
def main():
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


        
main()