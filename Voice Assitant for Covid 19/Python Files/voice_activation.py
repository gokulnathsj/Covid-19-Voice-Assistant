# importing required libraries and packages
import speech_recognition as sr
import covid_graph as cg
import pickle
import datetime
import calendar 
import pyttsx3
import time
import os

# voice Activation package initialization
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Time 
hour = int(datetime.datetime.now().hour)
minute = int(datetime.datetime.now().minute)
current_time = "Current time in India is " + str(minute) + " minutes past " + str(hour)  


# date Function
def findDay(date): 
    date = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[date]) 

# Speaks out Current Time
def Current_time_India(time, week_day):   
    speak(str(datetime.datetime.now().day) + week_day)
    speak(current_time)

# class for getting current covid details
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
    # defining a recognizer 
    recog = sr.Recognizer()

    # making microphone as the source for audio
    with sr.Microphone() as source:
        print("------------------------------------------------------")
        print("Graphical Mode[command(say): graphical interface]")
        print("Statistical Mode [command(say) : statistical Interface]")
        print("\n Listening....['terminate' for terminating] ")
        print("------------------------------------------------------")
        recog.pause_threshold = 1

        # listening the content 
        audio = recog.listen(source)
    
    try:
        print("---------------------------------")
        print("Recognizing...")

        # converting the audio into text
        query = recog.recognize_google(audio, language='en-in')

        print(f"User said: {query}\n")
        print("---------------------------------")

    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"

    return query

# greet funciton
def greet():
    
    date = " ".join(str(datetime.datetime.now()).split(" ")[0].split("-")[::-1])
    week_day = findDay(date)

    time.sleep(1)

    # calculating the greeting time
    if hour >= 0 and hour < 12:
        speak("Good Morning, I am a covid 19 Voice assistant system.")
    
    elif hour >= 12 and hour <= 17:
        speak("Good Afternoon, I am a covid 19 Voice assistant system.")
    
    else:
        speak("Good Evening, I am a covid 19 Voice assistant system.")

    # current time monitoring
    Current_time_India(current_time, week_day)


# this will give a small description on the voice assitant
def usage():
    speak("I can get the details of the current, active, death reports and the total number of people affected in india")
    speak("for example, the sound can be, what is the active cases in kerala or, it can be how many death cases are there in gujarath")
    speak("U can refer to the help file for understanding my proper usage. please see the console for further details.")


# main function
if __name__ == "__main__":

    greet()
    

    # usage function activation
    know = input("Do you want to get a brief introduction on how to use this properly[y/n] ")
    if know == "y":
        usage()
    

    # upadating covid19.py file
    know = input("Do you want to update the current covid details [y/n] ? ")
    if know == 'y':
        speak("Please remove you hand from the cursor during the updation of the files. It may lead to inaccurate results.")
        os.system("python covid19.py")

    # upadating covid_graph.py file
    know = input("Do you want to update the covid 19 graph details [y/n] ? ")
    if know == 'y':
        speak("Please remove you hand from the cursor during the updation of the files. It may lead to inaccurate results.")
        os.system("python covid_graph.py")
    

    # opening the covid 19 model 
    with open('covid_19_object.pkl', 'rb') as input:
        states = pickle.load(input)

    # for state in states:
    #     print(state.state, state.total, state.active, state.recoverd, state.death)
    state = "statistical"
    country = ['india', 'total', 'cases', 'graph', 'plot', 'country', 'nation', 'number']     

    # the while loop starts
    while True:
        # takes the querry and converts it into lower case
        query = takeCommand().lower()
        word = query.split(" ")
        flag = 0
        
        # statistical interfacing part
        if state == "statistical":
            for i in word:
                for j in range(len(states)):
                    if i in states[j].state.lower().split(" "):
                        if "active" in query:
                            speak("Number of Active cases in " + states[j].state + " is " + str(states[j].active))
                            print("Number of Active cases in " + states[j].state + " is " + str(states[j].active))
                            flag = 1
                            break

                        elif "recovered" in query:
                            speak("Number of recovered cases in " + states[j].state + " is " + str(states[j].recoverd))
                            print("Number of recovered cases in " + states[j].state + " is " + str(states[j].recoverd))
                            flag = 1
                            break
                        
                        elif "death" in query:
                            speak("Total Number of death in " + states[j].state + " is " + str(states[j].death))
                            print("Total Number of death in " + states[j].state + " is " + str(states[j].death))
                            flag = 1
                            break

                        else:
                            speak("Number of Cases in " + states[j].state + " is " + str(states[j].total))
                            print("Number of Cases in " + states[j].state + " is " + str(states[j].total))
                            flag = 1
                    
                if flag == 1:
                    break


        # graphical interfacing section
        if state == "graphical":
            if "active" in query:
                cg.graph_ploting('Files\\active_cases.txt')

            elif "recovered" in query:
                cg.graph_ploting('Files\\recovered_cases.txt')
            
            elif "death" in query:
                cg.graph_ploting('Files\\death_cases.txt')

            elif set(country) & set(word):
                cg.graph_ploting('Files\\total_cases.txt')
                
              
        if "graphical interface" in query:
            speak("Switching to graphical data analysis part")
            state = "graphical"
        elif "statistical interface" in query:
            state = "statistical"
            speak("Switching to statistical data analysis part")

        # terminating section
        if 'terminate' in query:
            speak("terminating voice assistant")
            break
    

        
    

        