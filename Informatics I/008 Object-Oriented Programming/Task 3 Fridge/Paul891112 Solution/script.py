#!/usr/bin/env python3

class Fridge:
    
    
    
    def __init__(self):
        self.__items = list() #list of tuples (date, name)
        self.__i=-1
        self.__item_count = 0
        
    def store(self,item):
        self.__items.append(item)
        self.__item_count += 1
        self.__items.sort()
        
    
    
    def __get_item_count(self):
        return self.__item_count
    
    def __iter__(self):
        
        return self
        
    def __next__(self):
        self.__i += 1
        max_count = self.__get_item_count()
        if self.__i < max_count:
            return self.__items[self.__i]
        else:
            raise StopIteration
  
        
    def __len__(self):
        return self.__get_item_count()
    
    def take(self,item):
        for i in self.__items:
            if item == i:
                self.__items.remove(i)
                self.__item_count -= 1
                return item
        #if nothing to take, raise warning
        raise Warning("Cannot take from fridge")
        
    def find(self,name):
        for i in self.__items:
            if name == i[1]:
                return i
        return None
    
    def take_before(self,date):
        throw = list()
        for i in self.__items:
            if date >i[0]:
                throw.append(i)
        for i in throw:
            self.__items.remove(i)
            self.__item_count -= 1
               
        return throw
        
            
        
    
        

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
    
#f.take((191127, "Butter")) # ok
f.take_before(191201)

     
