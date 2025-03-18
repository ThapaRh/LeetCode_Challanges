#622. Design Circular Queue
#This is not the right approach, i used stack but should have used linkedlist, will use linkedlist and try again tomorrow

class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        if len(self.arr)<self.k:
            self.arr.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        i=1
        if (not self.arr):
            return False
        while(i<len(self.arr)):
            self.arr[i-1] = self.arr[i]
            i+=1
        self.arr.pop()
        return True


    def Front(self) -> int:
        if self.arr:
            return self.arr[0]
        else:
            return -1
        

    def Rear(self) -> int:
        if self.arr:
            return self.arr[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if self.arr:
            return False
        return True
        

    def isFull(self) -> bool:
        if len(self.arr) == self.k:
            return True
        else:
            return False