class Node:
    def __init__(self, value):
        self.value = value  # 🎲 Valor a ser armazenado.
        self.next = None  # 👉 Forma de apontar para outro nó. Default = None.

    def __str__(self):
        return f"Node(value={self.value}, next={self.next})"
