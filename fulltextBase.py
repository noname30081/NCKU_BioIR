from enum import Enum
from selenium import webdriver
from keywordBase import KeyWordBase
from keywordBase import KeyWordMode
import xml.etree.ElementTree as xmlapi
from bs4 import BeautifulSoup
import json

#Please Make Sure installed driver
class DrvBase(Enum) :
    Chrome = 0
    FireFox = 1
    Edge = 2
    _IE = 3
    Opera = 4

#Please Make Sure installed driver
class Format(Enum) :
    HTML_BASIC = 0
    XML = 1
    JSON = 2

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
    def GetSentencesBytagsName(driver,tagname,keyword,pageformat : Format,keywordMode : KeyWordMode):
        paragraph = ""
        Sents = []
        keySents = []
        if(pageformat == Format.XML) :
            element = xmlapi.fromstring(driver.page_source)
            try :
                #Get Spefic Element
                for ele in element.iter(tagname) :
                        paragraph += ele.text
                #Split Sentences
                Sent = KeyWordBase.SplitSentences(paragraph)
                for se in Sent :
                        if(se is not None) :
                            if(se[:1] == ' ') :
                                se =  se[1:]                           
                            if(len(se)>2) :
                                Sents.append(se)
                #Choose Sentences By Keyword
                keySents = KeyWordBase.KeywordSectence(Sents,keyword,keywordMode)
            except Exception as ex:
                print("GetSentencesBytagsName GetException => {}".format(ex))
            return Sents,keySents
        elif(pageformat == Format.JSON) : 
            element = BeautifulSoup(driver.page_source)
            try :
                #Get Spefic Element
                pars = json.loads(element.text)
                for par in pars :
                    paragraph = par[tagname]
                    paragraph = paragraph.replace("\n➡️ ","")
                    paragraph = paragraph.replace("\n","")
                    sent = KeyWordBase.SplitSentences(paragraph)
                    for se in sent :
                        if(se is not None) :
                            if(se[:1] == ' ') :
                                se =  se[1:]
                            if(se[:1] == '\"') :
                                se =  se[1:]                                
                            if(len(se)>2) :
                                Sents.append(se)
                #Choose Sentences By Keyword
                keySents = KeyWordBase.KeywordSectence(Sents,keyword,keywordMode)
            except Exception as ex:
                print("GetSentencesByClassName GetException => {}".format(ex))
            return Sents,keySents
    def GetSentenceStatices(inSentce: str) :
        charnum = len(inSentce)
        words = KeyWordBase.SplitWords(inSentce)
        return words,len(words),charnum
