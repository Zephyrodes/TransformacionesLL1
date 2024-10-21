class ASTNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

    def __repr__(self):
        return f"ASTNode({self.value}, {self.children})"
