class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_nth_from_end(head: Node, n: int) -> int:
    # Инициализирует два указателя, медленный и быстрый, на начало списка
    slow, fast = head, head

    # Перемещает быстрый указатель на n позиций вперед по отношению к медленному указателю
    for i in range(n):
        if fast is None:
            return None  # В списке нет n элементов
        fast = fast.next

    # Перемещает медленный и быстрый указатели, пока быстрый указатель не достигнет конца списка
    while fast is not None:
        slow = slow.next
        fast = fast.next

    # Возвращает значение узла, на который указывает медленный указатель
    return slow.val
