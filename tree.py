class Node:
    def __init__(self, *args):
        if len(args) == 2:
            self.left = args[0]
            self.right = args[1]

    def init_children(self):
        self.left = Node()
        self.right = Node()

    def init_child(self):
        self.next = Node()