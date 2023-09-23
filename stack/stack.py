from collections import deque


class Stack:
    def __init__(self):
        self.deque = deque([])

    def add_item(self, item):
        add = self.deque.append(item)
        return add

    def pop_item(self):
        self.deque.pop()

    def print_list(self):
        print(self.deque)


