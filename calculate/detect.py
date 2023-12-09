def detect_clause(formula, pos):
    if formula[pos] == "S":
        return "S", 1
    elif formula[pos] == "K":
        return "K", 1
    else:
        a = 1
        i = 0
        while 0 < a:
            if formula[pos+i] == "A":
                a += 1
                i += 1
            else:
                a -= 1
                i += 1
        return formula[pos:pos+i], i