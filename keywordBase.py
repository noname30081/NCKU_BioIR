import re

class KeyWordBase:
    lis= [10,10,10]
    def SplitSentences(inStr):
        return re.split(r'(?<!\w\.\w.)(?<!\.\s[a-z])(?<![A-Z][a-z]\.)(?<!Mrs\.)(?<=\.|\?|\!)\s' , inStr)
    def KeywordSectence(inarray, keyword): 
        keysen = []
        for sentence in inarray:
            if(keyword in sentence):
                keysen.append(sentence)
        return keysen;





#Culture
#Cuture = ['Mrs\.']

#Debug
#inStr = "Mrs. Ken bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind! Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."
#list = re.split(r'(?<!\w\.\w.)(?<!\.\s[a-z])(?<![A-Z][a-z]\.)(?<!Mrs\.)(?<=\.|\?|\!)\s' , inStr)
#list2 = re.split(r'(?<!\w\.\w.)(?<!\.\s[a-z])(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s' , inStr)
#print("Get list String {0} Length {1} First Sentences ChrLen[{3}]".format(list,len(list),list[0],len(list[0])))