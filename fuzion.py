def raz(list_less):  # Вход - строка, Выход - словарь где, ключь - буква, значение - количество
    result = {}
    for i in list_less:
        i_lower = i.lower()
        result[i_lower] = result.get(i_lower, 0)+1
    return result


def cal_fre(dict_co):  # Вход - словарь, Выход - словарь где, ключь - остается прежним, значение - процент частоты
    total = sum(dict_co.values())
    frequ = {}
    for k, count in dict_co.items():
        perce = (count/total)*100
        frequ[k] = round(perce, 1)
    return frequ


def analize(text, search_letter):  # Вход - текст, буква которую ищем, Выход - словарь где ключь название буквы, значение - список букв идущих за ней
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
