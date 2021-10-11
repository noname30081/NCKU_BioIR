import re
from enum import Enum

class KeyWordMode(Enum) :
    CONTAINS = 0
    FULLMATCH = 1

class KeyWordBase:
    lis= [10,10,10]
    def SplitSentences(inStr):
        #return re.split(r'(?<![A-Z]\.[A-Z].)(?<![A-Z]\.[a-z].)(?<![a-z]\.[a-z].)(?!…\s)(?<=(\w|\))(\.|\!|\?))(?:[^0-9])' , inStr)
        return re.split(r'(?<![A-Z]\.[A-Z].)(?<![A-Z]\.[a-z].)(?<![a-z]\.[a-z].)(?![+-]?([0-9]*[.])?[0-9]+)(?!…\s)(?<=(\w|\))(\.|\!|\?))' , inStr)
    def KeywordSectence(inarray, keyword : str , searchmode : KeyWordMode): 
        keysen = []
        keyword_Fword = keyword[:1].upper()+keyword[1:].lower()
        if(searchmode == KeyWordMode.CONTAINS) :
            for sentence in inarray:
                if(keyword in sentence):
                    keysen.append(sentence)
                elif(keyword_Fword in sentence) :
                    keysen.append(sentence)
        elif(searchmode == KeyWordMode.FULLMATCH) :
            for sentence in inarray:
                #match = re.findall(r"(\W({0}|{1})\W)|^(({0}|{1})\W)".format(keyword,keyword_Fword), sentence)
                match = re.findall(r"\W({}|{})\W".format(keyword,keyword_Fword), sentence)
                if(len(match) > 0) : 
                   keysen.append(sentence) 
        return keysen;
    def SplitWords(inStr):
        rgx = re.compile("([\w][\w'-]*\w)")   
        words = rgx.findall(inStr)
        wordsOut = []
        rgx = re.compile("([^0-9])")
        for word in words :
            if (len(rgx.findall(word)) > 0) :
                wordsOut.append(word)
        return wordsOut
    def SplitSGelement(inStr):
        rgx = re.compile("([\w][\w'-]*\w)")
        return rgx.findall(inStr)
    






#Culture
#Cuture = ['Mrs\.']

#Debug
#inStr = "Mrs. Ken bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind! Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."
#list = re.split(r'(?<!\w\.\w.)(?<!\.\s[a-z])(?<![A-Z][a-z]\.)(?<!Mrs\.)(?<=\.|\?|\!)\s' , inStr)
#list2 = re.split(r'(?<!\w\.\w.)(?<!\.\s[a-z])(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s' , inStr)
#print("Get list String {0} Length {1} First Sentences ChrLen[{3}]".format(list,len(list),list[0],len(list[0])))