class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_last(self, newNode) -> None:
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            
            lastNode.next = newNode
    
    def insert_head(self, newNode) -> None:
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode
    
    def insert_at(self, newNode, pointer) -> None:
        pass
    
    def print(self):
        if self.head is None:
            print('List is empty')
            return
        currentNode =  self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

if __name__ == '__main__':
    firstNode = Node('John')
    linkedList = LinkedList()
    linkedList.insert_last(firstNode)
    secondNode = Node('Ben')
    linkedList.insert_last(secondNode)
    thirdNode = Node('Mathew')
    linkedList.insert_last(thirdNode)
    linkedList.print()
    fourthNode = Node('peter')
    linkedList.insert_head(fourthNode)
    linkedList.print()