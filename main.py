import fuzion as fu
import sys
try:
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            text = file.read()
    else:
        text = input("Ведите текст\nВвод\n")
    qwest = input("Поиск по букве(a) или словарь(b)?\nВвод\n")
    if qwest == "a":
        fu.tor(text)
    elif qwest == 'b':
        print(fu.analize_text(text))
    else:
        print("Ошибка повтори")
except:
    print("Ошибка повтори")
