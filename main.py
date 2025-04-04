lissen = input("Введите преложение которое хотите разбить....\nВвод:")


def raz(list_less):
    list_lissen = list(list_less)
    a = list_lissen.count('a')
    b = list_lissen.count('b')
    c = list_lissen.count('c')
    d = list_lissen.count('d')
    e = list_lissen.count('e')
    f = list_lissen.count('f')
    g = list_lissen.count('g')
    h = list_lissen.count('h')
    i = list_lissen.count('i')
    j = list_lissen.count('j')
    k = list_lissen.count('k')
    l = list_lissen.count('l')
    m = list_lissen.count('m')
    n = list_lissen.count('n')
    o = list_lissen.count('o')
    p = list_lissen.count('p')
    q = list_lissen.count('q')
    r = list_lissen.count('r')
    s = list_lissen.count('s')
    t = list_lissen.count('t')
    u = list_lissen.count('u')
    v = list_lissen.count('v')
    w = list_lissen.count('w')
    x = list_lissen.count('x')
    y = list_lissen.count('y')
    z = list_lissen.count('z')
    abc = [a, b, c, d, i, f, g, h, i, j, k, l,
           m, n, o, p, q, r, s, t, u, v, w, x, y, z]
    true_nam = []
    for alf in abc:
        if not alf == 0:
            true_nam.append(alf)
    return true_nam
