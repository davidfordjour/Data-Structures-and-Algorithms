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


class Stack:
    def __init__(self):
        self.bottom = None
        self.top = None         # The position where values get added or removed
        self.length = 0

    def __str__(self):
        string = []
        current = self.bottom
        
        for i in range(0,self.length):
            if current == None:
                break
            
            else:
                string.append(current.getData())
                current = current.getNext()

        return "[" + ",".join([str(item) for item in string]) + "]"

    
    def isEmpty(self):
        return self.bottom == None

    def size(self):
        return self.length

    def push(self,item):
        temp = Node(item)
        self.length +=1

        if self.length == 1:
            temp.setNext(self.top)
            self.bottom = temp
            self.top = self.bottom

        else:
            self.top.setNext(temp)
            self.top = temp

    def peek(self):
        return self.top.getData()

    def pop(self):
        current = self.bottom
        previous = None
        found = False


        while current != None and not found:
            if current.getNext() == None:
                if self.length ==1:
                    self.bottom = current.getNext()
                else:
                    previous.setNext(current.getNext())
                    previous = self.top
                    
                self.length -=1
                found = True

            else:
                previous = current 
                current = current.getNext() 
                

        

        
            
            






mystack = Stack()

mystack.push('l')
mystack.push('o')
mystack.push('l')
mystack.push('x')
print(mystack)
mystack.pop()
print(mystack)
mystack.pop()
print(mystack)
mystack.pop()
print(mystack)
mystack.pop()
print(mystack)


