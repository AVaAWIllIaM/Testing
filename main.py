import fuzion as fuz
lissen = input("Введите преложение которое хотите разбить....\n\nВвод:\n")
dict_toy = fuz.raz(lissen)
dict_prezent = fuz.cal_fre(dict_toy)
result = {key: {'name': key,
                'num': dict_toy[key],
                'proc': dict_prezent[key]} for key in dict_toy}
fo = input("Введите о какой букве выдать информацию:\n\nВвод...\n")
print(f"Буква: {result[fo]['name']}\nКоличество встречаний: {result[fo]['num']}\nПроцентное соотношение: {result[fo]['proc']}")
