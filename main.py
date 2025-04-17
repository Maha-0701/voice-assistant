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
    "hello": "Hello Maha! How can I help you today?",
    "exit": "Goodbye Maha! Shutting down the assistant.",
    "stop": "Okay Maha, stopping now."
}

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_and_respond():
    try:
        with sr.Microphone() as source:
            print("\n🎤 Listening... Speak now!")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                command = recognizer.recognize_google(audio)
                command = command.lower().strip()
                print("🗣️ You said:", command)

                for key in commands:
                    if key in command:
                        response = commands[key]
                        print("🤖 Assistant:", response)
                        speak(response)
                        if key in ["exit", "stop"]:
                            return False
                        break
                else:
                    speak("Sorry, I didn't understand that.")
            except sr.UnknownValueError:
                print("⚠️ Could not understand audio.")
                speak("Sorry, I couldn't understand you.")
            except sr.RequestError as e:
                print("⚠️ Request error:", e)
                speak("Sorry, there was a problem with the speech service.")
    except Exception as e:
        print("⚠️ Microphone error:", e)
        speak("Microphone is not working. Please check your setup.")
    return True

if __name__ == "__main__":
    while True:
        if not listen_and_respond():
            break
