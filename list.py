class Node:
    def __init__(self, value):
        self.id = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def create_loop(self, count):
        self.head = Node(1)
        current = self.head

        for i in range(2, count + 1):
            current.next = Node(i)
            current = current.next

        self.tail = current
        self.tail.next = self.head

    def all_elements(self):
        elements = []
        current = self.head
        while True:
            elements.append(current.id)
            current = current.next
            if current == self.head:
                break
        return elements


    def search_exceptions(self, n, m, k):
        prev = self.tail
        current = self.head

        while current.id != m:
            prev = current
            current = current.next

        for _ in range(n):
            for _ in range(k - 1):
                prev = current
                current = current.next

            prev.next = current.next
            current = current.next

        safe_positions = []
        start_node = current
        while True:
            safe_positions.append(start_node.id)
            start_node = start_node.next
            if start_node == current:
                break

        return sorted(safe_positions)