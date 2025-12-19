import speech_recognition as sr
from command_executor import parse_text_to_command, run_command

def listen_and_recognize() -> str | None:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening... speak now.")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print("API error:", e)
        return None

def main():
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
        user = input("[Enter to speak / 'exit' to quit]: ").strip().lower()
        if user == "exit":
            break

        spoken = listen_and_recognize()
        if not spoken:
            continue

        args = parse_text_to_command(spoken)
        if args is None:
            print("I couldn't map that speech to a known command.")
        else:
            run_command(args)

if __name__ == "__main__":
    main()
