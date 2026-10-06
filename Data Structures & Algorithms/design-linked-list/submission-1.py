class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = self.prev = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        i =0
        curr = self.left.next
        while curr is not self.right and i<index:
            curr = curr.next
            i+=1
        return curr.val if curr is not self.right else -1

    def addAtHead(self, val: int) -> None:
        curr = Node(val)
        temp = self.left.next
        curr.next = temp
        curr.prev = self.left
        temp.prev = curr
        self.left.next = curr
        self.size +=1

    def addAtTail(self, val: int) -> None:
        curr = Node(val)
        temp = self.right.prev
        curr.prev = temp
        curr.next = self.right
        self.right.prev = curr
        temp.next = curr
        self.size +=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        i = 0
        prev =self.left
        curr = prev.next
        while curr is not self.right and i<index:
            i+=1
            prev = curr
            curr = curr.next
        
        node = Node(val)
        node.next = curr
        node.prev = prev
        prev.next = node
        curr.prev = node
        self.size +=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return 
        i = 0
        prev =self.left
        curr = prev.next
        while curr is not self.right and i<index:
            i+=1
            prev = curr
            curr = curr.next
        temp = curr.next
        prev.next = temp
        temp.prev = prev
        curr.prev = curr.next = None
        self.size -=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)