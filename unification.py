values = {}
renamed = 1

def rename(formula):
    global renamed
    res = []
    if type(formula) == int:
        return 1
    elif type(formula) == str:
        return formula
    for el in formula:
        if type(el) == int:
            if el not in values:
                values[el] = renamed
                renamed += 1
                res.append(values[el])
            else:
                res.append(values[el])

        elif type(el) == list:
            res.append(rename(el))
        else:
            res.append(el)
    return res

def change(lst, number, formula):
    res = []
    if type(lst) == int:
        if lst == number:
            return formula
        return lst
    if type(lst) == str:
        return lst
    for el in lst:
        if type(el) == int:
            if el == number:
                res.append(formula)
            else:
                res.append(el)
        elif type(el) == str:
            res.append(el)
        else:
            res.append(change(el, number, formula))
    return res

def new_bind(key, value):
    binds[key] = value
    for bind in binds:
        binds[bind] = change(binds[bind], key, value)

def pares(l1, l2):
    res = []
    for i in range(len(l1)):
        res.append((l1[i], l2[i]))
    return res

binds = {}

def unificate(first, second):
    if type(first) == type(second) == int:
        if first == second:
            if first in binds:
                return binds[first]
            return first
        else:
            if first in binds and second in binds:
                return unificate(binds[first], binds[second])
            elif first in binds and second not in binds:
                return unificate(binds[first], second)
            elif first not in binds and second in binds:
                return unificate(first, binds[second])
            else:
                new_bind(first, second)
                return binds[first]

    elif type(first) == type(second) == str and first == second:
        return first

    elif type(first) == int and type(second) != int:
        if first in binds:
            return unificate(binds[first], second)
        if not (type(second) == list and first in second):
            new_bind(first, second)
            return binds[first]
    elif type(first) != int and type(second) == int:
        if second in binds:
            return unificate(first, binds[second])
        if not (type(first) == list and second in first):
            new_bind(second, first)
            return binds[second]
    elif type(first) == type(second) == list and len(first) == len(second):
        res = [unificate(x[0], x[1]) for x in pares(first, second)]
        if False not in res:
            return res

    return False

result = unificate(eval(input()), eval(input()))
if result:
    for key in binds:
        result = change(result, key, binds[key])
    print(repr(rename(result)))
else:
    print('NO')
