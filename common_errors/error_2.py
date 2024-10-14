


def c(p, t):
    s = 0
    for i in p:
        if i[0] == t:
            s += i[1] * 0.2
        else:
            s += i[1] * 0.1
    return s