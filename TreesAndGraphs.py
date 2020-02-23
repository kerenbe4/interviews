from StacksAndQueues import Stack, Queue


class Node:
    def __init__(self, data, children=[]):
        self.data = data
        self.visited = False
        self.children = children


def visit(node):
    print(node.data)


def dfs(root):
    if root is None:
        return
    root.visited = True
    visit(root)
    for child in root.children:
        if not child.visited:
            dfs(child)


def dfs_it(root):
    s = Stack()
    root.visited = True
    s.push(root)
    while not s.is_empty():
        node = s.pop()
        visit(node)
        for child in node.children:
            if not child.visited:
                child.visited = True
                s.push(child)


def bfs(root):
    q = Queue()
    root.visited = True
    q.add(root)
    while not q.is_empty():
        node = q.remove()
        visit(node)
        for child in node.children:
            if not child.visited:
                child.visited = True
                q.add(child)


e = Node(4)
f = Node(5)
b = Node(1)
a = Node(0, [b, e, f])
c = Node(2, [b])
d = Node(3, [c, e])
b.children = [d, e]

print("~ bfs ~")
bfs(a)
# print("~ dfs with stack ~")
# dfs_it(a)
