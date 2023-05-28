class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None
        self.prev: Node | None = None


class DoublyQueue:
    # Function to initialize head
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __repr__(self):
        current = self.tail
        node = []
        while current:
            node.append(current.data)
            current = current.next
        return "None <- " + " <=> ".join(map(str, node)) + " -> None"

    def isempty(self):
        return self.size == 0

    def enqueue(self, data):
        """
        enqueue is a function to add a new data to the tail of linked list
        Time complexity: O(1)
        Space complexity: O(1)
        """
        if self.head is None:
            self.head = self.tail = Node(data)
            self.size += 1
        else:
            new_node = Node(data)
            self.tail.prev = new_node
            new_node.next = self.tail
            self.tail = new_node
            self.size += 1

    def dequeue(self):
        """
        dequeue is a function to remove a data from the head of linked list
        Time complexity: O(1)
        Space complexity: O(1)
        """
        if self.head is None:
            return None
        else:
            assert isinstance(self.tail, Node)
            temp = self.head.data
            self.head = self.head.prev
            assert isinstance(self.tail, Node)
            self.head.next = None
            self.size -= 1
            return temp


if __name__ == "__main__":
    dqueue = DoublyQueue()
    dqueue.enqueue(12)
    dqueue.enqueue("hello")
    dqueue.enqueue("world")
    dqueue.enqueue(19)
    dqueue.enqueue(20)
    print("Before: ", dqueue)
    pop = dqueue.dequeue()
    print("After:  ", dqueue)
