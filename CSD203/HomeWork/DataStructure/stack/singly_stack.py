class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None


class SinglyStack:
    # Function to initialize head
    def __init__(self):
        self.head: Node | None = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __repr__(self):
        head = self.head
        node = []
        while head:
            node.append(head.data)
            head = head.next
        node.append("None")
        return " -> ".join(map(str, node))

    def isempty(self):
        return self.size == 0

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            self.size += 1
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            self.size -= 1
            return popped

    def peek(self):
        if self.isempty():
            return None
        else:
            assert isinstance(self.head, Node)
            return self.head.data


if __name__ == "__main__":
    sstack = SinglyStack()
    sstack.push(1)
    sstack.push(2)
    sstack.push(3)
    sstack.push(9)
    sstack.pop()
    sstack.push(9)
    sstack.push(12)
    print("Before: ", sstack)
    sstack.pop()
    print("After:  ", sstack)
