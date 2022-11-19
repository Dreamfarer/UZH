#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    def __init__(self, keywords, template):
        self.__keywords = keywords
        self.__template = template

    # Private Function that creates a correct replacement for the swearword given the template
    def __clean(self, swear_word, msg):

        self.substring = self.__template[:len(swear_word) % len(self.__template)]
        self.long_string = self.__template * (len(swear_word) // len(self.__template))
        return self.long_string + self.substring

    # Function that returns a filtered message with a given keywords and message
    def filter(self, msg):
        self.__keywords.sort(key=len, reverse=True)
        lower_msg = msg.lower()

        for swear_word in self.__keywords:
            swear_word = swear_word.lower()

            while swear_word in lower_msg:

                index_swear_word = lower_msg.index(swear_word)

                # Accesses the __clean function to get the correct replacement string
                replacement_string = ProfanityFilter.__clean(self, swear_word, msg)

                # replaces the swear word with the replacement stinrg
                msg = msg[:index_swear_word] + replacement_string + msg[index_swear_word + len(swear_word):]

                # adds new filtered msg to lower_msg, so it can loop through it as long as there still is a swear word
                lower_msg = msg

        return msg





# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abcshoteas defghi Mastard jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno


