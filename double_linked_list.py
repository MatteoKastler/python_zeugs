class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
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
            self.head = new_node
            return
        temp = self.head
        temp.next = new_node
        new_node.prev = temp
        self.head = new_node

    def pop(self):
        if self.base == None:
            print("list has no elements")
            return
        temp = self.head
        self.head = temp.prev
        self.head.next = None
        del(temp)

    def remove(self, obj):
        if self.base == None:
            print("list has no elements")
            return
        temp = self.base
        while temp.data != obj:
            temp = temp.next
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        del(temp)

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
        ll.push(2)
        ll.push(4)
        ll.push(5)
        ll.printList()
        ll.remove(2)
        print("\n")
        ll.printList()
