from fulltextBase import FullTextBase
from fulltextBase import DrvBase 
from fulltextBase import Format

print('Hello World!')

def main():
    drvbase = DrvBase.Chrome
    url = "file:///D:/Master Degree/Lesson/web crawler/HW1/Testing/test1.xml"
    driver,check = FullTextBase.CreatePage(url,drvbase)
    if(check == url) :
        Sents,keysents = FullTextBase.GetSentencesBytagsName(driver,"Title","COVID-19",Format.XML)
        Sents,keysents = FullTextBase.GetSentencesBytagsName(driver,"AbstractText","COVID-19",Format.XML)
    else :
        print("Fail to Create Driver [{}]".format(drvbase))
    print("endjob")
  
if __name__=="__main__":
    main()