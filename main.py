# CSC 413 Project: Binary Search Tree in python
#
#
#
#

# Class to build nodes for BST
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data


# Binary Search Tree class w/ methods
# BST must be correctly implemented with
# Lesser values on left side of root
# and greater values on right side of root
class BinarySearchTree:
    # root node of BST
    root = None

    # Initial constructor
    def __init__(self, root=None):
        self.root = root

    # Sets root of BST
    def set_root(self, node):
        self.root = node

    # Inserts new node of a value into the binary search tree
    def insert(self, data, node):
        # If there is no root, set root to new node
        if not self.root:
            new_node = Node(data, None)
            self.set_root(new_node)
        # If data is less than current nodes, data go left
        elif data < node.data:
            # If there is nowhere left to walk to, make a new node and add to the tree
            if not node.left:
                node.left = Node(data, node)
            # Traverse until open spot is found
            else:
                self.insert(data, node.left)
        # If data is greater than current nodes, data go left
        elif data > node.data:
            # If spot is open, create a new node and add to the tree on right side
            if not node.right:
                node.right = Node(data, node)
            # Travers until open spot is found
            else:
                self.insert(data, node.right)

    # This method prints the data of BST in-order
    def in_order(self, node):
        # If node exists
        if node:
            # Goes all the way left and works its way back to the root of each subtree
            # Prints farthest left if it exists, then the subtree root
            self.in_order(node.left)
            print(node.data)
            # Prints right side of tree at each subtree
            self.in_order(node.right)
        pass

    # Searches for a value in BST, returns true is found, false otherwise
    def search(self, val, node):
        # Value is found, return true - base case
        if val == node.data:
            return True
        if val < node.data:
            self.search(val, node.left)
        elif val > node.data:
            self.search(val, node.right)
        else:
            return False

    # Returns succesor of a node in BST
    def get_successor(self, node):
        # Parent node has a right child
        if node.right:
            # Goes to minimum value of that right child which is the successor
            return self.get_min(node.right)
        y = node.parent
        while y and node == y.right:
            node = y
            y = y.parent
        return y

    # TODO: This
    def delete(self, node, val):
        #  If value is equal to node value, we have found node to be deleted! - base case
        if val == node.data:
            # If value has no left child, transplant node and right child
            if not node.left:
                self.transplant(node, node.right)
                # If value has no right child, transplant node and left child
            elif not node.right:
                self.transplant(node, node.left)
                # If the node has both children,
            else:
                y = self.get_min(node.right)
                if not y.parent == node:
                    self.transplant(y, y.right)
                    y.right = node.right
                    y.right.parent = y
                self.transplant(node, y)
                y.left = node.left
                y.left.parent = y
        # If value less than node's data, walk left
        elif val < node.data:
            self.delete(node.left, val)
        # If value greater than node's data, walk right
        elif val > node.data:
            self.delete(node.right, val)
        # If no node with that value exists in bst, return None
        else:
            return None

    # Transplants a parent node and a child node
    # This function helps the delete method
    def transplant(self, node, child):
        if not node.parent:
            self.root = child
        elif node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child
        if child:
            child.parent = node.parent

    # Gets minimum value in BST
    @staticmethod
    def get_min(node):
        #  While node.left exists, slide down to last node and returns the value
        while node.left:
            node = node.left
        return node


    # Gets max value in BST
    @staticmethod
    def get_max(node):
        #  While node.right exists, slide down to last node and returns the value
        while node.right:
            node = node.right
        return node


def main():
    # Test data
    input_data = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
    bst = BinarySearchTree()
    # Inserts each of the test values into the Binary Search Tree
    for num in input_data:
        bst.insert(num, bst.root)

    print("---In-order Traversal----")
    bst.in_order(bst.root)
    print("")

    max_node = bst.get_max(bst.root)
    min_node = bst.get_min(bst.root)

    print("Min: " + str(min_node.data) + " Max: " + str(max_node.data))
    print("")

    print("Deleting node with value: '15'")

    bst.delete(bst.root, 15)

    print("---In-Order Traversal----")
    bst.in_order(bst.root)

    pass


if __name__ == "__main__":
    main()
