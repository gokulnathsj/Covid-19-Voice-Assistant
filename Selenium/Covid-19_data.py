from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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


if __name__ == "__main__":
    states = []


    PATH = "C:\Program Files (x86)\chromedriver.exe"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, executable_path=PATH)

    driver = webdriver.Chrome(PATH)
    driver.get("https://www.covid19india.org")

    affected_places = driver.find_elements_by_class_name("title")
    total_affected = driver.find_elements_by_class_name("total")
    total_area_affected = len(affected_places)

    for i in range(total_area_affected):
        state = Covid_States(affected_places[i].text, total_affected[i*4].text, 
        total_affected[i*4 + 1].text, total_affected[i*4 + 2].text, total_affected[i*4 + 3].text)
        
        states.append(state)

    for state in states:
        print(state.state, state.total, state.active, state.recoverd, state.death)
        
    time.sleep(5)
    driver.quit()