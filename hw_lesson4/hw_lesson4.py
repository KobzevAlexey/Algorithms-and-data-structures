class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.color = True  # Красный цвет обозначается True, черный - False


class Tree:
    def __init__(self):
        self.root = None

    @staticmethod
    def rotate_left(my_node):
        print("Left rotation!!")
        child = my_node.right
        child_left = child.left

        child.left = my_node
        my_node.right = child_left

        return child

    @staticmethod
    def rotate_right(my_node):
        print("Right rotation!!")
        child = my_node.left
        child_right = child.right

        child.right = my_node
        my_node.left = child_right

        return child

    @staticmethod
    def is_red(my_node):
        if my_node is None:
            return False
        return my_node.color

    @staticmethod
    def swap_colors(node1, node2):
        temp = node1.color
        node1.color = node2.color
        node2.color = temp

    def insert(self, my_node, data):
        if my_node is None:
            return Node(data)

        if data < my_node.data:
            my_node.left = self.insert(my_node.left, data)
        elif data > my_node.data:
            my_node.right = self.insert(my_node.right, data)
        else:
            return my_node

        # Case 1: Правый ребенок красный, а левый - черный или нулевой
        if self.is_red(my_node.right) and not self.is_red(my_node.left):
            my_node = self.rotate_left(my_node)
            self.swap_colors(my_node, my_node.left)

        # Case 2: Левый ребенок и его левый ребенок - красные
        if self.is_red(my_node.left) and self.is_red(my_node.left.left):
            my_node = self.rotate_right(my_node)
            self.swap_colors(my_node, my_node.right)

        # Case 3: Оба ребенка красные
        if self.is_red(my_node.left) and self.is_red(my_node.right):
            my_node.color = not my_node.color
            my_node.left.color = False
            my_node.right.color = False

        return my_node

    def inorder(self, my_node):
        if my_node is not None:
            self.inorder(my_node.left)
            c = '●' if my_node.color else '◯'
            print(str(my_node.data) + c + " ", end='')
            self.inorder(my_node.right)


if __name__ == '__main__':
    tree = Tree()
    while True:
        num = int(input("Enter an integer: "))
        tree.root = tree.insert(tree.root, num)
        tree.inorder(tree.root)

        ch = input("\nDo you want to continue? (y/n): ")
        if ch.lower() != 'y':
            break
