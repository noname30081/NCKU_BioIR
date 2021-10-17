import typing
from selenium.webdriver.chrome.webdriver import WebDriver
from fulltextBase import FullTextBase
from fulltextBase import DrvBase 
from fulltextBase import Format
from keywordBase import KeyWordMode
from ArticleCompare import ArticleCompare, Setting
from ArticleCompare import ArticleCompare as artcleC
from ArticleCompare import MapMode
from ArticleCompare import Setting

from selenium import webdriver

from enum import Enum

#Please Make Sure installed driver
class LoadMode(Enum) :
    Local = 0
    Web = 1

class SearchEngine() :
    Driver : WebDriver
    def StartEngine(self) : 
        drvbase = DrvBase.Chrome
        self.Driver,check = FullTextBase.CreatePage("",drvbase)
    def LoadSource(self,url,loadmode : LoadMode) :
        if(loadmode == LoadMode.Local) :
            url = "file:///{}".format(url)
        self.Driver.get(url)
    def ParaGraphInfo(self,tagname,keywords,formate,searchmode = KeyWordMode.FULLMATCH) :
        Sents,keysents,chall = FullTextBase.GetSentencesBytagsName(self.Driver,tagname,keywords,formate,searchmode)
        parawordsum = 0
        for sent in Sents :
            words,wordsnum,charnum = FullTextBase.GetSentenceStatices(sent)
            parawordsum += wordsnum
        return Sents,keysents,parawordsum,chall
    def ParaGraphByTag(self,tagname,formate) :
        paragraph,sents,chall = FullTextBase.GetParagraphBytagsName(self.Driver,tagname,formate)
        return paragraph,sents,chall 
    def CompareArticles(self,Article_A : str , Article_B : str, mapmode : MapMode , settings ) :
        match,result = ArticleCompare.AtMap(artcleC,Article_A,Article_B,mapmode,settings)
        return match,result
    