class Box:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, box, parent_box, item):
        if box is None:
            return None, parent_box, False
        if item == box.data:
            return box, parent_box, True
        if item < box.data:
            if box.left:
                return self.__find(box.left, box, item)
        if item > box.data:
            if box.right:
                return self.__find(box.right, box, item)
        return box, parent_box, False

    def append(self, item):
        if self.root is None:
            self.root = item
            return item

        box, parent_box, fl_find = self.__find(self.root, None, item.data)

        if not fl_find and box:
            if item.data < box.data:
                box.left = item
            if item.data > box.data:
                box.right = item

        return item

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)


item = [10, 5, 7, 16, 13, 2, 20]

tree = Tree()

for x in item:
    tree.append(Box(x))

tree.show_tree(tree.root)
