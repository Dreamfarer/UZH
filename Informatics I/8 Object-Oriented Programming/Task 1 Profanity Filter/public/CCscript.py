#!/usr/bin/env python3

class ProfanityFilter:

    def __init__(self, keywords: list, template: str):
        self.__banned: list = list(map(lambda x: x.lower(), keywords)).sort(key=lambda el: -len(el))
        self.__replacement: str = template
        self.__repLen: int = len(self.__replacement)

    def filter(self, msg: str) -> str:
        result: str = msg.lower()
        for ban in self.__banned:
            result = result.replace(ban, self.__get_replacement(len(ban)))
        for i in range(len(msg)):
            if msg[i].isupper():
                result = result[:i] + result[i].upper() + result[i + 1:]
        return result

    def __get_replacement(self, length: int) -> str:
        return self.__replacement * (length // self.__repLen) + self.__replacement[:length % self.__repLen]
    
