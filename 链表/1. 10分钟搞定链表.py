class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


def insert_node(node, value):
    if node is None:
        return
    new_node = ListNode(value)
    cur = node
    while cur.next is not None:
        cur = cur.next
    cur.next = new_node


def print_node(node):
    cur = node
    while cur is not None:
        print(cur.val, end="\t")
        cur = cur.next
    print()


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(123)
    head.next.next = ListNode(456)
    head.next.next.next = ListNode(789)

    tmp = head
    tmp = tmp.next
    tmp.next = None
    tmp.next = ListNode(100)
    head.next.next = None

    print("***********************************************************")
    root = ListNode(10)
    insert_node(root, 20)
    insert_node(root, 30)
    insert_node(root, 40)
    insert_node(root, 50)
    insert_node(root, 60)
    insert_node(root, 70)

    print("***********************************************************")
    print_node(root)
    pass
