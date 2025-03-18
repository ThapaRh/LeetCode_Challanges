#622. Design Circular Queue
#The right approach using LinkedList

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class MyCircularQueue:
    def __init__(self, k: int):
        self.head = None
        self.k = k
        self.curr = self.head
        self.count = 0
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.curr = Node(value)
            self.head = self.curr
        else:
            self.curr.next = Node(value)
            self.curr = self.curr.next
        self.count+=1
        return True     

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.count-=1
        if self.count == 0:
            self.curr = None
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.curr.val   

    def isEmpty(self) -> bool:
        return self.count==0
        
    def isFull(self) -> bool:
        return self.count==self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()