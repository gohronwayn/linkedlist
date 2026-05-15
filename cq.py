"""cq.py

# Circular Queue

This module defines the CircularQueue data type
"""
############################### 72 chars ###############################


class CircularQueue:
    """Circular Queue implemented as Array.

    Methods
        - enqueue(item)
          Adds item at the end of the queue.

        - dequeue()
          Returns the first item in the queue.
    """

    def __init__(self, size: int):
        self.size = size
        self._arr = [None]*size
        self.head = -1
        self.tail = 0
    def __repr__(self) -> str:
        return f"CircularQueue({self.size})"
    def contains(self, item):
        end = self.tail
        i = self.head
        if self.is_full():
            i = (self.head+1)%self.size
            end = self.head
        elif self.is_empty():
            return False
        while i != end:
            if self._arr[i] == item:
                return True
            i += 1
            i %= self.size
        return False

    def enqueue(self, item: tuple[int, int]) -> None:
        """Add item at the end of the queue.

        Arguments
            - item
              The item to be added.

        Return
            None
        """
        if self.is_full():
            raise IndexError("Queue is full")
        elif self.isempty():
            self.head = 0
            self.arr[self.tail] = item
        else:
            self.tail = (self.tail + 1) % self.size
            self.arr[self.tail] = item
        
    def dequeue(self) -> tuple[int, int]:
        """Return the item at the head of the queue.

        Arguments
            None

        Return
            item
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            item = self._arr[self.head]
            self.head = (self.head - 1) % self.size
            return item
        
        

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.size == self.head
    

if __name__ == "__main__":
    # Write any test code here and run it with
    # `python cq.py`
    q = CircularQueue(5)
    for i in range(5):
        q.enqueue(i)
    for i in range(3):
        print(q.dequeue())
    print(q.contains(4))

