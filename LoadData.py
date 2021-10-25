import  csv

class LoadData:
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
    