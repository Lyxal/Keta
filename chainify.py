dyads = "*+-/%@!&^:"
monads = list(map(chr, range(ord("A"), ord("Z") + 1)))
nilads = "1234567890"
syntax = "{}[]"

source = input()[::-1]

def balance(source):
    '''

    a[bc --> a[bc]
    ab} --> {ab}
    m{ab]c -> [m{ab}]c
    
    '''

    final = ""
    brackets = []
    temp = ""
    for char in source:
        if char in "[{":
            brackets.append(char)
            final += char

        elif char == "}":
            if brackets:
                if brackets[-1] == "{":
                    final += char

                else:
                    final = "{" + final + "]}"

                brackets.pop()

            else:
                final = "[" + final + "]"

        elif char == "]":
            if brackets:
                if brackets[-1] == "[":
                    final += char

                else:
                    final = "[" + final + "}]"

                brackets.pop()

            else:
                final = "[" + final + "]"

        else:
            final += char

    if brackets:
        for char in brackets:
            if char == "[":
                final += "]"
            else:
                final += "}"
    return final

def chunkify(source):
    chunks = []
    in_bracket = 0
    for char in source: pass

arities = []
for char in source:
    if char in dyads:
        arities.append((2, char))

    elif char in monads:
        arities.append((1, char))

    else:
        arities.append((0, char))

exprs = []
expr = []
patterns = ["0", "1", "2",
    "020", "021", "022", "02", "10", "11", "12", "20", "21", "22",
            "102", "110", "111", "112", "120", "121", "122",
            "202", "210", "211", "212", "220", "221", "222"]
pattern = ""
while len(arities):
    if pattern in patterns and pattern + str(arities[-1][0]) not in patterns:
        exprs.append([pattern, expr])
        expr = []
        pattern = ""
        
    pattern += str(arities[-1][0])
    expr.append(arities[-1][1])
    arities.pop()

if expr and pattern in patterns:
    exprs.append([pattern, expr])
    expr = []
    pattern = ""

print(exprs)


for exp in exprs:
    pattern, fns = exp

    if pattern == "0":
        print(fns[0])

    elif pattern == "1":
        print(fns[0] + "(R)")

    elif pattern == "2":
        print(fns[0] + "(L, R)")

    elif pattern == "020":
        print(fns[1] + "(" + fns[0] + ", " + fns[2] + ")")

    elif pattern == "021":
        print(fns[1] + "(" + fns[0] + ", " + fns[2] + "(R))")

    elif pattern == "022":
        print(fns[1] + "(" + fns[0] + ", " + fns[2] + "(L, R))")

    elif pattern == "02":
        print(fns[1] + "(" + fns[0] + ", R)")

    elif pattern == "10":
        print(fns[0] + "(" + fns[1] + ")")

    elif pattern == "11":
        print(fns[0] + "(" + fns[1] + "(R))")

    elif pattern == "12":
        print(fns[1] + "(" + fns[0] + ", " + "R)")

    elif pattern == "20":
        print(fns[0] + "(L, " + fns[1] + ")")

    elif pattern == "21":
        print(fns[0] + "(L, " + fns[1] + ")")

    elif pattern == "22":
        print(fns[1] + "(" + fns[0] + "(L, R), R*)")

    elif pattern == "102":
        print(fns[2] + "(" + fns[0] + "(" + fns[1] + "), R)")

    elif pattern == "110":
        print(fns[0] + "(" + fns[1] + "(" + fns[2] + "))")

    elif pattern == "111":
        print(fns[0] + "(" + fns[1] + "(" + fns[2] + "(R)))")

    elif pattern == "120":
        print(fns[1] + "(" + fns[0] + "(R), " + fns[2] + ")")

    elif pattern == "121":
        print(fns[1] + "(" + fns[0] + "(R), " + fns[2] + "(R*))")

    elif pattern == "122":
        print(fns[1] + "(" + fns[0] + "(R), " + fns[2] + "(L*, R*))")

    elif pattern == "202":
        print(fns[2] + "(" + fns[0] + "(L, " + fns[1] + "), R*)")

    elif pattern == "210":
        print(fns[0] + "(L, " + fns[1] + "(" + fns[2] + "))")

    elif pattern == "211":
        print(fns[0] + "(L, " + fns[1] + "(" + fns[2] + "(R*)))")

    elif pattern == "212":
        print(fns[2] + "(" + fns[0] + "(L, " + fns[1] + "(R*)), R&)")

    elif pattern == "220":
        print(fns[1] + "(" + fns[0] + "(L, R), " + fns[2] + ")")

    elif pattern == "221":
        print(fns[1] + "(" + fns[0] + "(L, R), " + fns[2] + "(R*))")

    elif pattern == "222":
        print(fns[2] + "(" + fns[1] + "(" + fns[0] + "(L, R), R*), R&)")

    
