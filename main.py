from grammar import Grammar
from ast import ASTNode

def main():
    productions = {
        'S': ['A', 'A B'],
        'A': ['aA', 'b'],
        'B': ['bB', 'c']
    }

    grammar = Grammar(productions)

    print("Producciones originales:")
    print(grammar.productions)

    grammar.eliminate_left_recursion()
    print("Después de eliminar recursión por la izquierda:")
    print(grammar.productions)

    grammar.eliminate_common_factors()
    print("Después de eliminar factores comunes:")
    print(grammar.productions)

if __name__ == "__main__":
    main()
