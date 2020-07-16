#####################################################
# !!! This project uses Google chrome for web 
# Scraping purposes.
# This python file will collect current covid 19 data
# It Uses Selenium as the web scraping tool
# Please Install Selenium for running this module
# Please install pickle which is used to save the 
# covid 19 object so that it can be used later 
# !!!! please download chrome driver and put it inside
# "C:\Program Files (x86)\chromedriver.exe" in windows
# or else please change the PATH variable according
# to the path of the chromedriver.exe file
# please check the current google chrome version 
# and download the corresponding chromedriver 
# accordingly
#####################################################


# importing required libraries and packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pickle
import time


# covid 19 class
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
    
    # constructor
    def __init__(self, state, total, active, recoverd, death):
        self.state = state
        self.total = total
        self.active = active
        self.recoverd = recoverd
        self.death = death

################################################
'''
main function, this function is used to 
collect the current data from the website.
The data will be stored inside a python object 
which could be used later.
'''
#################################################


# main function
if __name__ == "__main__":
    states = []

    # Path of the application chromedriver
    PATH = "C:\Program Files (x86)\chromedriver.exe"

    # initializing the driver for web scraping 
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, executable_path=PATH)

    # driver = webdriver.Chrome(PATH)
    driver.get("https://covidindia.org/")


    # getting the element by locating its name
    drop_down = driver.find_element_by_name("tablepress-96_length")

    # click event
    drop_down.click()

    value = driver.find_elements_by_tag_name("option")
    value[2].click()

    # scraping elements by class name
    affected_places = driver.find_elements_by_class_name("column-1")
    total = driver.find_elements_by_class_name("column-2")
    recoverd = driver.find_elements_by_class_name("column-3")
    death = driver.find_elements_by_class_name("column-4")
    active =  ["active"]


    # calculating the active cases
    for i in range(1, len(affected_places) - 1):
        active.append(int(total[i].text) - int(recoverd[i].text) - int(death[i].text))
    
    active.append(sum(active[1:]))

    # appending everything to the covid object
    for i in range(len(affected_places)):
        state = Covid_States((affected_places[i].text).lower(), total[i].text, active[i],
        recoverd[i].text, death[i].text)
        
        states.append(state)

    states[-1].state = "India"

    time.sleep(8)
    driver.quit()

    # saving covid 19 object for future reference
    with open('covid_19_object.pkl', 'wb') as output:
        pickle.dump(states, output, pickle.HIGHEST_PROTOCOL)

    

   