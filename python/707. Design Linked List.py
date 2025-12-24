class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.length = 0
        
    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1
        cur = self.head
        start = -1
        while start < index:
            cur = cur.next
            start += 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        head_next = self.head.next
        self.head.next = ListNode(val=val, next=head_next)
        self.length += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head
        start = 0
        while start < self.length:
            cur = cur.next
            start += 1
        
        cur.next = ListNode(val=val, next=None)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length or index < 0:
            return
        
        cur = self.head
        start = 0
        while start < index:
            cur = cur.next
            start += 1
        
        cur_next = cur.next
        cur.next = ListNode(val=val, next=cur_next)
        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length or index < 0:
            return
        
        cur = self.head
        start = 0
        while start < index:
            cur = cur.next
            start += 1
        cur.next = cur.next.next
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)