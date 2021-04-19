class LinkedListNode():
    def __init__(self, Value, NextNode = None, PreviousNode = None):
        self.Value = Value
        self.NextNode = NextNode
        self.PreviousNode = PreviousNode
        
        
class DLinkedList():
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        
    def insert_at_end(self, new_value):
        NewNode = LinkedListNode(new_value)
        NewNode.NextNode = None
        if self.head is None:
            self.head = NewNode
            self.tail = NewNode
            
        else:
            NewNode.PreviousNode = self.tail
            self.tail.NextNode = NewNode
            self.tail = NewNode
            
        
        
    def print_reversed(self):
        fibonacci = self.tail
        while fibonacci is not None:
            print(fibonacci.Value)
            fibonacci = fibonacci.PreviousNode
            


def fibonacci(val, x):
    for j in range(len(val)):
        x.insert_at_end(val[j])
    x.print_reversed()
    print("----------------------------------------------------")

        
x = DLinkedList()
Fibonacci = []
for i  in range(100):
    if i == 0:
        Fibonacci.append(0)
    elif i == 1:
        Fibonacci.append(1)

    else:
        t = Fibonacci[i-2]+Fibonacci[i-1]
        Fibonacci.append(t)
        
        
a = fibonacci(Fibonacci, x)
print(a)
print("hi htdgdzj")


