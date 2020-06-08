from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

#----------------------------
# Locating Elements from HTML
#----------------------------

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)



#-----------------------------
# Tutorial 1 and 2
#-----------------------------
'''

driver.get("https://techwithtim.net")
print(driver.title)


# getting the element, entering the search result, and pressing enter
search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

print(driver.page_source)
# print(driver.page_source) #This will print the entire html
try:
    main = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements_by_tag_name("articles")
    for article in articles:
        header = article.find_element_by_class_name("entry_summary")
        print(header.text)
except:
    driver.quit()

# time.sleep(5)   # wait for 5 seconds
# driver.quit()
'''

#---------------------------
# Tutorial 2
#---------------------------

'''
driver.get("https://techwithtim.net")
print(driver.title)


link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()
    # element.clear() clears content in the field
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    # element.back() returns one step backward
    # element.forward() return one step forward
finally:
    driver.quit()
'''

#---------------------------
# Tutorial 3
#---------------------------
'''
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5) # wait for 5 seconds

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie) #it click where ever the mouse is

for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()

'''           
