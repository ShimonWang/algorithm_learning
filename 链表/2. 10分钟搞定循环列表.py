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


def delete_node(head):
    if head is None or head.next is head:
        return head
    cur = head
    while cur.next.next is not head:
        cur = cur.next
    cur.next = head


if __name__ == '__main__':
    head = CircularListNode(1)
    head.next = head

    newNode = CircularListNode(2)
    head.next = newNode
    newNode.next = head

    tmp = CircularListNode(3)
    head.next.next = tmp
    tmp.next = head

    head.next.next = head

    print("##################  方法封装  ##################")
    root = CircularListNode(11)
    root.next = root
    append_node(root, 12)
    append_node(root, 13)
    append_node(root, 14)
    append_node(root, 15)
    append_node(root, 16)

    print_node(root)

    delete_node(root)
    print_node(root)

    delete_node(root)
    print_node(root)

    delete_node(root)
    print_node(root)

    delete_node(root)
    print_node(root)

    delete_node(root)
    print_node(root)

    delete_node(root)
    print_node(root)
    pass