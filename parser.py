def is_oper(word):
    return '(' in word

def make_args_list(arguments):
    res = []
    brackets = 0
    arg = ''
    for i, digit in enumerate(arguments):

        if digit == ',':
            if brackets == 0:
                res.append(arg)
                arg = ''
                continue

        if digit == '(':
            brackets += 1
        if digit == ')':
            brackets -= 1

        arg += digit

        if i == len(arguments) - 1:
            res.append(arg)
    return res


def parse(formula):
    formula = formula.replace(' ', '')
    if not is_oper(formula):
        if not formula.isalpha():
            return False
        return formula

    if formula.count('(') != formula.count(')'):
        return False

    name = formula[:formula.index('(')]
    args = make_args_list(formula[formula.index('(') + 1: -1])

    if not name.isalpha():
        return False

    result = [name]

    for arg in args:
        if not is_oper(arg):
            if not arg.isalpha():
                return False
            result.append(arg)
        else:
            result.append(parse(arg))
    if False in result:
        return False
    return result

renamed = 1
binds = {}
capitals = 'ABCDEFGHIJKLMNOPQRSTUVWZYZ'

def rename(array):
    if type(array) == str:
        if array[0] in capitals:
            return 1
        return array

    global renamed
    result = []
    for el in array:
        if type(el) == str:
            if el in binds:
                result.append(binds[el])
            else:
                if el[0] in capitals:
                    binds[el] = renamed
                    renamed += 1
                    result.append(binds[el])
                else:
                    result.append(el)
        else:
            result.append(rename(el))

    return result

answer = parse(input())
if answer:
    print(repr(rename(answer)))
else:
    print('NOPARSE')
