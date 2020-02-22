class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("No items")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("No items")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class StackArrayStyle:
    def __init__(self):
        self.items = [None] * 10
        self.top_index = None

    def push(self, item):
        if self.top_index is None:
            self.top_index = 0
        else:
            self.top_index = self.top_index + 1
        self.items[self.top_index] = item

    def pop(self):
        if self.top_index is None:
            raise Exception("No items")
        item_to_return = self.items[self.top_index]
        if self.top_index == 0:
            self.top_index = None
        else:
            self.top_index = self.top_index - 1
        return item_to_return

    def peek(self):
        if self.top_index is None:
            raise Exception("No items")
        return self.items[self.top_index]

    def is_empty(self):
        return self.top_index is None


class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self):
        if self.is_empty():
            raise Exception("no items")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise Exception("no items")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

