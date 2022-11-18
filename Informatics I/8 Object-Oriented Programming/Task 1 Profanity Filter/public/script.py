#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    def __init__(self, keywords, template):

        self.__keywords = keywords
        self.__template = template

        self.__keywords.sort(key=len, reverse=True) # Sort the keywords accroding to length

    def filter(self, msg):

        # Convert it to lower case only so "Shot" gets also replaced, not only "shot"
        msg_ref = msg.lower()

        # Loop through every filter
        for keyword in self.__keywords:

            # Convert it to lower case only so "Shot" gets also replaced, not only "shot"
            keyword = keyword.lower()

            insert = ""
            index_counter = 0

            # Build the string that should be put in place instead of the swear word.
            while not len(insert) == len(keyword): 
                if index_counter == len(self.__template): index_counter = 0
                insert += self.__template[index_counter]
                index_counter += 1

            # Replace the swear word with the newly created string (without altering the rest of the sentence)
            while not msg_ref.find(keyword) == -1:

                index = msg_ref.find(keyword)

                msg_ref = "".join([msg_ref[:index], insert, msg_ref[index + len(keyword):]])
                msg = "".join([msg[:index], insert, msg[index + len(keyword):]])

        return msg

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi mastard jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
