from collections import deque


class Node:
    def __init__(self, data=0):
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None
        self.next: Node | None = None
        self.prev: Node | None = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def isempty(self):
        return self.root is None

    # Recursion
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root, data):
        if data == root.data:
            return
        elif data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self._insert(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                self._insert(root.right, data)

    def breadth_first_traversal(self):
        """
        breadth_first_traversal is a function to print
        all the data of the tree as Level order traversal.
        Time Complexity: O(N) where n is the number of nodes in the binary tree.
        Auxiliary Space: O(N) where n is the number of nodes in the binary tree.
        """
        root = self.root
        if root == None:
            return
        queue = deque()
        queue.append(root)
        while queue:
            print(queue[0].data, end=" ")
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        print()

    def inorder_recursive(
        self,
    ):
        """
        inorder_recursive using recursion to traverse all the data
        Time Complexity: O(n)
        Space Complexity: O(h) where h is the height of tree
        """

        def inorder(p):
            if p == None:
                return
            inorder(p.left)
            print(f"{p.data}", end=" ")
            inorder(p.right)

        inorder(self.root)
        print()

    def inorder_iterative(self):
        """
        inorder_iterative using stack for storing data
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        temp = self.root
        stack = []
        while temp != None or not (len(stack) == 0):
            if temp != None:
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                print(str(temp.data) + " ", end="")
                temp = temp.right
        print()

    def preorder_recursive(
        self,
    ):
        """
        inorder_recursive using recursion to traverse all the data
        Time Complexity: O(n)
        Space Complexity: O(h) where h is the height of tree
        """

        def preorder(p):
            if p == None:
                return
            print(f"{p.data}", end=" ")
            preorder(p.left)
            preorder(p.right)

        preorder(self.root)
        print()

    def preorder_iterative(self):
        """
        inorder_iterative using stack for storing data
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = [self.root]
        while len(stack) > 0:
            node = stack.pop()
            assert isinstance(node, Node)
            print(node.data, end=" ")
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        print()

    def postorder_recursive(
        self,
    ):
        """
        inorder_recursive using recursion to traverse all the data
        Time Complexity: O(n)
        Space Complexity: O(h) where h is the height of tree
        """

        def postorder(p):
            if p == None:
                return
            postorder(p.left)
            postorder(p.right)
            print(f"{p.data}", end=" ")

        postorder(self.root)
        print()

    def postorder_iterative(self):
        """
        inorder_iterative using stack for storing data
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        root = self.root
        if root == None:
            return
        stack = deque()
        stack.append(root)
        output = deque()
        while stack:
            cur = stack.pop()
            output.append(cur.data)
            if cur.left != None:
                stack.append(cur.left)
            if cur.right != None:
                stack.append(cur.right)
        while output:
            print(output.pop(), end=" ")
        print()


if __name__ == "__main__":
    bts = BinarySearchTree()
    bts.insert(8)
    bts.insert(4)
    bts.insert(1)
    bts.insert(9)
    bts.insert(20)
    bts.insert(100)
    bts.insert(5)
    bts.insert(5)
    bts.insert(9)
    bts.postorder_recursive()
    bts.postorder_iterative()
