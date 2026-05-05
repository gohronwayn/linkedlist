"""datastruct.py

# Data Structures

This module defines the LinkedList abstract data type
"""
############################### 72 chars ###############################


class Node:
    """Represents a node in a linkedlist.

    Arguments
        - data
          The data encapsulated in the node.

    Attributes
        - next: Node | None
          The next node in the linkedlist, or None if the node is the tail.

    Methods
        - get() -> data
          Return the data stored in the node.
    """

    def __init__(self, data: tuple[int, int]):
        # Replace the line below with your code
        self.data = data
        self.next = None
        
    def __repr__(self) -> str:
        return f'Node({self.get()})'

    def get(self) -> tuple[int, int]:
        """Return the data stored in the node.

        Arguments
            None

        Return
            tuple[int, int]
        """
        # Replace the line below with your code
        return self.data


class LinkedList:
    """Represents a sequence of data items.

    Arguments
        None

    Attributes
        None

    Methods
        - length() -> int
        - get(index) -> item
        - insert(index, item) -> None
        - append(item) -> None
        - delete(index) -> None
    """

    def __init__(self):
        self._head = None

    def __repr__(self) -> str:
        return 'LinkedList()'

    def length(self) -> int:
        """Returns the number of nodes in the linkedlist.

        Arguments
            None

        Return
            length of linkedlist as an integer (zero or positive)
        """
        if not(self._head):
            return 0
        current = self._head
        count = 0
        while current != None:
            current = current.next
            count += 1
        return count 

    def get(self, n: int) -> tuple[int, int]:
        """Returns item at n-th node.

        Arguments
            - n: int
              sequence number of item to be retrieved.

        Returns
            item

        Raises
            IndexError if n > length
        """
        current = self._head
        for i in range(n):
            current = current.next
            if current == None:
                raise IndexError
        return current.data
        

    def insert(self, n: int, item: tuple[int, int]) -> None:
        """Insert item into linkedlist at position n.

        If n == 0, inserts item at the head.
        If n == length, appends item at the tail of the linkedlist.

        Arguments
            - n: int
              sequence number of item to be inserted.

        Raises
            IndexError if n > length
        """
        if n == 0:
            temp = self._head
            self._head = Node(item)
            self._head.next = temp
            return
        last = self._head
        current = self._head.next
        for i in range(n - 1):
            if current == None:
                raise IndexError
            last = current
            current = current.next
        last.next = Node(item)
        last.next.next = current

    def append(self, item: tuple[int, int]) -> None:
        """Append item at the end of linkedlist.

        Arguments
            - item
              The item to be appended.

        Returns
            None
        """
        if self._head == None:
            self._head = Node(item)
        else:
            current = self._head
            while current.next != None:
                current = current.next
            current.next = Node(item)

    def delete(self, n: int) -> None:
        """Delete n-th item from linkedlist.

        Arguments
            - n: int
              sequence number of item to be retrieved.

        Raises
            IndexError if n > length
        """
        last = None
        current = self._head
        for i in range(n):
            last = current
            current = current.next
            if current == None:
                raise IndexError
        if last:
            last.next = current.next
        else:
            self._head = self._head.next
       
    def contains(self, item: tuple[int, int]) -> bool:
        """Checks whether an item is in the linkedlist.
        Returns a boolean value to indicate the status of the search.

        Arguments
            - item
              The item to be searched for.

        Returns
            True if item is found in the linkedlist,
            otherwise False
        """
        if not(self._head):
            return False
        current = self._head
        while current != None:
            if current.data == item:
                return True
            current = current.next
        return False


if __name__ == "__main__":
    # Write any test code here and run it with
    # `python datastruct.py`
    pass

