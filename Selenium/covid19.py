from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import speech_recognition as sr
import pyttsx3
import pickle
import time

class Covid_States:
    state = ""
    total = 0
    active = 0
    recoverd = 0
    death = 0
    
    def __init__(self, district, total, active, recoverd, death):
        self.dis_name = district
        self.dis_total = total
        self.dis_active = active
        self.dis_recoverd = recoverd
        self.dis_death = death
    
    def __init__(self, state, total, active, recoverd, death):
        self.state = state
        self.total = total
        self.active = active
        self.recoverd = recoverd
        self.death = death



if __name__ == "__main__":
    states = []

    PATH = "C:\Program Files (x86)\chromedriver.exe"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, executable_path=PATH)

    # driver = webdriver.Chrome(PATH)
    driver.get("https://covidindia.org/")

    drop_down = driver.find_element_by_name("tablepress-96_length")
    drop_down.click()
    value = driver.find_elements_by_tag_name("option")
    value[2].click()

    affected_places = driver.find_elements_by_class_name("column-1")
    total = driver.find_elements_by_class_name("column-2")
    recoverd = driver.find_elements_by_class_name("column-3")
    death = driver.find_elements_by_class_name("column-4")
    active =  ["active"]

    for i in range(1, len(affected_places) - 1):
        active.append(int(total[i].text) - int(recoverd[i].text) - int(death[i].text))
    
    active.append(sum(active[1:]))

    for i in range(len(affected_places)):
        state = Covid_States((affected_places[i].text).lower(), total[i].text, active[i],
        recoverd[i].text, death[i].text)
        
        states.append(state)

    # for state in states:
    #     print(state.state, state.total, state.active, state.recoverd, state.death)

    states[-1].state = "India"

    time.sleep(8)
    driver.quit()

    with open('covid_19_object.pkl', 'wb') as output:
        pickle.dump(states, output, pickle.HIGHEST_PROTOCOL)

    

   