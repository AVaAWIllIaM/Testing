import fuzion as fuz
lissen = input("Введите преложение которое хотите разбить....\n\nВвод:\n")
dict_toy = fuz.raz(lissen)
for k, v in dict_toy.items():
    print(k, ' = ', v)
