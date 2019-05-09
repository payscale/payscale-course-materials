# from lib import Stack  # uncomment when you have a class Stack
# from lib import Queue  # uncomment when you have a class Queue


# Stack code

# uncomment when you've implemented "__init__"
# s = Stack()
# print(s._data, "should be []")  # note, you don't normally using the _underscore_data
# uncomment when you've implemented "push"
# s.push(5)
# s.push(6)
# print(s._data, "should be [5, 6]")

# uncomment when you've implemented "__len__"
# print(len(s), "should be 2")
# uncomment when you've implemented "__repr__"
# print(s, "should be Stack(5, 6)")

# uncomment when you've implemented "pop"
# x = s.pop()

# uncomment before *** the when you've implemented
# __init__, __repr__, pop, and push
# print(len(s), "should be 1")
# print(s, "should be Stack(5)")

# y = s.pop()

# print(len(s), "should be 0")
# print(s, "should be Stack()")

# print(x, "should be 6")
# print(y, "should be 5")
# ***

# uncomment when you've implemented peek and the methods above
# s.push(1)
# peeked = s.peek()
# print(peeked, "should be 1")
# print(len(s), "should be 1")
# print(s, "should be Stack(1)")


# Queue code

# q = Queue()
# print(q._data, "should be []")

# uncomment when you've implemented enqueue
# q.enqueue(5)
# q.enqueue(4)
# print(q._data, "should be [4, 5]")

# uncomment when you've implemented __repr__
# print(q, "should be Queue(4, 5)")
# uncomment when you've implemented __len__
# print(len(q), "should be 2")

# uncomment when you've implemented dequeue
# x = q.dequeue()
# print(x, "should be 4")
# print(q, "should be Queue(5)")

# y = q.dequeue()
# print(y, "should be 5")
# print(q, "should be Queue()")


# Extra credit
# Use Stack to solve the balanced perenthesis problem
# Note, the "parentheses" to consider are (){}[]
# def parens_balanced(string):
#     # insert implementation here
#     pass


# text = "sljsfd(sdfjlk)sfkj)"
# result = parens_balanced(text)
# print(result, "should be False")

# text = "s(ljsfd(sdfjlk)sfkj)"
# result = parens_balanced(text)
# print(result, "should be True")

# text = "({})"
# result = parens_balanced(text)
# print(result, "should be True")

# text = "()[]{[()]}{}"
# result = parens_balanced(text)
# print(result, "should be True")

# text = "({)}"
# result = parens_balanced(text)
# print(result, "should be False")

# text = "()[]{[()}{}"
# result = parens_balanced(text)
# print(result, "should be False")
