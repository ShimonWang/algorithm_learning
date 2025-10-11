class DoubleListNode:
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None


class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, val):
        new_node = DoubleListNode(val)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def insert_at_start(self, val):
        new_node = DoubleListNode(val)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        # self.head.prev = new_node
        # new_node.next = self.head
        # self.head = new_node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def print_at_start(self):
        cur = self.head
        while cur is not None:
            print(cur.val, end='\t')
            cur = cur.next
        print()

    def print_at_end(self):
        cur = self.tail
        while cur is not None:
            print(cur.val, end='\t')
            cur = cur.prev
        print()

    def delete(self, val):
        cur = self.head
        while cur is not None:
            if cur.val == val:
                if cur.prev is None:
                    self.head = cur.next
                    cur.next = None
                    self.head.prev = None
                    return
                if cur.next is None:
                    self.tail = cur.prev
                    cur.prev = None
                    self.tail.next = None
                    return
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
            cur = cur.next


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

    print("*********************  方法封装  ***************************")
    root = DoubleList()
    root.insert_at_end(1)
    root.insert_at_end(2)
    root.insert_at_end(3)
    root.insert_at_end(4)
    root.insert_at_end(5)

    root.insert_at_start(10)
    root.insert_at_start(20)
    root.insert_at_start(30)
    root.insert_at_start(40)
    root.insert_at_start(50)

    root.print_at_start()

    root.print_at_end()

    root.delete(50)
    root.print_at_start()

    root.delete(5)
    root.print_at_start()

    root.delete(1)
    root.print_at_start()

    root.delete(100)
    root.print_at_start()
    pass