from anytree import NodeMixin

root = None
input_data = []
output = []

class Node:
    def __init__(self, parent, left, right, data):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data


def insert(data, node):
    if data < node.data:
        if not node.left:
            node.left = Node(node, None, None, data)
        else:
            insert(data,node.left)
    elif data > node.data:
        if not node.right:
            node.right = Node(node,None,None,data)
        else:
            insert(node.right, data)


def in_order(node):
    if node:
        in_order(node.left)
        print(node.data)
        in_order(node.right)
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
