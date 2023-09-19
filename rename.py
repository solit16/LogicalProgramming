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

print(repr(rename(eval(input()))))
