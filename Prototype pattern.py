"""Lets you copy existing objects without making your code dependent on their classes."""

from abc import ABCMeta, abstractstaticmethod
from copy import copy

class IProtoType(metaclass=ABCMeta):
    """interface with clone method"""

    @abstractstaticmethod
    def clone():
        """The clone, deep or shallow, is up to how you
        want implement the details in your concrete class"""
    
class ConcreteClass1(IProtoType):
    """concrete class 1"""

    def __init__(self, i=0, s="", l=[], d={}) -> None:
        self.i = i
        self.s = s
        self.l = l
        self.d = d
    
    def clone(self):
        return type(self)(
            self.i,
            self.s,
            self.l.copy(),
            self.d.copy()
        )
    
    def __str__(self) -> str:
        return f'{id(self)}\ti={self.i}\t\ts={self.s}\tl={self.l}\td={self.d}\n'

class ConcreteClass2(IProtoType):
    """concrete class 1"""

    def __init__(self, i=0, s="", l=[], d={}) -> None:
        self.i = i
        self.s = s
        self.l = l
        self.d = d
    
    def clone(self):
        return type(self)(
            self.i,
            self.s,
            copy.deepcopy(self.l),
            copy.deepcopy(self.d)
        )
    
    def __str__(self) -> str:
        return f'i={self.i}\t\ts={self.s}\tl={self.l}\td={self.d}\t{id(self)}'

if __name__ == '__main__':
    obj2 = ConcreteClass1(1,"obj1",[1,2,3], {1:'one'})
    #obj2 = ConcreteClass2(1,"obj1",[1,2,3], {1:'one'})
    obj1 = obj2.clone()
    print(obj1)
    print(obj2)