import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    print(f"[jarvis]: {text}")
    engine.say(text)
    engine.runAndWait()
    print(text)


def listen(prompt=None, timeout=5, phrase_time_limit=5):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        if prompt:
            speak(prompt)

        try:
            print("🎙️ Listening...")
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            command = recognizer.recognize_google(audio)
            print(f"[User]: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Network issue. Please check your internet.")
        except Exception as e:
            print(f"Error: {e}")
    return ""


#Brain
def handle_command(command):
    
    if not command:
        return

    if "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open gmail" in command:
        speak("Opening Gmail.")
        webbrowser.open("https://mail.google.com")

    elif "open netflix" in command:
        speak("Opening Netflix.")
        webbrowser.open("https://www.netflix.com")

    elif "play music" in command or "play song " in command:
        speak("what song would u like me to play hindi nepali or english")
        if "hindi" in command :
            speak("playing brown munda")
            webbrowser.open("https://www.youtube.com/watch?v=VNs_cCtdbPc")
        elif "english" in command:
            speak("playing english song")
        elif "nepali" in command:
            speak("playing nepali music")
        else:
            speak("i did not quit catch that")


    elif "who created you" in command:
        speak("i was created by samyak pokharel")

    elif "search google for" in command:
        search_term = command.split("search google for")[-1].strip()
        if search_term:
            speak(f"Searching Google for {search_term}")
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
        else:
            speak("Please tell me what to search for.")

    elif "time" in command or "what is the time" in command or "what time is it" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif "what is your name" in command or "who are you" in command:
        speak("I am Harry, your personal voice assistant.")

    elif "who created you" in command:
        speak("I was created by Samyak.")

    elif "tell me a joke" in command:
        speak("bruhhhhh")

    elif "exit" in command or "quit" in command or "goodbye" in command:
        speak("Goodbye! Talk to you later.")
        exit()

    else:
        speak("Sorry, I don't understand that command.")


if __name__ == "__main__":
    speak("Hello, I am jarvis. Say 'activate' to wake me up.")

    while True:
        wake_word = listen(timeout=3, phrase_time_limit=3)

        if "activate" in wake_word:
            speak("I'm awake. What can I do for you?")
            break

    

    while True:
        user_command = listen(prompt="Listening for your command...", timeout=6, phrase_time_limit=6)
        handle_command(user_command)
