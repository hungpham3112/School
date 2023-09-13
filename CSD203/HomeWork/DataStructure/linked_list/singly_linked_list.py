class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None

    def __getitem__(self):
        return self.data

    def set_current(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, next_data):
        self.next = next_data


class SinglyLinkedList:
    # Function to initialize head
    def __init__(self):
        self.head: Node | None = None
        self.size = 0

    def __delitem__(self):
        del self

    def __len__(self):
        return self.size

    def __repr__(self):
        head = self.head
        node = []
        while head:
            node.append(head.data)
            head = head.next
        node.append("None")
        return " -> ".join(map(str, node))

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def isempty(self):
        return self.size == 0

    def prepend(self, node: Node):
        node.next = self.head
        self.head = node
        self.size += 1

    def append(self, node: Node):
        """
        append is a function to add a new node into the tail of linked list
        Time complexity: O(n)
        Space complexity: O(1)
        """
        head = self.head
        if head is None:
            head = node
            self.head = head
        else:
            for current_node in self:
                head = current_node
            head.next = node
        self.size += 1

    def insert(self, index: int, node: Node):
        if self.size == 0:
            raise IndexError
        elif index == 0:
            self.prepend(node)
        elif index == len(self) + 1:
            self.append(node)
        elif 0 < index < len(self) + 1:
            count = 0
            assert isinstance(self.head, Node)
            head = self.head
            while count < index - 2:
                assert isinstance(head, Node)
                head = head.next
                count += 1
            assert isinstance(head, Node)
            node.next = head.next
            head.next = node
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
        if self.head is None:
            return None
        else:
            if self.head.next is None:
                self.head = None
            else:
                head = self.head
                assert isinstance(head.next, Node)
                while head.next.next is not None:
                    head = head.next
                    assert isinstance(head.next, Node)
                term = head.next
                head.next = None
                self.size -= 1
                return term

    def pop_index(self, index: int):
        if index == 0:
            self.pop_first()
        elif index == len(self):
            self.pop_last()
        elif 0 < index < len(self) + 1:
            count = 0
            head = self.head
            assert isinstance(head, Node)
            while count < index - 2:
                head = head.next
                count += 1
                assert isinstance(head, Node)
            assert isinstance(head.next, Node)
            term = head.next
            head.next = head.next.next
            self.size -= 1
            return term
        else:
            raise IndexError("Out of index")

    def update(self, index: int, node: Node):
        index -= 1
        if self.head is None and index == 0:
            self.prepend(node)
        elif index == 0:
            assert isinstance(self.head, Node)
            node.next = self.head.next
            self.head = node
        elif 0 < index <= len(self) + 1:
            count = 0
            head = self.head
            assert isinstance(head, Node)
            while count < index - 2:
                head = head.next
                count += 1
                assert isinstance(head, Node)
            assert isinstance(head.next, Node)
            node.next = head.next.next
            head.next = node
        else:
            raise IndexError


if __name__ == "__main__":
    sllist = SinglyLinkedList()
    sllist.pop_index(0)
    sllist.append(Node(1))
    sllist.append(Node(2))
    sllist.update(1, Node(3))
    sllist.append(Node(3))
    sllist.pop_index(2)
    sllist.insert(2, Node(4))
    print(sllist)
    sllist.pop_last()
    print(sllist)
    sllist.append(Node(3))
    print(sllist)
    sllist.pop_index(2)
    print(sllist)
    sllist.pop_last()
    print(sllist)
    sllist.append(Node(5))
    sllist.prepend(Node("Hello"))
    print(sllist)
