class TreeNode:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None

    def add_child(self, child):
        self.parent = self
        self.child.append(self.child)


def build_tree():
    root = TreeNode("electronics")
    root.add_child(TreeNode("laptop"))
    root.add_child(TreeNode("plamtop"))

    return root


if __name__ == "__main__":
    root = build_tree()
    pass


