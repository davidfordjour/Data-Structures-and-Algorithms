class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext



class Queue:
    def __init__(self):
        self.rear = None        # Equivalent to head
        self.front = None       # Equivalent to tail
        self.length = 0

    def __str__(self):
        string = []
        current = self.rear
        
        for i in range(0,self.length):
            if current == None:
                break
            
            else:
                string.append(current.getData())
                current = current.getNext()

        return "[" + ",".join([str(item) for item in string]) + "]"

    def isEmpty(self):
        return self.rear == None

    def size(self):
        return self.length

    def enqueue(self,item):
        temp = Node(item)
        self.length +=1

        if self.length == 1:
            temp.setNext(self.front)
            self.rear = temp
            self.front = self.rear 

        else:
            temp.setNext(self.rear)
            self.rear = temp

    
    def dequeue(self):
        current = self.rear
        previous = None
        found = False


        while current != None and not found:
            if current.getNext() == None:
                if self.length ==1:
                    self.rear = current.getNext()
                else:
                    previous.setNext(current.getNext())
                    previous = self.front
                    
                self.length -=1
                found = True

            else:
                previous = current 
                current = current.getNext() 


myqueue = Queue()

myqueue.enqueue('al')
myqueue.enqueue(10)
myqueue.enqueue('-')
print(myqueue)
myqueue.dequeue()
print(myqueue)
myqueue.dequeue()
print(myqueue)