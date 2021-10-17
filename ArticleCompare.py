from enum import Enum
from enum import IntFlag
import re

class MapMode(Enum) :
    Paragraph = 0
    Sentence = 1
    Ward = 2
    char = 3

class Setting(IntFlag) :
    SKIP_SPACE = 1
    SKIP_WORD_UL = 2

class ArticleCompare :
    #the Article_B will compare to the A
    def AtMap(self,Article_A :str,Article_B:str,mapmode : MapMode,setting) :
        match = False
        result = ''
        aa = Setting.SKIP_SPACE | Setting.SKIP_WORD_UL
        if(mapmode == MapMode.Paragraph) :
            match , result = self.ATM_ByParaG(Article_A,Article_B,setting)
        elif(mapmode == MapMode.char) : 
            match , result = self.ATM_ByChars(Article_A,Article_B,setting)
        return match,result
    #直接文章做等號
    def ATM_ByParaG(Article_A :str,Article_B:str,setting) :
        result = ''
        match = False
        if(setting is None) :  
            match = (Article_B == Article_A)
        else :
            if(Setting.SKIP_SPACE in setting) : 
                Article_A = Article_A.replace(' ','')
                Article_B = Article_B.replace(' ','')
                Article_A = Article_A.replace('\n','')
                Article_B = Article_B.replace('\n','')
            if(Setting.SKIP_WORD_UL in setting) :
                Article_A = Article_A.upper()
                Article_B = Article_B.upper()
            match = (Article_B == Article_A)
        result = 'Articles Match[{}]'.format(match)
        return match,result
    #逐字元比對
    def ATM_ByChars(Article_A :str,Article_B:str,setting) :
        result = ""
        match = False
        Acharlen = len(Article_A)
        Bcharlen = len(Article_B)
        Matchlen = 0
        if(setting is None) :
            match = Acharlen == Bcharlen
            #挑較短文章為搜索長度 避免溢位
            serchlen = min(Acharlen,Bcharlen)
            for i in range(0,serchlen) : 
                if(Article_A[i:i+1] == Article_B[i:i+1]) :
                    Matchlen += 1
                    a = Article_B[i:i+1]
                    result += Article_B[i:i+1]
                else : 
                    match = False
                    result += '<span style="background-color:pink;color:black">{}</span>'.format(Article_B[i:i+1])
            if(Bcharlen > Acharlen) :
                result = '{}<span style="background-color:pink;color:black">{}</span>'.format(result,Article_B[serchlen-1:])
            overflow = Bcharlen - Acharlen
            persnt = Matchlen/serchlen
            if(overflow < 0) : overflow = 0
            result = 'Match[{}] Match Persent[{}%] OverFlow[{}] <br>\
                Article Compare Result.<br>\
            {}'.format(match,persnt*100,overflow,result)
        else : 
            match = Acharlen == Bcharlen
            #挑較短文章為搜索長度 避免溢位
            serchlen = max(Acharlen,Bcharlen)
            shiftA = 0
            shiftB = 0
            for i in range(0,serchlen) :
                if(Article_A[i+shiftA:i+shiftA+1] == Article_B[i+shiftB:i+shiftB+1]) :
                    Matchlen += 1
                    a = Article_B[i+shiftB:i+shiftB+1]
                    result += Article_B[i+shiftB:i+shiftB+1]
                else : 
                    if(Setting.SKIP_SPACE in setting) :
                        check = (Article_A[i+shiftA:i+shiftA+1] + Article_B[i+shiftB:i+shiftB+1])
                        while(len(re.findall(r'(\s|\t|\n)',Article_A[i+shiftA:i+shiftA+1])) > 0) :
                            shiftA += 1
                        while(len(re.findall(r'(\s|\t|\n)',Article_B[i+shiftB:i+shiftB+1])) > 0) :                           
                            result += Article_B[i+shiftB:i+shiftB+1]
                            shiftB += 1
                            Matchlen += 1
                        if(Article_A[i+shiftA:i+shiftA+1] == Article_B[i+shiftB:i+shiftB+1]) :
                            Matchlen += 1
                            a = Article_B[i+shiftB:i+shiftB+1]
                            result += Article_B[i+shiftB:i+shiftB+1]
                            continue
                    if(Setting.SKIP_WORD_UL in setting) : 
                        if(Article_A[i+shiftA:i+shiftA+1].upper() == Article_B[i+shiftB:i+shiftB+1].upper()) :
                            Matchlen += 1
                            a = Article_B[i+shiftB:i+shiftB+1]
                            result += Article_B[i+shiftB:i+shiftB+1]
                            continue
                    match = False
                    result += '<span style="background-color:pink;color:black">{}</span>'.format(Article_B[i+shiftB:i+shiftB+1])
            if(Bcharlen > Acharlen and len(result) < Bcharlen) :
                result = '{}<span style="background-color:pink;color:black">{}</span>'.format(result,Article_B[serchlen-1:])
            overflow = Bcharlen - Acharlen
            persnt = Matchlen/serchlen
            if(persnt > 1) : persnt = 1
            if(overflow < 0) : overflow = 0
            match = persnt >= 1
            result = 'Match[{}] Match Persent[{}%] OverFlow[{}] <br>\
                Article Compare Result.<br>\
            {}'.format(match,persnt*100,overflow,result)                
        return match,result
        
