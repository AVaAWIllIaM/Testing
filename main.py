import fuzion as fuz
lissen = input("Введите преложение которое хотите разбить....\n\nВвод:\n")
dict_toy = fuz.raz(lissen)
dict_prezent = fuz.cal_fre(dict_toy)
for k, v in dict_toy.items():
    print(
        f"{k} встречается {v} - раз в процентном соотношении {dict_prezent[k]}%")
