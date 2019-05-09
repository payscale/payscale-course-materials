import unittest

from lib import Stack, Queue


class TestStack(unittest.TestCase):

    def setUp(self):
        self.num_stack = Stack()
        self.num_stack.push(1)
        self.num_stack.push(2)
        self.num_stack.push(3)

        self.letter_stack = Stack()
        self.letter_stack.push("a")
        self.letter_stack.push("b")

    def test_peek(self):
        self.assertEqual(self.num_stack.peek(), 3)
        self.assertEqual(self.letter_stack.peek(), "b")

        empty_stack = Stack()
        with self.assertRaises(LookupError):
            empty_stack.peek()

    def test_push(self):
        empty_stack = Stack()
        empty_stack.push(4)
        self.assertEqual(len(empty_stack), 1)

    def test_len(self):
        self.assertEqual(len(self.num_stack), 3)
        self.assertEqual(len(self.letter_stack), 2)

    def test_repr(self):
        self.assertEqual(repr(self.num_stack), "Stack(1, 2, 3)")
        self.assertEqual(repr(self.letter_stack), "Stack(a, b)")

    def test_pop(self):
        popped = self.num_stack.pop()
        self.assertEqual(len(self.num_stack), 2)
        self.assertEqual(popped, 3)
        popped = self.num_stack.pop()
        self.assertEqual(popped, 2)
        self.assertEqual(len(self.num_stack), 1)

        empty_stack = Stack()
        with self.assertRaises(LookupError):
            empty_stack.pop()


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.num_queue = Queue()
        self.num_queue.enqueue(3)
        self.num_queue.enqueue(2)
        self.num_queue.enqueue(1)

        self.letter_queue = Queue()
        self.letter_queue.enqueue("b")
        self.letter_queue.enqueue("a")

    def test_enqueue(self):
        empty_queue = Queue()
        empty_queue.enqueue(4)
        self.assertEqual(len(empty_queue), 1)

    def test_len(self):
        self.assertEqual(len(self.num_queue), 3)
        self.assertEqual(len(self.letter_queue), 2)

    def test_repr(self):
        self.assertEqual(repr(self.num_queue), "Queue(1, 2, 3)")
        self.assertEqual(repr(self.letter_queue), "Queue(a, b)")

    def test_dequeue(self):
        first = self.num_queue.dequeue()
        self.assertEqual(len(self.num_queue), 2)
        self.assertEqual(first, 1)
        second = self.num_queue.dequeue()
        self.assertEqual(second, 2)
        self.assertEqual(len(self.num_queue), 1)

        empty_queue = Queue()
        with self.assertRaises(LookupError):
            empty_queue.dequeue()

    def test_first(self):
        self.assertEqual(self.num_queue.first(), 1)
        self.assertEqual(self.letter_queue.first(), "a")

        empty_queue = Queue()
        with self.assertRaises(LookupError):
            empty_queue.first()


if __name__ == '__main__':
    unittest.main()
