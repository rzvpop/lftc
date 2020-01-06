from Entity.PIF import PIF
from Entity.SymbolTable import SymbolTable
from scanner.Scanner import *
from scanner.Spec import *

# daca gramatica nu e regular, nu se face transaformarea in automat


def __main__():
    f = open("source1.txt", "r")
    source = f.read()
    f.close()

    st_cst = SymbolTable()
    st_ident = SymbolTable()
    pif = PIF()

    line = 0
    for token in getTokens(source, separators, operators):
        # if token != ' ' and token != '\n':
        #     print(token)
        if token == ' ' or token == '\n':
            pass

        elif token in all_comp:
            pif.add_to_end(codification[token])
            if token in separators:
                line += 1

        elif isConstant(token):
            if st_cst.getCode(token) is None:
                st_cst.putSymbol(token)
            pif.add_to_end((str(codification['constant']), st_cst.getCode(token)))

        elif isIdentifier(token):
            if st_ident.getCode(token) is None:
                st_ident.putSymbol(token)
            pif.add_to_end((str(codification['identifier']), st_ident.getCode(token)))

        else:
            raise Exception('Unknown token', token, 'at logical line', str(line))

    print(codification)
    print(st_cst)
    print(st_ident)
    print(pif.getElements())


__main__()
