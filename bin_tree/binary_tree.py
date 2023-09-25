class Box:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def __find_item(self, parent_box, box, item):
        if box is None:
            return parent_box, None, False

        if item == box.data:
            return parent_box, box, True

        if item < box.data:
            if box.left:
                return self.__find_item(box, box.left, item)
        if item > box.data:
            if box.right:
                return self.__find_item(box, box.right, item)
        return parent_box, box, False

    def append(self, item):
        if self.root is None:
            self.root = item
            return item

        parent_box, box, flag_find = self.__find_item(None, self.root, item.data)

        if not flag_find and box:
            if item.data < box.data:
                box.left = item
            if item.data > box.data:
                box.right = item

    def show_tree(self, root):
        if root is None:
            return

        self.show_tree(root.left)
        print(root.data)
        self.show_tree((root.right))

    def dell__lif(self, parent_box, box):
        if parent_box.left == box:
            parent_box.left = None
        if parent_box.righr == box:
            parent_box.righr = None


    def dell_one_child(self, parent_box, box):
        if parent_box.left == box:
            if box.left is None:
                parent_box.left = box.right
            elif box.right is None:
                parent_box.left = box.left

        if parent_box.right == box:
            if box.right is None:
                parent_box.right = box.left
            if box.left is None:
                parent_box.right = box.right
    def find_min(self, box, parent_box):
        if box.left:
            return self.find_min(box.left, box)

        return box, parent_box
    def dell__(self, item):
        parent_box, box, flag_find = self.__find_item(None, self.root, item)

        if not flag_find:
            return None

        if box.left is None and box.right is None:
            self.dell__lif(parent_box, box)
        elif box.left is None or box.right is None:
            self.dell_one_child(parent_box, box)
        else:
            box.right, parent_box.right = self. find_min(box.right, box)



tree = Tree()
lis_t = [10, 5, 7, 2, 12, 16, 20]
for i in lis_t:
    tree.append(Box(i))

tree.show_tree(tree.root)
tree.dell__(12)
tree.show_tree(tree.root)
