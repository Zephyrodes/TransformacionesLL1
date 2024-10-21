class Grammar:
    def __init__(self, productions):
        self.productions = productions
    
    def eliminate_left_recursion(self):
        new_productions = {}
        for non_terminal, rules in self.productions.items():
            direct_recursion = []
            non_recursion = []
            for rule in rules:
                if rule.startswith(non_terminal):
                    direct_recursion.append(rule[len(non_terminal):])
                else:
                    non_recursion.append(rule)
            if direct_recursion:
                new_non_terminal = non_terminal + "'"
                non_recursion.append(new_non_terminal)
                new_productions[non_terminal] = non_recursion
                new_productions[new_non_terminal] = [rule + new_non_terminal for rule in direct_recursion] + ['ε']
            else:
                new_productions[non_terminal] = rules
        self.productions = new_productions

    def eliminate_common_factors(self):
        new_productions = {}
        for non_terminal, rules in self.productions.items():
            factors = {}
            for rule in rules:
                prefix = rule[0]
                if prefix in factors:
                    factors[prefix].append(rule)
                else:
                    factors[prefix] = [rule]

            for prefix, grouped in factors.items():
                if len(grouped) > 1:
                    new_non_terminal = non_terminal + "'"
                    new_productions[non_terminal] = [prefix + new_non_terminal]
                    new_productions[new_non_terminal] = [rule[len(prefix):] for rule in grouped]
                else:
                    new_productions[non_terminal] = rules

        self.productions = new_productions

    def left_factoring(self):
        # Implementar aquí la lógica de factorización por la izquierda
        pass
