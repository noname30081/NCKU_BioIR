from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from keywordBase import KeyWordBase


url = input('Give The URL : ')

print(KeyWordBase.lis[0])
driver = webdriver.Chrome()
#driver.get("file:///D:/Master%20Degree/Lesson/web%20crawler/jof/index.html?format=json")
driver.get(url)

# 定位搜尋框
try:
    WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "about"))
            )
    element = driver.find_element_by_class_name("full.margin_top_20")
    #element = WebDriverWait(driver, 10).until(driver.find_element_by_class_name("full margin_top_20"))
    list = KeyWordBase.SplitSentences(element.text)
    #list = element.text.split("[.+ +A-Z]")
    list = KeyWordBase.KeywordSectence(list,"tempor")
    print(list[0]) 
except Exception as e:
    print(e)
    quit();
driver.quit()


# 傳入字串
#element.send_keys("Selenium Python")
#element.send_keys(Keys.ENTER)


#button = driver.find_element_by_name("btnK")
#button.click()
