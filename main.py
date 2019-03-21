from anytree import NodeMixin

root = None
output = []

class Node:
    def __init__(self, parent, left, right, data):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data


def insert(val, node):
    if val < node.data:
        pass
    else:
        pass


def in_order(node):
    pass


def delete(node):
    pass


def search(val, node):
    if val == node.data:
        return True
    if val < node.data:
        search(val, node.left)
    elif val > node.data:
        search(val, node.right)
    else:
        return False


# Gets minimum value in BST
def get_min(node):
    while node.left:
        node = node.left
    return node.data


# Gets max value in BST
def get_max(node):
    while node.right:
        node = node.right
    return node.data


def main():
    pass


if __name__ == "__main__":
    main()
