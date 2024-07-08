"""Lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code."""

class Person:
    """Person class repr"""

    def __init__(self) -> None:
        self.name = None
        self.age = None
        self.address = None

    def __str__(self) -> str:
        return f'A Person with name {self.name if self.name else "NA"} ' \
                f'with age {self.age if self.age else "NA"} ' \
                f'lives at {self.address if self.address else "NA"}'

class PersonBuilder:
    """person builder class repr"""
    def __init__(self, person=Person()):
        self.person = person

    def setname(self, name):
        """set name method"""
        self.person.name = name
        return self

    def setage(self, age):
        """set age method"""
        self.person.age = age
        return self

    def setaddress(self, address):
        """set address method"""
        self.person.address = address
        return self

    def build(self):
        """returns a person obj"""
        return self.person

if __name__ == '__main__':
    pb = PersonBuilder()
    person = pb.setname("RRR").build()
    print(person)