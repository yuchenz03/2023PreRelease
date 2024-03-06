#Depth first search using a stack implementation - my version.

### Stack data structure  ###


#This approach to building a stack uses a pointer.
class Stack:
    def __init__(self, mymax): #All other parameters are the same to the way the "pythonic" approach was programmed,
        self.mymax = mymax      #but this approach has an extra pointer that is used to go through the list
        self.arr = [None] * self.mymax
        self.pointer = -1
    
    def __repr__(self):
        print(self.arr)
        return ""

    def push(self, val): #pushes a new value to the end of the stack.
        if self.isFull():
            print("Cannot push; stack full")
        else:
            self.pointer += 1
            self.arr[self.pointer] = val

    def pop(self): #returns the last value of the stack and pointer moves left one
        if self.isEmpty():
            print("Cannot pop; stack empty")
        else:
            self.num = self.arr[self.pointer]
            self.pointer -= 1
            return self.num
            #Alternative way to solve this problem, but not exactly good practice. Ignore above and do:
            # self.pointer -= 1
            # return self.arr[self.pointer + 1]
    
    def peek(self): #returns the last value of the stack
        if self.isEmpty():
            print("Cannot peek; list empty")
        else:
            return self.arr[self.pointer]
    
    def isFull(self): #Checks if the stack is full. Private as outsiders shouldn't be able to access this method.
        if len(self.arr)-1 == self.mymax:
            return True
        else:
            return False
    
    def isEmpty(self): #In this approach to building a stack, to check if it is empty, we check if the pointer is at -1. This
        if self.pointer == -1:    #works as when the length of the list is 0, the pointer is at 0-1 which equals -1
            return True
        else:
            return False


#Graph represented through adjacency list
graph = {
'A': ('C','B'),
'B': ('A','C','D','E'),
'C': ('A','B','F','D'),
'D': ('C','E','B','H'),
'E': ('B','D'),
'F': ('C','G'),
'G': ('F',),
'H': ('D',)
}

def depthFirstSearch(graph):
    #Initializing visited set:
    visited = set()
    
    #Initializing our stack
    stack = Stack(16) #A stack with max length 16
    
    #List to show output
    output = list()
    
    stack.push(list(graph.keys())[0])  #Push first node onto the stack
    visited.add(list(graph.keys())[0]) #Add first node as visited
    
    while stack.isEmpty() == False:
        node = stack.peek()
        visited.add(node)
        for newnode in graph[node]:
            if newnode not in visited:
                stack.push(newnode)
        newnode = stack.peek()
        if node == newnode:
            if node not in output:
                output.insert(0,node)
            stack.pop()
    return output

print(depthFirstSearch(graph))