from FiniteAutomata import FiniteAutomata
from Grammar import Grammar

if __name__ == '__main__':
    grammar = Grammar.fromFile('rg.txt')
    print("Grammar:")
    print(grammar)

    print("Productions for non-terminal A:")
    try:
        grammar.showProductionsFor('A')
    except Exception as e:
        print(e)
    print()

    # grammar2 = Grammar.fromConsole()
    # print('\n' + str(grammar2))

    finiteAutomata = FiniteAutomata.fromFile('fa.txt')
    print("Finite automata:")
    print(finiteAutomata)

    # finiteAutomata2 = FiniteAutomata.fromConsole()
    # print('\n' + str(finiteAutomata2))

    # Transformations
    print("Transitions for q1:")
    finiteAutomata.showTransitionsFor('q1')
    print()

    # Regular Grammar -> Finite Automata
    grammar = Grammar.fromFile('rg.txt')
    if grammar.isRegular():
        finiteAutomata = FiniteAutomata.fromRegularGrammar(grammar)
        print("Finite automata from grammar:")
        print(finiteAutomata)
    else:
        print("The grammar is not regular\n")

    # Finite Automata -> Regular Grammar

    finiteAutomata = FiniteAutomata.fromFile('fa.txt')
    grammar = Grammar.fromFiniteAutomata(finiteAutomata)

    print("Grammar from finite automata:")
    print(grammar)
