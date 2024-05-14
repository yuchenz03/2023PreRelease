#This class builds a circular queue
class circularQueue:
    def __init__(self,mymax):
        self.mymax = mymax #mymax is a user entered value that specifies the length of the queue
        self.arr = self.mymax * [None] #this line creates an empty queue of length mymax
        self.head = 0 #The head pointer points at the first value of the queue (which can increase as values are dequeued)
        self.tail = 0 #The tail pointer points at the last value of the queue (which will increase as values are enqueued)
    
    def dequeue(self): #This method dequeues a value from the start of the queue.
        if self.__isEmpty:
            print("Cannot dequeue: queue empty.")
        else:
            self.head = (self.head + 1) % self.mymax
    
    def enqueue(self, val): #This method enqueues a value onto the end of the queue.
        self.val = val
        if self.__isFull:
            print("Cannot enqueue: queue full.")
        else:
            self.arr[self.tail] = self.val
            self.tail = (self.tail + 1) % self.mymax
        
    
    def __isFull(self): #This method checks if the queue is full
        if self.head > self.tail: #If the head pointer's value is greater than the tail pointer's, this means the head pointer has "wrapped" 
                                  #around. In this case, if tail is one less than head, then tail the queue is full.
            if self.tail+1 == self.head: 
                return True
            else:
                return False
        else: #However, if the head pointer hasn't "wrapped" around yet, where the tail > head, then the queue is only full when head = 0 
              #and tail = max length-1
            if self.head == 0 and self.tail == self.mymax-1:
                return True
            else:
                return False
    
    def __isEmpty(self): #This method checks if the queue is empty.
        if self.head == self.tail:
            return True
        else:
            return False
