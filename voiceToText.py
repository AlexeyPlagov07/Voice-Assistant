import pyttsx3
import datetime
import speech_recognition as sr

MASTER = 'Alexey'
print('Initializing...')
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
stop_second_loop = 0
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak('The current time is')
    speak(Time)

def date():
    Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    year = str(datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = str(datetime.datetime.now().day)
    speak('The Current date is')
    speak(Months[month-1])
    speak(date)
    speak(year)

def no():
    global stop_second_loop
    stop_second_loop = 1
command_list = {'time':time, 'date':date, "no":no}
def repeat():

    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as the source for input
    with sr.Microphone() as source:
        print("Please say something:")
        audio = recognizer.listen(source)

        try:
        # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print(text)
            for i in command_list:
                if i in text:
                    command_list[i]()
            if 'no' not in text:
                x = "Anything else?"
            else:
                x = "Bye bye"
        except sr.UnknownValueError:
            x = ("Sorry, I could not understand the audio.")
        except sr.RequestError:
            x = ("Could not request results from Google Web Speech API.")

        speak(x)
        
while True:
    recognizer = sr.Recognizer()

    # Use the microphone as the source for input
    with sr.Microphone() as source:
        print("Please say something(1):")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(text)
        if 'charles' in text.lower():
            speak("How can I help?")
            stop_second_loop = 0
            while stop_second_loop == 0:
                repeat()
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        pass
