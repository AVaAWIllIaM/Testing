import fuzion as fu

text = input("Ведите текст\nВвод\n")

qwest = input("Поиск по букве(a) или словарь(b)?\nВвод\n")
if qwest == "a":
    fu.tor(text)
elif qwest == 'b':
    print(fu.analize_text(text))
else:
    print("Ошибка повтори")
