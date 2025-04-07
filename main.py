import fuzion as fu
import sys
import json
import os
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
        name = input("Название файла?\nВвод\n")
        name = name.lower()
        os.makedirs("bin", exist_ok=True)
        if os.path.exists(f"./bin/{name}.json"):
            w = input(
                f"Фаил {name} существует, перезаписать(a) или добавить в существующий(b)?\nВвод\n")
            if w == "a":
                with open(f"./bin/{name}.json", "w") as file:
                    json.dump(fu.analize_text(text), file, indent=4)
            elif w == "b":
                with open(f"./bin/{name}.json", "a") as file:
                    json.dump(fu.analize_text(text), file, indent=4)
        else:
            with open(f"./bin/{name}.json", "w") as file:
                json.dump(fu.analize_text(text), file, indent=4)
        print(r"Фаил сохранен в репозитории \bin")
    else:
        print("Ошибка повтори")
except:
    print("Ошибка повтори")
