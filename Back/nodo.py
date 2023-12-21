class Nodo:

    def __init__(self, node):
        self.node = node
        self.siguiente = None

    def __str__(self) -> str:
        return str(self.node) 