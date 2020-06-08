from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.covid19india.org")
print(driver.title)

time.sleep(5)
driver.quit()