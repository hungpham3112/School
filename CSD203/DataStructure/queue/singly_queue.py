class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None


class SinglyQueue:
    # Function to initialize head
    def __init__(self):
        self._head: Node | None = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __repr__(self):
        head = self._head
        node = []
        while head:
            node.append(head.data)
            head = head.next
        node.append("None")
        return " -> ".join(map(str, node))

    def isempty(self):
        return self.size == 0

    def enqueue(self, data):
        """
        enqueue is a function to add a new data to the head of linked list
        Time complexity: O(1)
        Space complexity: O(1)
        """
        if self._head is None:
            self._head = Node(data)
            self.size += 1
        else:
            new_node = Node(data)
            new_node.next = self._head
            self._head = new_node
            self.size += 1

    def dequeue(self):
        """
        dequeue is a function to remove a data from the tail of linked list
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if self._head is None:
            return None
        else:
            head = self._head
            count = 1
            while count < self.size - 1:
                assert head is not None
                head = head.next
                count += 1
            assert head is not None
            assert head.next is not None
            temp = head.next.data
            head.next = None
            self.size -= 1
            return temp


if __name__ == "__main__":
    squeue = SinglyQueue()
    squeue.enqueue(4)
    squeue.enqueue(12)
    squeue.enqueue(500)
    print("Before: ", squeue)
    pop = squeue.dequeue()
    print("After:  ", squeue)
