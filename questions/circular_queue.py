"""
Problem: Circular Queue Implementation

Description:
Design and implement a data structure for a circular queue. The circular queue is a linear data structure in which operations are performed based on the FIFO (First In First Out) principle. The last position is connected back to the first position to form a circle, hence the name "circular queue" or "ring buffer". Unlike a regular queue, in a circular queue, when the queue becomes full, if there is space at the beginning of the queue, it can be utilized for new entries.

The class should support the following operations:
- MyCircularQueue(k): Initializes the circular queue with a given size 'k'.
- Front(): Retrieves the front item from the queue. Return -1 if the queue is empty.
- Rear(): Retrieves the last item from the queue. Return -1 if the queue is empty.
- enQueue(value): Inserts a value into the circular queue. Return True if successful, otherwise False.
- deQueue(): Deletes an item from the circular queue. Return True if successful, otherwise False.
- isEmpty(): Checks if the circular queue is empty. Return True if it is, otherwise False.
- isFull(): Checks if the circular queue is full. Return True if it is, otherwise False.

You must implement this without using the built-in queue data structures in your programming language.

Function Signatures:
class MyCircularQueue:

    def __init__(self, k: int):
        pass
    
    def Front(self) -> int:
        pass
    
    def Rear(self) -> int:
        pass
    
    def enQueue(self, value: int) -> bool:
        pass
    
    def deQueue(self) -> bool:
        pass
    
    def isEmpty(self) -> bool:
        pass
    
    def isFull(self) -> bool:
        pass

Examples:

1. 
    myCircularQueue = MyCircularQueue(3)
    myCircularQueue.enQueue(1)    # Returns True
    myCircularQueue.enQueue(2)    # Returns True
    myCircularQueue.enQueue(3)    # Returns True
    myCircularQueue.enQueue(4)    # Returns False (since the queue is full)
    myCircularQueue.Rear()        # Returns 3
    myCircularQueue.isFull()      # Returns True
    myCircularQueue.deQueue()     # Returns True
    myCircularQueue.enQueue(4)    # Returns True
    myCircularQueue.Rear()        # Returns 4

Notes:
    - Make use of a list or an array to store elements.
    - Maintain two pointers, one for the front and one for the rear to effectively and efficiently implement the queue operations.

Tags:
    - Queue
    - Data Structures
"""
class MyCircularQueue:

    def __init__(self, k: int):
        self.length = k
        self.queue = [0]*5
        self.front = self.rear = -1
    
    
    
    def Front(self) -> int:
        if (self.front == -1):
            return self.front
        else:
            return self.queue[self.front]
    
    def Rear(self) -> int:
        if (self.front == -1):
            return self.front
        else:
            return self.queue[self.rear]
        
    
    def enQueue(self, value: int) -> bool:
        #disclaimer:I learnt about the divide by length of the array trick from stack exchange explaining how to create circular lists
        if ((self.rear + 1) % self.length == self.front):
            return False
            
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
            return True
        else:
            self.rear = (self.rear + 1) % self.length
            self.queue[self.rear] = value
            return True
    
    def deQueue(self) -> bool:
        if (self.front == -1): 
            return False
        elif (self.front == self.rear):
            
            self.front = -1
            self.rear = -1
            return True
        else:
            self.front = (self.front + 1) % self.length
            return True
            
    
    def isEmpty(self) -> bool:
        if (self.front == -1):
            return True
        else:
            return False
    
    def isFull(self) -> bool:
        if ((self.rear + 1) % self.length == self.front):
            return True
        else:
            return False
