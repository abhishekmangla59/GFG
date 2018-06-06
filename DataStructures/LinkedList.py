class Node:


    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def addNode(self,data):
        newNode = Node(data)
        if(self.head == None):

            self.head = newNode
        else:
            curr = self.head
            while(curr.next):
                curr = curr.next
            curr.next = newNode

    def delNode(self,key):
        temp = self.head

        if(temp ==None):
            return

        if(temp.data==key):
            self.head = temp.next
            return
        while(temp is not None):
            if(temp.data == key):
                break
            pre = temp
            temp = temp.next
        pre.next = temp.next
        temp = None


if __name__ == '__main__':


    list = LinkedList()
    list.addNode(10)
    list.addNode(20)
    list.addNode(30)
    list.addNode(11)


    #print(list.head.data)
    list.printList()
    list.delNode(30)
    list.printList()