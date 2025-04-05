import fuzion as fuz
lissen = input("Введите преложение которое хотите разбить....\n\nВвод:\n")
fo = input("Введите о какой букве выдать информацию:\n\nВвод...\n")
dict_toy = fuz.raz(lissen)
dict_prezent = fuz.cal_fre(dict_toy)
analize = fuz.analize(lissen, fo)
result = {key: {'name': key,
                'num': dict_toy[key],
                'proc': dict_prezent[key],
                'foll': analize[fo]} for key in dict_toy}
print(f"Буква: {result[fo]['name']}\nКоличество встречаний: {result[fo]['num']}\nПроцентное соотношение:{result[fo]['proc']}\nБуквы идущие после: {'-'.join(result[fo]['foll'])}")
