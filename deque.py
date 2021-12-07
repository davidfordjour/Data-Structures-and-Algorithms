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

class Deque:
    def __init__(self):
        self.rear = None        # Equivalent to start of list
        self.front = None       # Equivalent to end of list
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

    def addFront(self,item):
        temp = Node(item)
        self.length +=1

        if self.length == 1:
            temp.setNext(self.front)
            self.rear = temp
            self.front = self.rear 

        else:
            self.front.setNext(temp)
            self.front = temp

    def addRear(self,item):
        temp = Node(item)
        self.length +=1

        if self.length == 1:
            temp.setNext(self.front)
            self.rear = temp
            self.front = self.rear 

        else:
            temp.setNext(self.rear)
            self.rear = temp


    def removeFront(self):
        current = self.rear
        previous = None
        found = False

        if self.length == 0:
            raise RuntimeError("No items to remove")


        while current != None and not found:
            if current.getNext() == None:
                if self.length ==1:
                    popped_item = self.rear.getData()
                    self.rear = current.getNext()
                else:
                    popped_item = current.getData()
                    previous.setNext(current.getNext())
                    previous = self.front
                    
                self.length -=1
                found = True

            else:
                previous = current 
                current = current.getNext()

        return popped_item

    
    def removeRear(self):
        current = self.rear
        found = False

        if self.length == 0:
            raise RuntimeError("No items to remove")

        while not found:
            popped_item = current.getData()
            self.rear = current.getNext()
            self.length -=1
            found = True

        return popped_item



mydeque = Deque()

mydeque.addFront(7)
mydeque.addFront(99)
mydeque.addRear(8)
mydeque.addRear(81)
print(mydeque)

