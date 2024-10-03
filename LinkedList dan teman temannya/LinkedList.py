class Node:
    def __init__(self, value: str = None):
        self.value = value
        self.next = None
        self.prev = None

    def setNext(self, next: 'Node'):
        self.next = next

    def setPrev(self, prev: 'Node'):
        self.prev = prev

    def getNext(self) -> 'Node':
        return self.next

    def getPrev(self) -> 'Node':
        return self.prev

    def getValue(self) -> str:
        return self.value


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, value: str):
        newNode = Node(value)
        if self.first is None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.setNext(newNode)
            newNode.setPrev(self.last)
            self.last = newNode

    def insert(self, value: str, index: int):
        if index < 0 or index > self.size():
            raise Exception('Invalid index')
        newNode = Node(value)
        if index == 0:
            newNode.setNext(self.first)
            if self.first is not None:
                self.first.setPrev(newNode)
            self.first = newNode
            if self.last is None:
                self.last = newNode
        else:
            current = self.first
            for i in range(index - 1):
                current = current.getNext()
            newNode.setNext(current.getNext())
            if current.getNext() is not None:
                current.getNext().setPrev(newNode)
            current.setNext(newNode)
            newNode.setPrev(current)
            if index == self.size():
                self.last = newNode

    def remove(self, index: int):
        if index < 0 or index >= self.size():
            raise Exception('Invalid index')
        if index == 0:
            self.first = self.first.getNext()
            if self.first is not None:
                self.first.setPrev(None)
            if index == self.size() - 1:
                self.last = self.first
        else:
            current = self.first
            for i in range(index - 1):
                current = current.getNext()
            if index == self.size() - 1:
                self.last = current
                current.setNext(None)
            else:
                current.setNext(current.getNext().getNext())
                if current.getNext() is not None:
                    current.getNext().setPrev(current)

    def swap(self, index1: int, index2: int):
        if index1 < 0 or index1 >= self.size() or index2 < 0 or index2 >= self.size():
            raise Exception('Invalid index')
        if index1 == index2:
            return
        current1 = self.first
        current2 = self.first
        for i in range(index1):
            current1 = current1.getNext()
        for i in range(index2):
            current2 = current2.getNext()

        # Menukar Value
        temp = current1.value
        current1.value = current2.value
        current2.value = temp

    def get(self, index: int) -> str:
        if index < 0 or index >= self.size():
            raise Exception('Invalid index')
        current = self.first
        for i in range(index):
            current = current.getNext()
        return current.getValue()

    def size(self) -> int:
        current = self.first
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def print(self):
        current = self.first
        while current is not None:
            print(current.value, end='')
            current = current.getNext()
        print()


linkedlist = LinkedList()
linkedlist.add('A')
linkedlist.add('B')
linkedlist.add('C')
print("Output: ", end='')
linkedlist.print()  # Output: ABC
linkedlist.insert('D', 1)
print("Output: ", end='')
linkedlist.print()  # Output: ADBC
linkedlist.remove(2)
print("Output: ", end='')
linkedlist.print()  # Output: ADC
print("Get index 1: ", linkedlist.get(1))  # Output: D
linkedlist.swap(0, 1)
print("Output: ", end='')
linkedlist.print() # Output: DAC
