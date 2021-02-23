"""
Модуль обов'язково повинен містити функцію для забезпечення доступу
до різних частин json об'єкта. Наприклад, попросити користувача
ввести ключ словника, значення якого він хоче переглянути.
Проект повинен бути розміщений як окремий репозиторій на GitHub. 

Припустимо, API повернуло нам певний об'єкт, певні значення якого
я як користувач хочу переглянути. При розробці модуля ви можете припустити,
що користувач знає, які поля є в об'єкті, але користувачу буде приємніше,
якщо йому підкажуть набір полів, серед яких він може вибрати бажане.
У відповідь на введений користувачем ключ, потрібно показати відповідне йому значення.
Але є декілька випадків, в яких програма може повести себе по-іншому:
♦ якщо значення, яке відповідає ключу теж є об'єктом -
    в такому випадку можна відобразити весь об'єкт повністю,
    або повідомити користувача, що це теж об'єкт, і відобразити доступні ключі
♦ якщо значення є списком - можна просто показати весь список,
    або ж повідомити що це список, спитати, який за номером елемент списку відобразити...
    варіантів реалізації може бути безліч
Важливо розуміти, що немає єдиного правильного способу,
вони обмежуються лише вашою фантазією, важливо, щоб зберігалась головна умова -
навігація по json-об'єкту (бажано, щоб вона була ще й зручною).
"""

from time import sleep
import json


def slow(message):
    """
    Print text slowly creating an effect of printing machine.
    It helps user not to lose track of 'text'.
    """
    for letter in message:
        print(letter, end='', flush=True)
        sleep(0.02)
    return ''


def read_json_file(file_path: str) -> list:
    """
    Reads JSON file and return it in list-format.
    """
    with open(file_path, 'r') as fle:
        return json.load(fle)


def show_info_user() -> None:
    """
    The main function of json_helper module.
    Help user to navigate through the certain JSON file.
    """
    try:
        path_to_file = input(slow("please enter the path to your JSON file: "))
        json_object = read_json_file(path_to_file)
        next_step = json_object

        while True:
            if isinstance(next_step, dict):
                slow(
                    f"\nthis object is a dict.\nit has these keys:\n\n")
                for this_key in next_step.keys():
                    slow(this_key + '    ')
                next_index = input(slow("\nwhich one do you want to see? "))
                if next_index not in next_step.keys():
                    slow("check your input and try again: ")
                    continue
                flag = next_step[next_index]
                next_step = flag

            elif isinstance(next_step, list):
                len_of_list = len(next_step)
                if not len_of_list:
                    slow("this is an empty list: []")
                    break
                slow(f"\nthis is the list, it has {len_of_list} elements\n")
                answer = input(slow("do you want to see them all? (y/n): "))

                while answer != 'n' and answer != 'y':
                    answer = input(slow("please, type 'y' or 'n': "))

                if answer.lower() == 'y':
                    slow(next_step)
                    break

                next_index = int(input(slow(
                    f"\nokay, then, please type the index (0-{len_of_list}) of the certain element you want to see: ")))
                if next_index not in range(0, len_of_list):
                    slow("\ncheck your input and type a number from the range! ")
                    continue
                next_step_flag = next_step[next_index]
                next_step = next_step_flag

            elif (not isinstance(next_step, list) and
                    not isinstance(next_step, dict)):
                slow(f"\nthis is your element:\n{next_step}")
                break

    except FileNotFoundError:
        slow("check your input because there is no such file according to your path and try again:)")


if __name__ == "__main__":
    show_info_user()
