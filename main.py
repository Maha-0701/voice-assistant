import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Commands dictionary (you can expand this)
commands = {
    "play music": "Playing your favorite music.",
    "turn on the light": "Turning on the light.",
    "what time is it": "I'm not a clock, but it's always coding time!",
    "hello": "Hello Maha! How can I help you today?"
}

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_and_respond():
    with sr.Microphone() as source:
        print("\n🎤 Listening... Speak now!")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("🗣️ You said:", command)

            for key in commands:
                if key in command.lower():
                    response = commands[key]
                    print("🤖 Assistant:", response)
                    speak(response)
                    break
            else:
                speak("Sorry, I didn't understand that.")
        except sr.UnknownValueError:
            print("⚠️ Could not understand audio.")
            speak("Sorry, I couldn't understand you.")
        except sr.RequestError as e:
            print("⚠️ Request error:", e)
            speak("Sorry, there was a problem with the speech service.")

if __name__ == "__main__":
    while True:
        listen_and_respond()
