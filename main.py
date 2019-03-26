
from anytree import NodeMixin


class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data


class BinarySearchTree:
    root = None
    # Initial constructor
    def __init__(self, root=None):
        self.root = root

    # Sets root of BST
    def set_root(self, node):
        self.root = node

    # Inserts vale into node
    def insert(self, data, node):
        if not self.root:
            new_node = Node(data, None)
            self.set_root(new_node)
        elif data < node.data:
            if not node.left:
                node.left = Node(data, node)
            else:
                self.insert(data, node.left)
        elif data > node.data:
            if not node.right:
                node.right = Node(node, None, None, data)
            else:
                self.insert(node.right, data)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.data)
            self.in_order(node.right)
        pass

    def search(self, val, node):
        if val == node.data:
            return True
        if val < node.data:
            self.search(val, node.left)
        elif val > node.data:
            self.search(val, node.right)
        else:
            return False

    # Returns succesor of a node
    def get_successor(self, node):
        if node.right:
            return self.get_min(node.right)
        y = node.parent
        while y and node == y.right:
            node = y
            y = y.parent
        return y

    # TODO: This
    def delete(self, node, val):
        if not node:
            return node
        pass

    # Gets minimum value in BST
    def get_min(self, node):
        while node.left:
            node = node.left
        return node.data

    # Gets max value in BST
    def get_max(self, node):
        while node.right:
            node = node.right
        return node.data



def main():
    input_data = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
    output = []
    bst = BinarySearchTree()
    for num in input_data:
        bst.insert(num, bst.root)

    pass


if __name__ == "__main__":
    main()
