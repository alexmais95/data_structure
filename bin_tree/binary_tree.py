class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, item):
        if node is None:
            return None, parent, False
        if item == node.data:
            return node, parent, True
        if item < node.data:
            if node.left:
                return self.__find(node.left, node, item)
        if item > node.data:
            if node.right:
                return self.__find(node.right, node, item)
        return node, parent, False

    def append(self, item):
        if self.root is None:
            self.root = item
            return item

        s, p, fl_find = self.__find(self.root, None, item.data)

        if not fl_find and s:
            if item.data < s.data:
                s.left = item
            if item.data > s.data:
                s.right = item

        return item

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)


item = [10, 5, 7, 16, 13, 2, 20]

nod = Tree()

for x in item:
    nod.append(Node(x))

nod.show_tree(nod.root)
