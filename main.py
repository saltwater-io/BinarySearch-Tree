from anytree import NodeMixin


class Node:
    parent = None
    left = None
    right = None
    data = None
    def __init__(self, parent, left, right, data):
        self.parent = parent
        self.left = left
        self.right = right



def insert(val, node):
    if val < node.data:
        pass
    else:
        pass

def in_order():
    pass


def delete(node):
    pass


def search():
    pass


def get_min(node):
    pass


def get_max(node):
    pass


def main():
    pass


if __name__=="__main__":
    main()
