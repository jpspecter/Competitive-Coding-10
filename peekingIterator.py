#Time: O(n)
#Space: O(1)
#Program ran on leetcode sucessfully

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.itr = iterator
        self.peekFlag = False
        self.res = None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peekFlag:
            self.peekFlag = True
            self.res = self.itr.next()
            return self.res
        else:
            return self.res
        

    def next(self):
        """
        :rtype: int
        """
        if self.peekFlag:
            self.peekFlag = False
            return self.res
        else:
            return self.itr.next()
            
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peekFlag or self.itr.hasNext():
            return True
        else:
            return False
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].