class CircularListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def append_node(head, val):
    if head is None:
        return
    cur = head
    while cur.next is not head:
        cur = cur.next
    new_node = CircularListNode(val)
    cur.next = new_node
    new_node.next = head


# def print_node(head):
#     if head is None:
#         return
#     cur = head.next
#     if head is cur:
#         print(cur.val)
#         return
#
#     print(head.val, end='\t')
#     while cur is not head:
#         print(cur.val, end='\t')
#         cur = cur.next
#     print()
def print_node(head):
    if head is None:
        return

    print(head.val, end='\t')
    cur = head.next
    while cur is not head:
        print(cur.val, end='\t')
        cur = cur.next
    print()


# def delete_node(head):
#     if head is None or head.next is head:
#         return head
#     cur = head
#     while cur.next.next is not head:
#         cur = cur.next
#     cur.next = head


def remove_node(head, k):
    if head is None or head.next is head:
        return head
    if k == 0:
        cur = head
        while cur.next is not head:
            cur = cur.next
        cur.next = head.next
        return head

    cur = head
    for i in range(k-1):
        cur = cur.next
    tmp = cur.next
    cur.next = cur.next.next
    return tmp


def josephus(n, m):
    head = CircularListNode(1)
    head.next = head
    for i in range(1, n):
        append_node(head, i + 1)
    print_node(head)

    for j in range(n):
        node = remove_node(head, m - 1)
        print(node.val, end='\t')
        head = node.next
    print()


if __name__ == '__main__':
    # josephus(6, 5)
    # josephus(6, 1)
    josephus(41, 3)