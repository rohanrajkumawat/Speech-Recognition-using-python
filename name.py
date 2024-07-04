import speech_recognition as sr
import pyttsx3

# Function to convert text to speech
def SpeakNow(command):
    # Initialize the engine
    voice = pyttsx3.init()
    voice.say(command)
    voice.runAndWait()

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the microphone as source for input
with sr.Microphone() as source2:
    # Wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
    print("Silence please")
    recognizer.adjust_for_ambient_noise(source2, duration=2)
    print("Speak now please...")
    
    # Listen for the user's input
    audio2 = recognizer.listen(source2)

    try:
        # Using Google to recognize audio
        Text = recognizer.recognize_google(audio2)
        Text = Text.lower()

        print("Did you say " + Text)
        SpeakNow(Text)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occurred")

