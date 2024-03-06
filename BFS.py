'''
Place first node in queue

LOOP until queue is empty (while queue:)
    If current node not in explored
        Place node in explored
    For node's neighbours:
        if not in explored, add to queue
    Dequeue the current node

'''

#This class builds a queue using pointers
class Queue:
    def __init__(self, mymax):
        self.mymax = mymax
        self.arr = [None] * self.mymax
        self.head = 0
        self.tail = 0

    def dequeue(self):
        if not self.isEmpty():
            self.head += 1
        else:
            print("Queue empty: cannot dequeue value")

    def enqueue(self, val):
        if not self.isFull():
            self.val = val
            self.arr[self.tail] = self.val
            self.tail += 1
        else:
            print("Queue full: cannot enqueue value")

    def isFull(self):
        return self.tail == (self.mymax - 1)

    def isEmpty(self):
        return self.head == self.tail

    #NEW FUNCTIONS TO SUIT THE FUNCTION OF THE PROGRAM
    def view(self):
        return self.arr[self.head]
    
    def __repr__(self):
        print(self.arr)
        return ""


#Graph represented through adjacency list
graph = {
    'A': ('C', 'B'),
    'B': ('A', 'C', 'D', 'E'),
    'C': ('A', 'B', 'F', 'D'),
    'D': ('C', 'E', 'B', 'H'),
    'E': ('B', 'D'),
    'F': ('C', 'G'),
    'G': ('F', ),
    'H': ('D', )
}

def BFS(graph):
    #Initializing explored set:
    explored = set()
    
    #Initializing our stack
    queue = Queue(8) #A queue with max length 16
    
    #List to show output
    output = list()
    
    queue.enqueue(list(graph.keys())[0])  #Push first node onto the stack
    
    while queue:
        print(explored)
        print(queue)
        node = queue.view()
        print(node)
        newnode = queue.view()
        if node not in explored: 
            explored.add(node)
        for neighbour in graph[node]:
            if neighbour not in explored:
                explored.add(neighbour)
                queue.enqueue(neighbour)
            output.append(queue.view)
        queue.dequeue()
    return output

BFS(graph)

'''
Place first node in queue

LOOP until queue is empty (while queue:)
    If current node not in explored
        Place node in explored
    For node's neighbours:
        if not in explored, add to queue
    Dequeue the current node
'''