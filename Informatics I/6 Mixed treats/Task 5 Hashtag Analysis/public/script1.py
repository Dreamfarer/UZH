#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.


#useful operations

#create new dict entry or add one to existing one
# if hashtag in all_hashtags.keys():
#     all_hashtags[hashtag] += 1
#     print("add 1")
# else:
#     all_hashtags[hashtag] = 1
#     print("create")





def analyze(posts): #2.75 points, consider ##aa and #ab#ac

    
    all_hashtags={}
    
    for post in posts:
        #post is a string in list of posts
        words = post.split()
        #get words, get rid of spaces
        
        
        for word in words:
            
            #check whether there is hashtag
            if not "#" in word:
                continue
            
            while "#" in word:
                
                
                #ignore if theres only hashtag
                if len(word)==1:
                        word = word[1:]
                        continue
                
                #get index of #
                hashtag_index = word.index("#")
                
                #check whether the char after hashtag is valid
                if not word[hashtag_index+1].isalpha():
                    #not alphabet after #, go to next word
                    word = word[1:]
                    continue
                
                #get the whole hashtag without #
                word = word[hashtag_index+1:]
                
                #word is now all chars after #
                if word.isalnum():
                    
                    #if all trailing chars are valid, get hashtag from word
                    hashtag = word
                    #create hashtag or add one to count
                    if hashtag in all_hashtags.keys():
                        all_hashtags[hashtag] += 1
                        print("add 1")
                    else:
                        all_hashtags[hashtag] = 1
                        print("create")
                    break#out of while loop
                #certain trailing chars are not num or letter        
                else:
                    for char in word:
                        #get the index of end of hashtag, extract substring
                        if not(char.isalnum()):
                            i = word.index(char)
                            hashtag = word[:i]
                            word = word[i:]
                            #hashtag get
                            #create hashtag or add one to count
                            if hashtag in all_hashtags.keys():
                                all_hashtags[hashtag] += 1
                                print("add 1")
                            
                            else:
                                all_hashtags[hashtag] = 1
                                print("create")
                            break
                    
                
                            
      
    return all_hashtags

#---------------------------------------------------------
#attempt 3
    
    # all_hashtags={}
    
    # for post in posts:
    #     words = post.split()
    #     for word in words:
    #         #ignore words without #
    #         if not "#" in word:
    #             continue
            
    #         while "#" in word:
    #             #the word contains hashtag

    #             #get the first index of #, cut off precedent chars
    #             hashtag_index = word.index("#")
    #             word = word[hashtag_index:]
                
    #             #get the finishing index
                
    #             for char in word:
    
    #                 #get the index of end of hashtag, extract substring
    #                 if not(char.isalnum()):
    #                     i = word.index(char)
    #                     hashtag = word[hashtag_index:i+1]
    #                     #cut hashtag off from word 
    #                     word = word[i+1:]
    #                     break#now we have a hashtag and the rest of word
                
    #             #check whether the current hashtag is valid
    #             #ignore if theres only hashtag
    #             if len(hashtag)==1:
    #                 continue
                
    #             #ignore if first char after # is number
    #             if len(hashtag)<2:
    #                 print("Index out of range")
    #                 continue
    #             if hashtag[1].isnumeric():
    #                 continue
                
    #             #now hashtag is surely valid, add to dictionary
    #             hashtag = hashtag[1:]
    #             if hashtag in all_hashtags.keys():
    #                 all_hashtags[hashtag] += 1
    #                 print("add 1")
    #             else:
    #                 all_hashtags[hashtag] = 1
    #                 print("create")
            
    # return all_hashtags 

#------------------------------------------------------------------------           
    
#attempt 2
    
    # for post in posts:
    #     #post is a string in list of posts
    #     words = post.split()
    #     #get words, get rid of spaces
        
        
    #     for word in words:
    #         #point 2
            
    #         #check whether there is hashtag
    #         if not "#" in word:
    #             continue
            
            
            
    #         
            
    #         #if its a normal hashtag:
    #         #word is now all nums or letters after #
            
    #         if word[1:].isalnum():
    #             #Make sure first char after # is not num
    #             if word[1].isnum():
    #                 #not alphabet after #, go to next word
    #                 continue
                
    #             #if all trailing chars are valid, get hashtag from word
    #             hashtag = word[1:]
    #             #create hashtag or add one to count
    #             if hashtag in all_hashtags.keys():
    #                 all_hashtags[hashtag] += 1
    #                 print("add 1")
    #             else:
    #                 all_hashtags[hashtag] = 1
    #                 print("create")
            
            
            
    #         #while there is still # in word:
    #         while "#" in word:
                
                
    #             #get the index of #
                
    #             hashtag_index = word.index("#")
    #             hashtag=""
                
    #             #get the index of end of hashtag - thus a valid hashtag
    #             for char in word:

    #                 #get the index of end of hashtag, extract substring
    #                 if not(char.isalnum()):
    #                     i = word.index(char)
    #                     hashtag = word[hashtag_index:i]
    #                     #cut hashtag off from word 
    #                     word = word[i+1:]
    #                     break#jump to check point 1
                
                
    #             #point 1
    #             #check whether the char after hashtag is valid
    #             print(hashtag)
    #             if not hashtag[1].isalpha():
    #                 #not alphabet after #, go to next word
    #                 break#jumpt to point 2
                
    #             #get the whole hashtag without #
    #             hashtag = hashtag[1:]
                
                
    #             #now hashtag is valid, do create or add
    #             if hashtag in all_hashtags.keys():
    #                 all_hashtags[hashtag] += 1
    #                 print("add 1")
    #             else:
    #                 all_hashtags[hashtag] = 1
    #                 print("create")
                
                
                            
      
    # return all_hashtags
        


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = [
    "hi #weekend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich #",
    ".9#invalidcharsbefore",
    "##doublehash1#doublehash2",
    "#abc0#ec;##ec##"
    "#zurich #tag3<3"]

print(analyze(posts))
