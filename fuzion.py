from collections import defaultdict as de


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


# Вход - текст, буква которую ищем, Выход - словарь где ключь название буквы, значение - список букв идущих за ней
def analize_core(text, search_letter):
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


def analize_text(text):  # Вход - текст, Выход - словарь где ключь название буквы, значение - словарь где описанно процентное соотношение бук идущих за искомой
    result = de(lambda: {
        'nomber': 0,
        'fir': de(int)
    })
    text = text.lower()
    for i in range(len(text)-1):
        current_char = text[i]
        next_char = text[i+1]
        result[current_char]['nomber'] += 1
        result[current_char]['fir'][next_char] += 1
    if len(text) > 0:
        last_char = text[-1]
        result[last_char]['nomber'] += 1
    result = dict(result)
    for char, data in result.items():
        total_foll = sum(data['fir'].values())
        if total_foll > 0:
            for next_char, count in data['fir'].items():
                data['fir'][next_char] = round((count/total_foll)*100, 2)
    return result


def tor(lissen):  # Основной main.py выведен в функцию
    fo = input("Введите о какой букве выдать информацию:\n\nВвод...\n")
    dict_toy = raz(lissen)
    dict_prezent = cal_fre(dict_toy)
    analize = analize_core(lissen, fo)
    result = {key: {'name': key,
                    'num': dict_toy[key],
                    'proc': dict_prezent[key],
                    'foll': analize[fo]} for key in dict_toy}
    try:
        print(f"Буква: {result[fo]['name']}\nКоличество встречаний: {result[fo]['num']}\nПроцентное соотношение:{result[fo]['proc']}\nБуквы идущие после: {'-'.join(result[fo]['foll'])}")
    except:
        print("Ошибка повтори еще раз")
