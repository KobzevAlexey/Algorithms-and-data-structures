class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # указатель на предыдущий узел
        self.next = None  # указатель на следующий узел


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # указатель на первый узел
        self.tail = None  # указатель на последний узел

    def add_node(self, data):
        """Добавляет новый узел в конец списка"""
        new_node = Node(data)

        if self.head is None:  # список пустой
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def expand_list(self):
        """Расширяет список, дублируя каждый узел"""
        curr = self.head

        while curr is not None:
            new_node = Node(curr.data)

            # вставляет новый узел после текущего узла
            new_node.prev = curr
            new_node.next = curr.next
            if curr.next is not None:
                curr.next.prev = new_node
            curr.next = new_node

            # переходит к следующему исходному узлу
            curr = new_node.next
