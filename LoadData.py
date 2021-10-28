import  csv
from keywordBase import KeyWordBase

class LoadData (object):
    def __init__(self) :
        return
    def GetParagraphicByCsvTag(fullpath,tagName):
        paragraphic = '' 
        with open(fullpath,newline='\n',encoding='utf-8') as csvfile :
            rows = csv.DictReader(csvfile)
            for row in rows :
                #print(row)
                paragraphic += row[tagName] + ' '
        return paragraphic
    def GetTags(fullpath):
        tags = []
        with open(fullpath,newline='',encoding='utf-8') as csvfile :
            rows = csv.reader(csvfile)
            for row in rows :
                tags = row
                return tags
    def GetParagraphicsByCsvTag(fullpaths,tagName,length):
        if length > len(fullpaths) :
            length = len(fullpaths)
        paragraphic = '' 
        for i in range(length) :
            with open(fullpaths[i],newline='\n',encoding='utf-8') as csvfile :
                rows = csv.DictReader(csvfile)
                for row in rows :
                    paragraphic += row[tagName] + ' '
        return paragraphic
    def GetRowsByCsvTag(fullpath):
        paragraphic = '' 
        Rows = []
        with open(fullpath,newline='\n',encoding='utf-8') as csvfile :
            rows = csv.reader(csvfile)
            i = 0
            for row in rows :
                if i != 0 :
                    Rows.append(row)
                i += 1
            return Rows
    def ParagraphicByList(listdata):
        WordSort = []
        WordDic = {}
        Index = {}
        i = 0     
        for data in listdata :
            Sent = KeyWordBase.SplitSentences(data)
            for se in Sent :
                if(se is not None) :
                    if(se[:1] == ' ') :
                        se =  se[1:]       
                    if(se == ' ') :
                        continue                   
                    if(len(se)>1) :
                        Words = KeyWordBase.SplitWords(se)
                        for Word in Words :
                            if WordDic.__contains__(Word) :
                                WordDic[Word] += 1
                            else :
                                WordDic.setdefault(Word,1)
                            if Index.__contains__(Word) :
                                if str(i) not in Index[Word] :
                                    Index[Word].append(str(i))
                            else :
                                Index.setdefault(Word,[])
                                Index[Word].append(str(i))
            i += 1
        WordSort = sorted(WordDic.items(),reverse=True, key=lambda x:x[1])
        return WordSort,WordDic,Index