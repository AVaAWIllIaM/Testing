def raz(list_less):  # Вход - строка, Выход - словарь где, ключь - буква, значение - количество
    list_lissen = list(list_less.lower())
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
    abc = [a, b, c, d, e, f, g, h, i, j, k, l,
           m, n, o, p, q, r, s, t, u, v, w, x, y, z]
    abc_nox = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    true_nam = []
    for alf in abc:
        true_nam.append(alf)
    pull_result = dict(zip(abc_nox, true_nam))
    result = {k: v for k, v in pull_result.items() if v != 0}
    return result


def cal_fre(dict_co):  # Вход - словарь, Выход - словарь где, ключь - остается прежним, значение - процент частоты
    total = sum(dict_co.values())
    frequ = {}
    for k, count in dict_co.items():
        perce = (count/total)*100
        frequ[k] = round(perce, 1)
    return frequ


def analize(text, search_letter):
    result = {}
    count = text.count(search_letter)

    if count == 0:
        return {False}

    following_letters = []
    for i in range(len(text)):
        if text[i] == search_letter and i + 1 < len(text):
            following_letters.append(text[i+1])
    result[search_letter] = following_letters
    return result
