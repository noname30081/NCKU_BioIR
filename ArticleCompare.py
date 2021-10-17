from enum import Enum
from enum import IntFlag

class MapMode(Enum) :
    Paragraph = 0
    Sentence = 1
    Word = 2
    char = 3

class Setting(IntFlag) :
    SKIP_SPACE = 0
    SKIP_WORD_UL = 1

class ArticleCompare :
    #the Article_B will compare to the A
    def AtMap(self,Article_A :str,Article_B:str,mapmode : MapMode,setting) :
        match = False
        result = ''
        aa = Setting.SKIP_SPACE | Setting.SKIP_WORD_UL
        if(mapmode == MapMode.Paragraph) :
            match , result = self.ATM_ByParaG(Article_A,Article_B,setting)
        return match,result
    def ATM_ByParaG(Article_A :str,Article_B:str,setting) :
        result = ''
        match = False
        if(setting is None) :  
            match = (Article_B == Article_A)
        else :
            if(setting == Setting.SKIP_SPACE) : 
                Article_A = Article_A.replace(' ','')
                Article_B = Article_B.replace(' ','')
                Article_A = Article_A.replace('\n','')
                Article_B = Article_B.replace('\n','')
            if(setting == Setting.SKIP_WORD_UL) :
                Article_A = Article_A.upper()
                Article_B = Article_B.upper()
            match = (Article_B == Article_A)
        result = 'Articles Match[{}]'.format(match)
        return match,result
        
