import random


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def add(self, data: int) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def size(self) -> int:
        counter = 0
        current = self.head
        while current:
            current = current.next
            counter += 1
        return counter

    def insert_at(self, node: Node | None, data) -> None:
        new_node = Node(data)
        current = self.head
        if current == node:
            self.head = new_node
            self.head.next = current
            return
        while current and current.next != node:
            current = current.next
        if current:
            current.next = new_node
            new_node.next = node

    def remove_node(self, node: Node) -> None:
        current = self.head
        if current and current == node:
            self.head = current.next
            current = None
            return
        previous = None
        while current and current != node:
            previous = current
            current = current.next
        if current is None:
            return
        previous.next = current.next
        current = None

    def remove_key(self, key: int) -> None:
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        if current is None:
            return
        previous.next = current.next
        current = None

    def search(self, data: int) -> Node | None:
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def print(self) -> None:
        current = self.head
        display = ""
        while current:
            display += str(current.data) + " "
            current = current.next
        print(display)

    def reverse(self) -> None:
        if not self.head:
            return

        previous = self.head
        current = self.head.next
        previous.next = None
        while current:
            next = current.next
            current.next = previous
            if not next:
                self.head = current
                break
            previous = current
            current = next

    def sort(self) -> None:
        if not self.head:
            return

        current = self.head.next
        while current:
            previous = self.head
            while previous != current:
                if current.data < previous.data:
                    target = current.data
                    self.insert_at(previous, target)
                    self.remove_node(current)
                    break
                previous = previous.next
            current = current.next

    def merge(self, other, sort=True) -> None:
        if not other:
            return

        if not self.head and other.head:
            self.head = other.head
        elif self.head and other.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = other.head

        if sort:
            self.sort()
        other.head = None


if __name__ == "__main__":
    # Створення списку
    llist = LinkedList()
    node_range = 10
    for _ in range(node_range):
        llist.add(random.randint(0, node_range))

    assert llist.size() == node_range

    # Друк зв'язного списку
    print("Linked list:")
    llist.print()

    # Вставляємо елемент у позицію, якщо вона існує, а потім видаляємо
    insertion_data = random.randint(node_range * 2, node_range * 3)
    node = llist.search(node_range // 3)
    if node:
        llist.insert_at(node, insertion_data)
        print(f"Linked list after insertion of {insertion_data} at {node.data}:")
        llist.print()
        llist.remove_key(insertion_data)
        print(f"Linked list after removal of {insertion_data}:")
        llist.print()

    # Розвертання зв'язного списку
    llist.reverse()

    # Друк реверсивного зв'язного списку
    print("Linked list reversed:")
    llist.print()

    # Сортування зв'язного списку
    llist.sort()

    # Друк відсортованого зв'язного списку
    print("Linked list sorted:")
    llist.print()

    # Створення іншого списку
    other_node_range = int(node_range * 1.5)
    other_llist = LinkedList()
    for _ in range(node_range):
        other_llist.add(random.randint(int(node_range * 0.5), other_node_range))

    assert other_llist.size() == node_range

    # Друк іншого зв'язного списку
    print("Other linked list:")
    other_llist.print()

    # З'єднання двох списків
    llist.merge(other_llist)

    # Інший список повинен бути порожній після об'єднання
    assert not other_llist.head
    # Перевірка розміру
    assert llist.size() == node_range * 2

    # Друк об'єднаного зв'язного списку
    print("Merged linked list:")
    llist.print()
