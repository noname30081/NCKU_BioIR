from fulltextBase import FullTextBase
from fulltextBase import DrvBase 

print('Hello World!')

def main():
    drvbase = DrvBase.Chrome
    url = "file:///D:/Master%20Degree/Lesson/web%20crawler/jof/index.html?format=json"
    driver,check = FullTextBase.CreatePage(url,drvbase)
    if(check == url) :
        Sents,keysents = FullTextBase.GetSentencesByClassName(driver,"full.margin_top_20","tempor")
    else :
        print("Fail to Create Driver [{}]".format(drvbase))
    print("endjob")
  
if __name__=="__main__":
    main()