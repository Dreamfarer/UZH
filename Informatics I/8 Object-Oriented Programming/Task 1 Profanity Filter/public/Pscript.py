#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.
class ProfanityFilter:
    
    

    def __init__(self, keywords, template):
        keywords.sort(key=len)
        keywords.reverse()
        self.__keywords = keywords
        self.__template = template
        
        
    def clean(self,word,swearword):
        
        cleaned = ""
        for i,letter in enumerate(swearword):
            cleaned += self.__template[i%len(self.__template)]
        #cleaned = the censored message
        return cleaned
    

    def changeToCleaned(msg, swearword,cleaned):
        msg = msg.lower()
        return msg.replace(swearword,cleaned)
        
 

        

    def filter(self, msg):
        
        words = msg.split() #list of words
        copy = msg
        words.sort(key=len)
        words.reverse()
        for i,word in enumerate(words):
            word = word.lower()
            for j in self.__keywords:
                j = j.lower()
                if j in word:
                    cleaned = ProfanityFilter.clean(self,word,j)
                    copy = ProfanityFilter.changeToCleaned(copy,j,cleaned)
                    
                    
        for i in msg.split():
            if i.lower() in copy:
                copy=copy.replace(i.lower(),i)
        
        return copy 
    
    


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc ducki MastArd HiaJueiLinfe JIl a jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
