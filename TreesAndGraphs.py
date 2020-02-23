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


# e = Node(4)
# f = Node(5)
# b = Node(1)
# a = Node(0, [b, e, f])
# c = Node(2, [b])
# d = Node(3, [c, e])
# b.children = [d, e]
#
# print("~ bfs ~")
# bfs(a)
# print("~ dfs with stack ~")
# dfs_it(a)

def route_between_nodes(node_a, node_b):
    """4.1"""
    if node_a is None or node_b is None:
        return False
    if node_a is node_b:
        return True

    q = Queue()
    node_a.visited = True
    q.add(node_a)
    while not q.is_empty():
        node = q.remove()
        for child in node.children:
            if not child.visited:
                if child is node_b:
                    return True
                child.visited = True
                q.add(child)
    return False


def construct_min_tree(numbers, fromm, to):
    """4.2"""
    if fromm > to:
        return None
    if fromm == to:
        return Node(numbers[fromm])

    mid_number_idx = ((to - fromm) // 2) + fromm
    mid_number = numbers[mid_number_idx]
    return Node(mid_number, [construct_min_tree(numbers, fromm, mid_number_idx - 1),
                             construct_min_tree(numbers, mid_number_idx + 1, to)])


def minimal_tree(numbers):
    if numbers is None or len(numbers) == 0:
        return None
    return construct_min_tree(numbers, 0, len(numbers) - 1)


nums = [1, 4, 7, 13, 20, 42, 58, 61]
res = minimal_tree(nums)
print(res)
