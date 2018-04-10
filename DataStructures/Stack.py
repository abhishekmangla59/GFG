from sys import maxsize

def createStack():
    stack= []
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack,element):
    stack.append(element)
    print("Pushed into stack "+str(element))

def pop(stack):
    if(isEmpty(stack)):
        return str(-maxsize -1)
    return stack.pop()


stack = createStack()

push(stack,10)
push(stack,12)

print(pop(stack))