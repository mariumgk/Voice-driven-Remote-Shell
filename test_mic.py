import speech_recognition as sr

def listen_once():
    r = sr.Recognizer()

    # Use the default microphone as source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... (1 second)")
        r.adjust_for_ambient_noise(source, duration=1)

        print("Say something...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print("API error:", e)

if __name__ == "__main__":
    listen_once()
