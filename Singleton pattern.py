"""Lets you ensure that a class has only one instance, while providing a global access point to this instance."""

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):

    @abstractstaticmethod
    def print_data():
        """implement in child class"""
    

class PersonSingleton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            return PersonSingleton("Default name", 0)
        return PersonSingleton.__instance
    
    def __init__(self, name, age) -> None:
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self
    
    @staticmethod
    def print_data():
        print(f'name is {PersonSingleton.__instance.name} and age is {PersonSingleton.__instance.age} ')

if __name__ == "__main__":
    p1 = PersonSingleton("mj",6)
    print(p1)
    p2 = p1.get_instance()
    print(p2)
    