# importing required libraries and packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import speech_recognition as sr
import numpy as np
import pyttsx3
import pickle
import time

# Total Covid 19 class
class Total_Covid:
    total = 0
    active = 0
    recovered = 0
    death = 0

    # constructor
    def __init__(self, total, death, active, recovered):
        self.total = total
        self.death = death
        self.active = active
        self.recovered = recovered

# function which will scrap the details from the site
def get_data():
    # path for the chromedriver
    PATH = "C:\Program Files (x86)\chromedriver.exe"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, executable_path=PATH)

    # the site from which the details are scraped
    driver.get("https://www.covid19india.org/")

    # scroll the webpage to get the details
    driver.execute_script("window.scrollTo(0, 1000)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 2000)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 3500)")
    time.sleep(2)

    stats = []
    # defining an action chain which can find the botton for total cases
    actions = ActionChains(driver)
    begining = driver.find_element_by_xpath("//button")
    
    # clicking the button for getting the entire covid details
    begining.click()

    # xpath for the small circle element in the svg 
    dots = driver.find_elements_by_xpath("//*[name()='svg']/*[name()='circle' and @stroke = '#28a745']")

    # iterating through the each and every dots in the svg
    for dot in dots:
        hover = ActionChains(driver).move_to_element(dot)
        hover.perform()

        # finding the corresponding details of the active, recovered, death and total cases 
        stat = driver.find_element_by_xpath("//div[@class='stats-bottom' ]//h2")
        active = driver.find_element_by_xpath("//div[@class='stats is-active']//div//h2")
        recovered = driver.find_element_by_xpath("//div[@class='stats is-recovered']//div//h2")
        death  = driver.find_element_by_xpath("//div[@class='stats is-deceased']//div//h2")
        stats.append(Total_Covid(stat.text, death.text, active.text, recovered.text))

    time.sleep(5)
    driver.quit()

    return stats

# function for writing the contents into a file
def file_write(stats):

    file = open('Files\\total_cases.txt', 'w')
    for stat in stats:
        file.write(stat.total+"\n")
    file.close()

    file = open('Files\\active_cases.txt', 'w')
    for stat in stats:
        file.write(stat.active+"\n")
    file.close()

    file = open('Files\\recovered_cases.txt', 'w')
    for stat in stats:
        file.write(stat.recovered+"\n")
    file.close()

    file = open('Files\\death_cases.txt', 'w')
    for stat in stats:
        file.write(stat.death+"\n")
    file.close()


# function for reading the contents from the file
def file_read(file):
    stats = []
    file = open(file, 'r')
    stats = file.readlines()
    file.close()
    return stats

# this function plots the graph details after reading from the files
def graph_ploting(file):

    data = []
    data1 = file_read(file)
    duration = len(data1)

    date = np.linspace(1, duration, duration)

    for i in range(duration):
        data.append(int("".join(data1[i].split(","))[:-1]))


    data = np.array(data)

    X = date
    y = data

    y = np.array([y]).reshape(-1,1)
    X = np.array([X]).reshape(-1,1)
    
    # defining a linear regression model
    lin_reg = LinearRegression()

    # defining polynomial regression model for fitting complex models
    poly_reg = PolynomialFeatures(degree = 5)
    X_poly = poly_reg.fit_transform(X)
    poly_reg.fit(X_poly, y)
    
    lin_reg.fit(X_poly, y)
    

    # Visualising the Polynomial Regression results (for higher resolution and smoother curve)
    X_grid = np.arange(min(X), max(X), 0.1)
    X_grid = X_grid.reshape((len(X_grid), 1))
    plt.scatter(X, y, color = 'red')
    plt.plot(X_grid, lin_reg.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
    plt.title('Covid 19 Statistics')
    plt.xlabel('Number of days')
    plt.ylabel(file[6:-4] + ' confirmed')
    plt.show()

# main function 
if __name__ == "__main__":
    stats = get_data()
    file_write(stats)

