"""Lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object."""

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def person_method():
        """Interface method"""

class Person(IPerson):

    def person_method(self):
        print("i am a person")

class ProxyPerson(IPerson):

    def __init__(self) -> None:
        self.person = Person()

    def person_method(self):
        print("i m a proxy person")
        self.person.person_method()

if __name__ == '__main__':
    p = Person()
    p.person_method()

    p1 = ProxyPerson()
    p1.person_method()