class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None
        self.prev: Node | None = None

    def __getitem__(self):
        return self.data

    def set_current(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, next_data):
        self.next = next_data


class DoublyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        return self.size

    def __repr__(self):
        current = self.head
        node = []
        while current:
            node.append(current.data)
            current = current.next
        return "None <- " + " <=> ".join(map(str, node)) + " -> None"

    def isempty(self):
        return self.head is None and self.tail is None

    def append(self, node: Node):
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def prepend(self, node: Node):
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
            node.prev = None
        self.size += 1

    def insert(self, index: int, node: Node):
        if self.size == 0:
            raise IndexError
        elif index == 0:
            self.prepend(node)
        elif index == len(self) + 1:
            self.append(node)
        elif 0 < index < len(self) / 2:
            count = 0
            assert self.head is not None
            current = self.head
            while count < index - 2:
                assert current is not None
                current = current.next
                count += 1
            assert current is not None
            node.next = current.next
            current.next = node
            self.size += 1
        elif len(self) / 2 <= index < len(self) + 1:
            count = 0
            current = self.tail
            while count < len(self) - index - 1:
                assert isinstance(current, Node)
                current = current.prev
                count += 1
            assert isinstance(current, Node)
            node.prev = current.prev
            assert isinstance(current.prev, Node)
            current.prev.next = node
            node.next = current
            current.prev = node
            self.size += 1
        else:
            raise IndexError

    def pop_first(self):
        if self.head is None:
            return None
        else:
            term = self.head
            self.head = self.head.next
            self.size -= 1
            return term

    def pop_last(self):
        if self.tail is None:
            return None
        else:
            term = self.tail
            self.tail = self.tail.prev
            assert isinstance(self.tail, Node)
            print(self.tail.data)
            self.tail.next = None
            self.size -= 1
            return term

    def pop_index(self, index: int):
        if index == 0:
            self.pop_first()
        elif index == len(self):
            self.pop_last()
        elif 0 < index < len(self) / 2:
            count = 0
            current = self.head
            while count < index - 1:
                assert isinstance(current, Node)
                current = current.next
                count += 1
            assert isinstance(current, Node)
            temp = current.data
            assert isinstance(current.next, Node)
            current.next = current.next.next
            assert isinstance(current.next, Node)
            assert isinstance(current.next.next, Node)
            current.next.next.prev = current
            self.size -= 1
            return temp
        elif len(self) / 2 <= index < len(self):
            count = 0
            current = self.tail
            while count < len(self) - index - 2:
                assert isinstance(current, Node)
                current = current.prev
                count += 1
            assert isinstance(current, Node)
            temp = current.data
            assert isinstance(current.prev, Node)
            assert isinstance(current.prev.prev, Node)
            current.prev.prev.next = current
            current = current.prev.prev
            self.size -= 1
            return temp
        else:
            raise IndexError("Out of index")

    def update(self, data, index):
        if index < 0 or index >= self.size:
            raise IndexError("Out of index")
        if index < self.size / 2:
            cur = self.head
            pos = 0
            while pos != index:
                assert isinstance(cur, Node)
                cur = cur.next
                pos = pos + 1
        else:
            cur = self.tail
            pos = self.size
            while pos - 1 != index:
                assert isinstance(cur, Node)
                cur = cur.prev
                pos = pos - 1
        assert isinstance(cur, Node)
        cur.data = data


if __name__ == "__main__":
    dllist = DoublyLinkedList()
    dllist.prepend(Node(123))
    dllist.append(Node(3))
    dllist.append(Node(5))
    dllist.append(Node(6))
    dllist.append(Node(7))
    dllist.append(Node(8))
    dllist.insert(3, Node("hello"))
    dllist.insert(4, Node("so 4"))
    dllist.insert(4, Node("so 5"))
    dllist.pop_index(1)
    print(dllist)
    dllist.pop_index(5)
    print(dllist)
    dllist.update("update", 5)
    print(len(dllist))
    print(dllist)
