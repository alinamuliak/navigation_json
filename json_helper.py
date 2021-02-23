"""
This module contains a functions that help to provide
an access to different parts of the json object
(navigation through the json-object).
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

    ♦ if the value corresponding to the key is also an object -
     in this case, inform the user that it is also an object and display the available keys
    ♦ if the value is a list - report that it is a list, ask whether user wants to see it all or
    which number of the list item to display
    """
    try:
        path_to_file = input(slow("please enter the path to your JSON file: "))
        json_object = read_json_file(path_to_file)
        next_step = json_object

        while True:
            if isinstance(next_step, dict):
                slow("\nthis object is a dict.\nit has these keys:\n\n")
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

                while answer not in ('n', 'y'):
                    answer = input(slow("please, type 'y' or 'n': "))

                if answer.lower() == 'y':
                    slow(next_step)
                    break

                next_index = int(input(slow(
                    f"\nokay, then, please type the index (0-{len_of_list}) \
of the certain element you want to see: ")))
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
        slow("check your input because there is no such file\
according to your path and try again:*")


if __name__ == "__main__":
    show_info_user()
