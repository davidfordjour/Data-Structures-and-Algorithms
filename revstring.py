from pythonds.basic import Stack

string = input("Enter a string that you want to reverse: ")

def revstring(mystr):
    '''This function reverses the characters in a string.'''

    s = Stack()

    reverse = ''

    for i in mystr:
        if i == " ":
            continue
        else:
            s.push(i)

    for i in range(s.size()):
        reverse = reverse + s.pop()


    return print(reverse)


    

revstring(string)



