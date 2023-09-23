class Box:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Box_list:
    def __init__(self, head_box=None):
        self.head_box = head_box

    def add_to_beggin(self, item):
        new_box = Box(item)
        if self.head_box is not None:
            new_box.next = self.head_box
            self.head_box = new_box
        self.head_box = new_box

    def add_to_end(self, item):
        new_box = Box(item)
        if self.head_box is None:
            self.head_box = new_box
            return

        end_box = self.head_box
        while end_box.next is not None:
            end_box = end_box.next
        end_box.next = new_box

    def print_box(self):
        element = self.head_box
        while element is not None:
            print(element.data)
            element = element.next

    def index(self):
        box = self.head_box
        index = 0
        while box is not None:
            box = box.next
            index += 1
        return int(index)

    def add_by_index(self, item, index):
        new_box = Box(item)
        corent_box = self.head_box
        time = 1
        while time <= index:
            corent_box = corent_box.next
            time += 1
        new_box.next = corent_box.next
        corent_box.next = new_box

    def add_to_midle(self, item):
        new_box = Box(item)
        index = self.index()
        midle = (index) // 2
        corent_box = self.head_box
        time = 0
        while time <= midle:
            corent_box = corent_box.next
            time += 1
        new_box.next = corent_box.next
        corent_box.next = new_box

    def delete_end_box(self):
        curent_box = self.head_box
        previos_box = curent_box

        while curent_box.next is not None:
            previos_box = curent_box
            curent_box = curent_box.next
        previos_box.next = None







