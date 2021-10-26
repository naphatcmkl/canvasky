# ถ้าอ่านอยู่ก็จะบอกว่าไฟล์นี้มีไว้ Test Function ต่างๆ เฉยๆ เพื่อเอาไปต่อยอดในงานจริง

# Import Speech Recognition Package
import speech_recognition as sr

# Declare r as an receiver
r = sr.Recognizer()

# Let we receive an input from microphone
with sr.Microphone() as source:
    print("Speak: ")

    # Listen
    audio = r.listen(source)

    try:
        # Translate word into text
        text = r.recognize_google(audio)

        # If the word we say translate == champ,
        if text == "champ":
            # Then print you're here.
            print("You're here")
        else:
            print("Bye bye!")
    except:
        print("Sorry, couldn't recognize your voice.")
