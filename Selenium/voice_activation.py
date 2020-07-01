import speech_recognition as sr
import pickle
import pyttsx3
import time
import os

# voice Activation
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

class Covid_States:
    state = ""
    total = 0
    active = 0
    recoverd = 0
    death = 0
    
    def __init__(self, state, total, active, recoverd, death):
        self.state = state
        self.total = total
        self.active = active
        self.recoverd = recoverd
        self.death = death

# speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# converts the speech to text
def takeCommand():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....[Say 'Quit' for terminating] ")
        recog.pause_threshold = 1
        audio = recog.listen(source)
    
    try:
        print("Recognizing...")
        query = recog.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"

    return query

def greet():
    speak("Hello Sir, I am a covid 19 Voice assistant system.")
    speak("You have to run the covid 19 dot p y file to update the variables with the present number of count")
    speak("you may not need to run it everytime.")
    speak("please see the console.")

def usage():
    speak("Sir, I can get the details of the current, active, death reports and the total number of people affected in india")
    speak("please include these keywords if you want to know about the same")
    speak("for example, the message can be, what is the active cases in kerala or, it can be how many death cases are there in gujarath")

if __name__ == "__main__":

    # greet()
    
    know = input("Do you want to use the voice assistant. It will give a brief introduction on how to use it properly[y/n] ")
    if know == "y":
        usage()
    
    know = input("Do you want to update the current covid details [y/n] ? ")
    if know == 'y':
        os.system("python covid19.py")
    
    with open('covid_19_object.pkl', 'rb') as input:
        states = pickle.load(input)

    # for state in states:
    #     print(state.state, state.total, state.active, state.recoverd, state.death)

    while True:
        query = takeCommand().lower()
        word = query.split(" ")
        flag = 0

        
        for i in word:
            for j in range(len(states)):
                if i == states[j].state.lower():
                    if "active" in query:
                        speak("Number of Active cases in " + states[j].state + " is " + str(states[j].active))
                        flag = 1
                        break

                    elif "recovered" in query:
                        speak("Number of recovered cases in " + states[j].state + " is " + str(states[j].recoverd))
                        flag = 1
                        break
                    
                    elif "death" in query:
                        speak("Total Number of death in " + states[j].state + " is " + str(states[j].death))
                        flag = 1
                        break

                    else:
                        speak("Number of Cases in " + states[j].state + " is " + str(states[j].total))
                    
            if flag == 1:
                break

        if "quit" in query:
            speak("Terminating..")
            break
    

        