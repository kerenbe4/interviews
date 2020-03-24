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


class StackMin:
    """3.2"""
    def __init__(self):
        self.items_stack = Stack()
        self.min_data_stack = Stack()

    def push(self, item):
        self.items_stack.push(item)
        if self.min_data_stack.is_empty():
            self.min_data_stack.push({'data': item, 'occurrence': 1})
            return
        current_min = self.min_data_stack.peek()
        if item < current_min['data']:
            self.min_data_stack.push({'data': item, 'occurrence': 1})
        else:
            current_min['occurrence'] += 1

    def pop(self):
        self.items_stack.pop()
        current_min = self.min_data_stack.peek()
        if current_min['occurrence'] == 1:
            self.min_data_stack.pop()
        else:
            current_min['occurrence'] -= 1

    def min(self):
        return self.min_data_stack.peek()['data']


# s = StackMin()
# s.push(5)
# print(s.items_stack.items)
# print(s.min())
# s.push(8)
# print(s.items_stack.items)
# print(s.min())
# s.push(2)
# print(s.items_stack.items)
# print(s.min())
# s.push(4)
# print(s.items_stack.items)
# print(s.min())
# s.push(1)
# print(s.items_stack.items)
# print(s.min())
# print('--')
# s.pop()
# print(s.items_stack.items)
# print(s.min())
# s.pop()
# print(s.items_stack.items)
# print(s.min())
# s.pop()
# print(s.items_stack.items)
# print(s.min())
# s.pop()
# print(s.items_stack.items)
# print(s.min())
# -----------------------------------------------------------------------------