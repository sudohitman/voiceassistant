# Import the required module for text to speech conversion 
import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


# init function to get an engine instance for the speech synthesis 
engine = pyttsx3.init() 

#get voices from computer
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print(voices[1].id)

# say method on the engine that passing input text to be spoken 
def speak(audio):
    engine.say(audio)
    # run and wait method, it processes the voice commands. 
    engine.runAndWait()



# function to greet user with goodmorning
def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Hitman")
    elif hour>12 and hour<5:
        speak("Good Afternoon Hitman")
    else:
        speak("Good Evening Hitman")
    speak("I am Garsen, Please tell me how may i help you today")

#take input through the microphone of users voice and return string output
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recongnizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        #print(e)

        print("Unable to recognize .. Say that again Please")
        return "None"
    return query





# main function
if __name__ == "__main__" :
    wishme()


    while True:
        query =takecommand().lower()
        #Logic to search something on wikipedia
        if "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)

        # Logic to open websites
        elif "open google" in query:
            speak("opening google")
            webbrowser.open('google.com')
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        # Logic to open music player
        elif "play music" in query:
            music_dir='C:\\Pankaj\\New Folder (2)\\Gajals'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        #Say the current time 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")