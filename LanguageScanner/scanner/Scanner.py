import re


def isConstant(token):
    return re.match('^0|[\+\-]?[1-9][0-9]*$|^\'.\'$|^".*"$', token) is not None


def isIdentifier(token):
    return re.match('^(_|[a-zA-Z])([a-zA-Z]|[0-9]|_){,7}', token) is not None


def isPartOfOperator(char, operators):
    for op in operators:
        if char in op:
            return True
    return False


def getOperator(code, index, operators):
    token = ''

    while index < len(code) and isPartOfOperator(code[index], operators):
        token += code[index]
        index += 1

    return token, index


def isEscapedQuote(line, index):
    return False if index == 0 else line[index - 1] == '\\'


def getStringToken(line, index, quote_type):
    token = ''
    quoteCount = 0

    while index < len(line) and quoteCount < 2:
        if line[index] == quote_type and not isEscapedQuote(line, index):
            quoteCount += 1
        token += line[index]
        index += 1

    return token, index


def getTokens(code, separators, operators):
    token = ''
    index = 0

    while index < len(code):
        if code[index] == '\n':
            token = ''
            index += 1
            yield '\n'
        elif code[index] == '"' or code[index] == '\'':
            if token:
                yield token
            token, index = getStringToken(code, index, code[index])
            yield token
            token = ''

        elif isPartOfOperator(code[index], operators):
            if token:
                yield token
            token, index = getOperator(code, index, operators)

        elif code[index] in separators:
            if token:
                yield token
            token, index = code[index], index + 1
            yield token
            token = ''

        else:
            token += code[index]
            index += 1

    if token:
        yield token
