"""Stack and Queue library."""


class Sequence:

    def __init__(self):
        self._data = []
        self._num_items = 0

    def __repr__(self):
        csv = ", ".join([str(i) for i in self._data])
        return f"{self.__class__.__name__}({csv})"

    def __len__(self):
        return self._num_items


class Stack(Sequence):
    """
    A stack class.
    Usage:
    ```
    >>> from ds import Stack
    >>> s = Stack()
    >>> s.push(5)
    >>> len(s)
    1
    >>> print(s)
    Stack(5)
    >>> s.push(6)
    >>> len(s)
    2
    >>> print(s)
    Stack(5, 6)
    >>> popped = s.pop()
    >>> len(s)
    1
    >>> popped
    6
    ```
    """

    def push(self, x):
        """
        Add element to the Stack.
        Usage:
        ```
        >>> from ds import Stack
        >>> s = Stack()
        >>> s.push(5)
        >>> len(s)
        1
        >>> print(s)
        Stack(5)
        >>> s.push(6)
        >>> len(s)
        2
        >>> print(s)
        Stack(5, 6)
        ```
        """
        self._num_items += 1
        self._data.append(x)

    def pop(self):
        if self._num_items == 0:
            raise LookupError("can't pop() from an empty Stack")
        self._num_items -= 1
        popped = self._data[-1]
        del self._data[-1]
        return popped

    def peek(self):
        if self._num_items == 0:
            raise LookupError("can't peek() from an empty Stack")
        return self._data[-1]


class Queue(Sequence):

    def enqueue(self, x):
        self._data = [x] + self._data
        self._num_items += 1

    def dequeue(self):
        if self._num_items == 0:
            raise LookupError("Can't dequeue() from an empty Queue")
        dequeued = self._data[0]
        del self._data[0]
        self._num_items -= 1
        return dequeued

    def first(self):
        if self._num_items == 0:
            raise LookupError("Can't first() from an empty Queue")
        return self._data[0]
