#!/usr/bin/env python3

class Fridge:

    def __init__(self):
        self.__items = []
        self.__item_index = -1

    def __len__(self):
        return len(self.__items)

    def __iter__(self):
        return self

    def __next__(self):
        self.__item_index += 1
        if self.__item_index < len(self.__items):
            return self.__items[self.__item_index]
        self.__item_index = -1
        raise StopIteration

    # function to store items
    def store(self, item):
        self.__items.append(item)
        self.__items.sort()

    def take(self, item):
        if item in self.__items:
            self.__items.remove(item)
            return item
        else:
            raise Warning("No matching item in the Fridge")

    def find(self, name):
        for item in self.__items:
            if name == item[1]:
                return item
        return None

    def take_before(self, date):
        lst = list()
        for item in self.__items:
            if item[0] >= date:
                break
            lst.append(item)
            self.take(item)
        return lst


f = Fridge()

f.store((191127, "Butter"))
f.store((191117, "Milk"))

# it = iter(f)
# print(it)
# print(next(it))
# print(next(it))

print("Items in the fridge:")
for i in f:
    print("- {} ({})".format(i[1], i[0]))

# f.take((191127, "Butter")) # ok
f.take_before(191201)





