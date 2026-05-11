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

    def enqueue(self, item: tuple[int, int]) -> None:
        """Add item at the end of the queue.

        Arguments
            - item
              The item to be added.

        Return
            None
        """
        if self.tail == -1:
            raise IndexError("Shi full bro")
        else:
            self._arr[self.tail] = item
            if self.head == -1:
                self.head = self.tail
            if (self.tail+1)%self.size == self.head:
                self.tail = -1
            else:
                self.tail += 1
                self.tail %= self.size

    def dequeue(self) -> tuple[int, int]:
        """Return the item at the head of the queue.

        Arguments
            None

        Return
            item
        """
        if self.head == -1:
            raise IndexError("Shi empty bro")
        else:
            item = self._arr[self.head]
            if self.tail == -1:
                self.tail = self.head
            if (self.head+1)%self.size == self.head:
                self.head = +1
            else:
                self.head += 1
                self.head %= self.size
            return item


if __name__ == "__main__":
    # Write any test code here and run it with
    # `python cq.py`
    q = CircularQueue(5)
    for i in range(5):
        q.enqueue(i)
    for i in range(3):
        print(q.dequeue())

