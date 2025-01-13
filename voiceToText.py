import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
import weather
import os
class person:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
person_dict = {}
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
    Time = datetime.datetime.now()
    half = ""
    if Time.hour > 12:
        hour = str(Time.hour - 12)
        half = 'PM'
    else:
        hour = str(Time.hour)
        half = 'AM'
    minute = str(Time.minute)
    speak('The current time is')
    speak(str(hour+" "+minute+" "+half))

def date():
    Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    year = str(datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = str(datetime.datetime.now().day)
    speak('The Current date is')
    speak(Months[month-1])
    speak(date)
    speak(year)


def weather():
    import weather
    import os
    os.system("python weather.py")
    # Make sure the weather data is fetched first
    weather.fetch_weather()

    # Now you can call the return functions
    current_temp = str(weather.return_temp())

    if current_temp[0] == '-':
        current_temp = (' negative '+ str(current_temp[1::]))
    speak("It is "+str(weather.return_current())+"outside")
    speak("With a temperature of"+current_temp+"degrees celsius")
    #print(weather.return_weather())




def no():
    print("stopped")
    global stop_second_loop
    stop_second_loop = 1

def add_to_dict():
    name, phone, email = input("Enter name, phone number, and email: ").split()
    x = name
    name = person(name, phone, email)
    person_dict[x] = name
    print(person_dict)
def wishme():
   speak("Welcome back sir!")
   speak("Charles at your service. Please tell me how can i help you?")

def sendEmail():
    print(person_dict)
    recognizer = sr.Recognizer()
    text1 = None
    # Use the microphone as the source for input
    while text1 == None:
        with sr.Microphone() as source:
            speak("Who do you want to email?")
            audio = recognizer.listen(source)

            try:
            # Recognize speech using Google Web Speech API
                text1 = recognizer.recognize_google(audio)
                print(text1)
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass
    if text1 in person_dict:
        content = None
        while content == None:
            with sr.Microphone() as source:
                speak("What do you want to email?")
            
                audio = recognizer.listen(source)
        
                try:
                # Recognize speech using Google Web Speech API
                    content = recognizer.recognize_google(audio)
                    print(content)
                    speak("Emailing")
                    speak(content)
                    speak("to")
                    speak(text1)
                except sr.UnknownValueError:
                    pass
                except sr.RequestError:
                    pass
    
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('alexeyplagov@gmail.com', 'snjq yyae bjlf jvgn')
        server.sendmail('alexeyplagov@gmail.com', person_dict[text1].email, content)
        server.close()
    else:
        speak("Type the details in the console.")
        add_to_dict()
        sendEmail()
command_list = {'time':time, 'date':date, "day":date, " no ":no, "email":sendEmail, "weather":weather}
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
            if 'no' not in text.split():
                x = "Anything else?"
            else:
                global stop_second_loop
                stop_second_loop = 1
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
            wishme()
            stop_second_loop = 0
            while stop_second_loop == 0:
                repeat()
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        pass
