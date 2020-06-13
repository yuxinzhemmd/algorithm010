class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.maxSize = k
        self.size = 0
        self.a = []
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size == self.maxSize:
            return False
        self.a.insert(0,value)
        self.size += 1
        return True

        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size == self.maxSize:
            return False
        self.a.append(value)
        self.size += 1
        return True
        

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size == 0:
            return False
        self.a.pop(0)
        self.size -= 1
        return True
        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size == 0:
            return False
        self.a.pop()
        self.size -= 1
        return True
        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        return self.a[0] if self.size != 0 else -1
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        return self.a[-1] if self.size != 0 else -1
        
        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        if self.size == 0:
            return True
        else: 
            return False
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        if self.size == self.maxSize:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()