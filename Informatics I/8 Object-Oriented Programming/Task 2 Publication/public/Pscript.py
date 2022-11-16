#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class Publication:

    def __init__(self, authors, title, year):
        self.__authors = authors
        self.__title = title
        self.__year = year
        
    def get_authors(self):
        copy = []
        for i in self.__authors:
            copy.append(i)
        return copy
    
    def get_title(self):
        return self.__title
    
    def get_year(self):
        return self.__year

    
    def __repr__(self):
        author_list = "["
        for i,author in enumerate(self.get_authors()):
            author_list += f"\"{author}\""
            if i<len(self.get_authors())-1:
                author_list += ", "
        author_list += "]"        
        repr_title = f"\"{self.get_title()}\""
        repr_year = f"{self.get_year()}"
        return "Publication(" + author_list + ", " + repr_title + ", " + repr_year +")" #assert return true
    
    
    def __str__(self):
        author_list = "["
        for i,author in enumerate(self.get_authors()):
            author_list += f"\"{author}\""
            if i<len(self.get_authors())-1:
                author_list += ", "
        author_list += "]"        
        repr_title = f"\"{self.get_title()}\""
        repr_year = f"{self.get_year()}"
        return "Publication(" + author_list + ", " + repr_title + ", " + repr_year +")" 
        #copy paste from repr
        
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            if self.get_authors()==other.get_authors() and self.get_title() == other.get_title() and self.get_year() == other.get_year():    
                return True
            else: return False
        else:
            return NotImplemented
        #==returns true and false as given
        
    def __hash__(self):
        i = 0
        for aut in self.get_authors():
            i+=hash(aut)
            
        return i*hash(self.get_title()) +hash(self.get_year())
    
    #>
    def __lt__(self,other):
        if isinstance(self, other.__class__):
            if self.get_authors()==other.get_authors():
                if self.get_title()==other.get_title():
                    return self.get_year()>other.get_year()
                else:
                    return self.get_title()>other.get_title()
            else: 
                return self.get_authors()>other.get_authors()
        else:
            return NotImplemented
        
    #>=
    def __le__(self,other):
        if isinstance(self, other.__class__):
            if self.get_authors()==other.get_authors():
                if self.get_title()==other.get_title():
                    return self.get_year()>=other.get_year()
                else:
                    return self.get_title()>=other.get_title()
            else: return self.get_authors()>=other.get_authors()
        else:
            return NotImplemented
        
    #<
    def __lt__(self,other):
        if isinstance(self, other.__class__):
            if self.get_authors()==other.get_authors():
                if self.get_title()==other.get_title():
                    return self.get_year()<other.get_year()
                else:
                    return self.get_title()<other.get_title()
            else: return self.get_authors()<other.get_authors()
        else:
            return NotImplemented
        
    #<=
    def __le__(self,other):
        if isinstance(self, other.__class__):
            if self.get_authors()==other.get_authors():
                if self.get_title()==other.get_title():
                    return self.get_year()<=other.get_year()
                else:
                    return self.get_title()<=other.get_title()
            else: return self.get_authors()<=other.get_authors()
        else:
            return NotImplemented
        
        
    
    
    
    

    # To implement the required functionality, you will also have to implement several
    # of the special functions that typically include a double underscore.


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    print(p)
    print(str(p) == s)#True

    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["A","C"], "C", 2345)
    p4 = Publication(["A","CE"],"D",2010)
    print(p1 == p2)  # True
    print(p2 == p3)  # False
    print(hash(p1)==hash(p2)) #True
    print(hash(p1)==hash(p3)) #False

    sales = {
        p1: 273,
        p2: 398,
    }
    print(p2>p3)#False
    print(p1<p3)#True
    print(p1<p4)#True
    list1 = [p3,p2,p4,p1]
    print(sorted(list1))

    
