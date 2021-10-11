from re import search
from fulltextBase import FullTextBase
from fulltextBase import DrvBase 
from fulltextBase import Format
from keywordBase import KeyWordMode

print('Hello World!')

#GUI : PyQt Still has problem , so demo on terminal.

def main():
    drvbase = DrvBase.Chrome
    driver,check = FullTextBase.CreatePage("",drvbase)
    while(True) :
        URL = input("Get URL : ")
        if(URL == "Q") :
            break;
        url = "file:///{}".format(URL)
        driver.get(url)        
        check = url

        #File Format
        fileforemate = Format.JSON
        if(url[-3:] == "xml") :
            fileforemate = Format.XML
        #Search way
        searchmode = KeyWordMode.CONTAINS
        smode = input("SearchMode[F\C] : ")
        if(smode == "F") :
            searchmode = KeyWordMode.FULLMATCH

        TagName = input("Tagname : ")
        KeyWord = input("Keyword : ")
        
        #url = "file:///D:/Master Degree/Lesson/web crawler/HW1/Testing/test6.json"

        if(check == url) :
            Sents,keysents = FullTextBase.GetSentencesBytagsName(driver,TagName,KeyWord,fileforemate,searchmode)
            #Sents,keysents = FullTextBase.GetSentencesBytagsName(driver,"Title","COVID-19",Format.XML)
            #Sents,keysents = FullTextBase.GetSentencesBytagsName(driver,"AbstractText","COVID-19",Format.XML)
            #Sents,keysents = FullTextBase.GetSentencesBytagsName(driver,"tweet_text","in",Format.JSON,KeyWordMode.CONTAINS)
            #Sents,keysents = FullTextBase.GetSentencesBytagsName(driver,"AbstractText","COVID-19",Format.XML)
            print("Match keyword {} [{}/{}] :\n{}\n".format(KeyWord,len(keysents),len(Sents), keysents))
            for sent in keysents :
                words,wordsnum,charnum = FullTextBase.GetSentenceStatices(sent)
                print("{} : {} words {} chars".format(sent,wordsnum,charnum))            
            #for sent in Sents :
                #words,wordsnum,charnum = FullTextBase.GetSentenceStatices(sent)
                #print("{} words {} chars".format(wordsnum,charnum))
        else :
            print("Fail to Create Driver [{}]".format(drvbase))
        print("endjob")
  
if __name__=="__main__":
    main()