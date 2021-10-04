from enum import Enum
from selenium import webdriver
from keywordBase import KeyWordBase

#Please Make Sure installed driver
class DrvBase(Enum) :
    Chrome = 0
    FireFox = 1
    Edge = 2
    _IE = 3
    Opera = 4

class FullTextBase : 
    #Create Driver Connection
    def CreatePage(url,drvbase : DrvBase) :
        try :
        #Get Driver
            if(drvbase == DrvBase.Chrome) :
                driver = webdriver.Chrome()
            elif(drvbase == DrvBase.FireFox) :
                driver = webdriver.Firefox()
            elif(drvbase == DrvBase.Edge) :
                driver = webdriver.Edge()
            elif(drvbase == DrvBase._IE) :
                driver = webdriver.Ie()     
            else :
                driver = webdriver.Opera()     
        #Connect Url
            driver.get(url)
        except Exception as ex:
            print("CreatePage GetException => {}".format(ex))
            url = "CreatePage GetException => {}".format(ex) 
        return driver , url
    #Get Sentences From def class name(Only Support Graphic class)
    def GetSentencesByClassName(driver,classname,keyword):
        Sents = []
        keySents = []
        try :
            #Get Spefic Element
            element = driver.find_element_by_class_name(classname)
            #Split Sentences
            Sents = KeyWordBase.SplitSentences(element.text)
            #Choose Sentences By Keyword
            keySents = KeyWordBase.KeywordSectence(Sents,keyword)
        except Exception as ex:
            print("GetSentencesByClassName GetException => {}".format(ex))
        return Sents,keySents

        




#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By

#url = input('Give The URL : ')
#driver = webdriver.Chrome()
#driver.get("file:///D:/Master%20Degree/Lesson/web%20crawler/jof/index.html?format=json")
#driver.get(url)

#try:
    #Wait Web Open
    #WebDriverWait(driver, 20).until(
    #        EC.presence_of_element_located((By.ID, "about"))
    #        )
    #Get Spefic Element
    #element = driver.find_element_by_class_name("full.margin_top_20")
    #Split Sentences
    #list = KeyWordBase.SplitSentences(element.text)
    #Choose Sentences By Keyword
    #list = KeyWordBase.KeywordSectence(list,"tempor")
#except Exception as e:
    #print(e)
    #quit();
#driver.quit()


# 傳入字串
#element.send_keys("Selenium Python")
#element.send_keys(Keys.ENTER)


#button = driver.find_element_by_name("btnK")
#button.click()
