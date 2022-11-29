from abc import ABC, abstractmethod

class Person():
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

class Serializer(ABC):

    def serialize(self, p):
        template = self.sentence_template()
        return template % (
            self.format_name(p),
            self.format_age(p),
            self.format_height(p)
        )

    @abstractmethod
    def sentence_template(self):
        pass

    def format_name(self, p):
        return p.name

    def format_age(self, p):
        return p.age

    def format_height(self, p):
        return p.height

class SentenceSerializer(Serializer):

    def sentence_template(self):
        return "%s is %s years old and %s tall"

    def format_height(self, p):
        return f"{p.height}cm"

class CSVSerializer(Serializer):

    def sentence_template(self):
        return '"%s",%s,%s'

class HTMLSerializer(Serializer):

    def sentence_template(self):
        return '<li>%s (%s): %s</li>'

    def format_height(self, p):
        return "%.2fm" % (p.height/100)

p = Person("Ann", 31, 168)

s1 = SentenceSerializer()
print(s1.serialize(p))

s2 = CSVSerializer()
print(s2.serialize(p))

s3 = HTMLSerializer()
print(s3.serialize(p))