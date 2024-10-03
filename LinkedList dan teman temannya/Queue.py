class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.last is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def swap(self, position1, position2):
        if position1 < 1 or position2 < 1:
            print("Invalid positions")
            return
        
        if position1 == position2:
            print("Positions are the same")
            return
        
        queue = self.first
        count = 1
        node1 = None
        node2 = None
        while queue:
            if count == position1:
                node1 = queue
            if count == position2:
                node2 = queue
            count += 1
            queue = queue.next

        if node1 and node2:
            temp = node1.value
            node1.value = node2.value
            node2.value = temp
            print("Swapped successfully")
        else:
            print("Invalid positions")
    
    def print_queue(self):
        queue = self.first
        while queue:
            print(queue.value, end=" ")
            queue = queue.next
        print()

    def haspop(self):
        return self.first is not None

    def pop(self):
        if self.haspop():
            popped_value = self.first.value
            self.first = self.first.next
            if self.first is None:
                self.last = None
            return popped_value
        else:
            print("Queue tidak ada nilai")
            return None

# percobaan

my_queue = Queue() 

my_queue.pop() # Cek apa ada pop di queue

my_queue.enqueue(1) # Tambahkan 1 ke queue dan seterusnya
my_queue.enqueue(2) 
my_queue.enqueue(3)
my_queue.enqueue(4)

print("Original Queue:")
my_queue.print_queue()

my_queue.swap(1, 3) #Swap nilai pada index 1 dan 3

print("Queue after swapping:")
my_queue.print_queue()

popped_value = my_queue.pop() #Pop nilai pertama
print("Popped Value:", popped_value)

print("Queue after popping:")
my_queue.print_queue()
