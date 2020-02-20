"""
Linked list
questions (pdf page 106-107, book page 94-95)
solutions (pdf page 220, book page 208)
"""


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


def print_list(head):
    node = head
    while node is not None:
        print(node.data)
        node = node.next_node


def remove_next_node(node):
    if node is None or node.next_node is None:
        return
    node_to_remove = node.next_node
    node.next_node = node_to_remove.next_node
    del node_to_remove


def remove_duplicates(head):
    """2.1.1"""
    if head is None or head.next_node is None:
        return
    prev = head
    node = head.next_node
    numbers = {prev.data}
    while node is not None:
        print(numbers)
        if node.data in numbers:
            remove_next_node(prev)
            node = prev.next_node
        else:
            numbers.add(node.data)
            prev = node
            node = node.next_node


def remove_duplicates_no_buffer(head):
    """2.1.2"""
    if head is None or head.next_node is None:
        return
    prev = head
    node = head.next_node
    while node is not None:
        it = head
        was_deleted = False
        while node is not it:
            if it.data == node.data:
                remove_next_node(prev)
                node = prev.next_node
                was_deleted = True
                break
            else:
                it = it.next_node
        if not was_deleted:
            prev = node
            node = node.next_node


#
# k = Node(3)
# j = Node(3, k)
# i = Node(3, j)
# h = Node(3, i)
#
# remove_duplicates_no_buffer(h)
# print_list(h)
# -----------------------------------------------------------------------------


def get_kth_last_node(k, head):
    """2.2"""
    if head is None or k < 0:
        return None
    p_first = head
    p_last = head

    for i in range(k):
        if p_last.next_node is None:
            return None
        p_last = p_last.next_node

    while p_last.next_node is not None:
        p_first = p_first.next_node
        p_last = p_last.next_node

    return p_first


#
# c = Node(3)
# b = Node(2, c)
# a = Node(1, b)
#
# res = get_kth_last_node(2, a)
# print(f'correct example, {res.data}')
#
# res = get_kth_last_node(2, None)
# print(f'list is nil, {res}')
#
# res = get_kth_last_node(0, a)
# print(f'K is zero, {res.data}')
#
# res = get_kth_last_node(-2, a)
# print(f'K is negative, {res}')
#
# res = get_kth_last_node(7, a)
# print(f'K is bigger than the list, {res}')
# -----------------------------------------------------------------------------


def delete_middle_node(node):
    """2.3"""
    if node is None or node.next_node is None:
        return
    to_be_deleted = node.next_node
    node.data = to_be_deleted.data
    node.next_node = to_be_deleted.next_node
    del to_be_deleted


# k = Node(4)
# j = Node(3, k)
# i = Node(2, j)
# h = Node(1, i)
#
# delete_middle_node(i)
# print_list(h)
# -----------------------------------------------------------------------------


def partition(head, x):
    """2.4"""
    l_head = Node()
    r_head = Node()
    last_left = None
    n = head
    while n is not None:
        if n.data < x:
            nn = n.next_node
            n.next_node = l_head.next_node
            l_head.next_node = n
            if last_left is None:
                last_left = n
            n = nn
        else:
            nn = n.next_node
            n.next_node = r_head.next_node
            r_head.next_node = n
            n = nn
        print_list(l_head)
        print_list(r_head)
        print("--")
    if last_left is None:
        return r_head.next_node
    else:
        last_left.next_node = r_head.next_node
        return l_head.next_node


#
# g = Node(1)
# f = Node(2, g)
# e = Node(10, f)
# d = Node(5, e)
# c = Node(8, d)
# b = Node(5, c)
# a = Node(3, b)
#
# res = partition(a, 5)
# print_list(res)
# -----------------------------------------------------------------------------


def sum_lists_reversed(lst1, lst2):
    """2.5.1"""
    p1 = lst1
    p2 = lst2
    res_head = None
    res_tail = None
    t = 0
    while p1 is not None or p2 is not None or t != 0:
        val1 = p1.data if p1 is not None else 0
        val2 = p2.data if p2 is not None else 0
        digit_sum = val1 + val2 + t
        t = digit_sum // 10
        n_node = Node(digit_sum % 10)
        if res_head is None:
            res_head = n_node
            res_tail = n_node
        else:
            res_tail.next_node = n_node
            res_tail = n_node

        if p1 is not None:
            p1 = p1.next_node
        if p2 is not None:
            p2 = p2.next_node

    return res_head


def get_number(lst):
    n = lst
    number = 0
    while n is not None:
        number = number * 10 + n.data
        n = n.next_node
    return number


def sum_lists(lst1, lst2):
    num1 = get_number(lst1)
    num2 = get_number(lst2)
    total_sum = num1 + num2

    head = None
    while total_sum > 0:
        residue = total_sum % 10
        digit = Node(residue)
        if head is None:
            head = digit
        else:
            digit.next_node = head
            head = digit
        total_sum = total_sum // 10
    return head


# f = Node(5)
# e = Node(9, f)
# d = Node(2, e)
# c = Node(7)
# b = Node(1, c)
# a = Node(6, b)
#
# res = sum_lists(a, d)
# print_list(res)
# -----------------------------------------------------------------------------

def get_tail_and_size(head):
    last_node = head
    size = 1
    while last_node.next_node is not None:
        last_node = last_node.next_node
        size = size + 1
    return last_node, size


def intersection(lst1, lst2):
    """2.7"""
    if lst1 is None or lst2 is None:
        return None

    last_node1, size1 = get_tail_and_size(lst1)
    last_node2, size2 = get_tail_and_size(lst2)

    if last_node1 is not last_node2:
        return None

    shorter = lst1 if size1 < size2 else lst2
    longer = lst2 if size1 < size2 else lst1
    chop = abs(size1 - size2)
    for i in range(chop):
        longer = longer.next_node

    while shorter is not longer:
        shorter = shorter.next_node
        longer = longer.next_node

    return longer


#
# f = Node(6)
# e = Node(5, f)
# d = Node(4, e)
# c = Node(3, d)
# b = Node(2, c)
# a = Node(1, b)
# x = Node(3, d)
#
# res = intersection(a, x)
# print_list(res)
# -----------------------------------------------------------------------------


def loop_detection(head):
    """2.8"""
    if head is None:
        return None
    node = head
    nodes = set()
    while True:
        print(node.data)
        if node in nodes:
            return node
        else:
            nodes.add(node)
            node = node.next_node


f = Node(6)
e = Node(5, f)
d = Node(4, e)
c = Node(3, d)
b = Node(2, c)
a = Node(1, b)
f.next_node = c

res = loop_detection(a)
print(res)

# x = 'hippo'
# print(x.index('p'))
# lst = [6, 2, 5, 9]
# print(lst)
# lst.append(10)
# print(lst + [3, 4])
# print(lst)
# lst.extend([3, 4])
# print(lst)
# del lst[1]
# print(lst)
# lst.remove(5)
# print(lst)

# t = 2,
# print(t)
# print(t[0])
# tp = (1, 2, 3)
# print(tp)


# def double(y):
#     y.append(6)
#     return y
#
#
# x = [5]
# double(x)
# print(x)
#
# li = x
#
# li = [0, 1]
# print(x)
# print(li)


# x = [1]
# y = [1]
#
# print(x == y)
# print(hex(id(x)))
# print(hex(id(y)))
