class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.base = None

    def printList(self):
        temp = self.base
        while temp != None:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        if self.base == None:
            self.base = new_node
            return
        temp = self.base
        while temp.next != None:
            temp = temp.next
        temp.next = new_node

    def pop(self):
        if self.base == None:
            print("list has no elements")
            return
        temp = self.base
        while temp.next.next != None:
            temp = temp.next
            print(temp.data)
        del(temp.next)
        temp.next = None

    def length(self):
        cnt = 0
        temp = self.base
        while temp != None:
            cnt +=1
            temp = temp.next
        return cnt

if __name__ == '__main__':
        ll = LinkedList()
        ll.push(0)
        ll.push(1)
        ll.push(2)
        ll.printList()
        print()
        print(ll.length())