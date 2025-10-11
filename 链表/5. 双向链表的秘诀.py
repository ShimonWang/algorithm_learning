class DoubleListNode:
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None


if __name__ == '__main__':
    head = DoubleListNode(1)

    new_node1 = DoubleListNode(2)
    head.next = new_node1
    new_node1.prev = head

    new_node2 = DoubleListNode(3)
    head.next.next = new_node2
    new_node2.prev = head.next

    print("*********************  向后遍历  ***************************")
    print(head.val)
    print(head.next.val)
    print(head.next.next.val)

    print("*********************  向前遍历  ***************************")
    cur = head.next.next
    print(cur.val)
    print(cur.prev.val)
    print(cur.prev.prev.val)

    head.next = head.next.next
    head.next.prev = head
    pass