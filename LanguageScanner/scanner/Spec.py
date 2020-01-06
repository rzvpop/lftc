separators = ['[', ']', '{', '}', '(', ')', ';', ' ', ':']
operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
             '>>', '<<', '==', '&&', '||', '!', '!=', '&', '~',
             '|', '^', '++', '--', ',']
reservedWords = ['char', 'boolean', 'integer', 'real', 'read', 'write', 'if', 'else', 'while', 'true', 'false', 'array']

all_comp = separators + operators + reservedWords
codification = dict([(all_comp[i], i + 2) for i in range(len(all_comp))])
codification['identifier'] = 0
codification['constant'] = 1
