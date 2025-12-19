import pyttsx3
import speech_recognition as sr
from command_executor import parse_text_to_command, run_command

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_and_recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand.")
        return None
    except sr.RequestError:
        print("API error.")
        return None


def main():
    speak("Hi")
    speak(" I am Voice Driven Shell System\n")
    speak("Built by Mariyum\n")
    speak(" WahFah\n")
    speak("\n and Mohmeenah")
    
    print("=== Voice Shell (Level 1) ===")
    print("Commands (speak in English):")
    print("  'list files' / 'show files'")
    print("  'current folder'")
    print("  'clear screen'")
    print("  'show file <name>'")
    print("  'show date'")
    print("  'disk usage'")
    print("  'memory usage'")
    print("  'show processes'")
    print("  'who am I'")
    print("  'cpu information'")
    print("  'kernel version'")
    
    while True:
        user = input("[ENTER to speak] ")
        if user.lower() == "exit":
            break

        spoken = listen_and_recognize()
        if not spoken:
            continue

        args = parse_text_to_command(spoken)
        if args is None:
            print("Unknown command.")
            speak("Sorry, I did not understand the command")
          
        else:
            run_command(args)
            speak("Command executed successfully")


if __name__ == "__main__":
    main()