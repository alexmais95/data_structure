import random

class RBNode:
    def __init__ (self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None

class RBTree:
    def __init__ (self):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        # Ordinary Binary Search Insertion
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True # new node must be red

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return

        # Set the parent and insert the new node
        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix the tree
        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:        #пока родитель нода не станет красным
            if new_node.parent == new_node.parent.parent.right:     #если родитель нода находиться в правой ветке прародителя
                u = new_node.parent.parent.left             # uncle находиться в левой ветке
                if u.red:                                   # если дядько красный
                    u.red = False                           # красим в черный
                    new_node.parent.red = False             # родитель нода тоже в черный
                    new_node.parent.parent.red = True       # прародитель красный
                    new_node = new_node.parent.parent         # определяем нода как прародителя
                else:                                        # если дядько черный
                    if new_node == new_node.parent.left:    # если нод левый ребенок
                        new_node = new_node.parent          # определяем нода как родителя
                        self.rotate_right(new_node)         # делаем правый оборот нода
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)    # делаем левый оборот прародителя
            else:
                u = new_node.parent.parent.right # uncle

                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
        self.root.red = False                                   # красим рут в черный

    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    # rotate left at node x
    def rotate_left(self, x):
        y = x.right           #Устанавливаем - у как правого ребенка от х
        x.right = y.left       #отцепляем левого ребенка у, присваеваем его как правого ребенка от х.
        if y.left != self.nil:  #делаем проверку, пустой ли левый ребенок у
            y.left.parent = x

        y.parent = x.parent     #переопределяем у и х
        if x.parent == None:      #если родитель х бил пустой, то х был рут, им становиться у
            self.root = y
        elif x == x.parent.left:       #если х был левым ребенком им станет у.
            x.parent.left = y
        else:                           #если х был правым ребенком им станет у.
            x.parent.right = y
        y.left = x                      #устанавливаем х как левого ребенка от у.
        x.parent = y                    #делаем у родителем х

    # rotate right at node x
    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def __repr__ (self):
        lines = []
        print_tree(self.root, lines)
        return '\n'.join(lines)

def print_tree(node, lines, level=0):
    if node.val != 0:
        print_tree(node.left, lines, level + 1)
        lines.append('-' * 4 * level + '> ' +
                     str(node.val) + ' ' + ('r' if node.red else 'b'))
        print_tree(node.right, lines, level + 1)

def get_nums(num):
    random.seed(1)
    nums = []
    for _ in range(num):
        nums.append(random.randint(1, num-1))
    return nums

def main():
    tree = RBTree()
    for x in range(1, 51):
        tree.insert(x)
    print(tree)

main()
