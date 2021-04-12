import random
import os
import time
import sys

HS_CLASS_NAMES = [
    "ROGUE",
    "MAGE",
    "PALADIN",
    "HUNTER",
    "WARLOCK",
    "WARRIOR",
    "SHAMAN",
    "DEMON HUNTER",
    "DRUID",
    "PRIEST",
]

HS_CLASS_STRING = """(1)  ROGUE\n(2)  MAGE\n(3)  PALADIN\n(4)  HUNTER\n(5)  WARLOCK\n
(6)  WARRIOR\n(7)  SHAMAN\n(8)  DEMON HUNTER\n(9)  DRUID\n(10) PRIEST"""

TRACK_HS_CLASSES = []


def clear_console():
    os.system('cls')


def generate_random_number(start, end):
    """random number from start to end (both inclusive)"""
    return random.randint(start, end)


def get_random_HS_class_from(hs_classes):
    return random.choice(hs_classes)


def create_random_HS_class_list_by_player(numbers):
    temp = []
    for n in numbers:
        temp.append(HS_CLASS_NAMES[n - 1])
    random.shuffle(temp)
    return temp


def print_stars(length):
    print("*" * length)


def print_class(hs_class, padding):
    print_stars(padding)
    print()
    time.sleep(0.5)
    print(hs_class.center(padding))
    print()
    print_stars(padding)


def print_starter_messages():
    print("\n| Select your classes for the roulette! |\n")
    print(HS_CLASS_STRING)
    print(
        "\nType their numbers separated by a space or press Enter to select all of them: ",
        end='')


def check_number_from(array):
    for number in array:
        if not 1 <= number <= 10:
            raise ValueError


def get_user_numbers():
    try:
        numbers = prompt_user().split(" ")
        user_class_numbers = list(map(int, list(set(numbers))))
        check_number_from(user_class_numbers)

    except ValueError:
        user_class_numbers = []

    return user_class_numbers


def get_hs_classes_from(user_numbers):
    hs_classes = HS_CLASS_NAMES.copy(
    ) if not user_numbers else create_random_HS_class_list_by_player(
        user_numbers)
    return hs_classes


def get_previous_hs_class():
    if TRACK_HS_CLASSES and len(TRACK_HS_CLASSES) > 1:
        return TRACK_HS_CLASSES[-1]


def has_only_one_element(iterable):
    return len(iterable) == 1


def main():
    print_starter_messages()

    user_numbers = get_user_numbers()
    hs_classes = get_hs_classes_from(user_numbers)

    clear_console()

    while True:
        current_hs_class = get_random_HS_class_from(hs_classes)

        while True:
            if has_only_one_element(hs_classes):
                break

            previous_deck = get_previous_hs_class()

            if previous_deck == current_hs_class:
                current_hs_class = get_random_HS_class_from(hs_classes)
            else:
                break

        TRACK_HS_CLASSES.append(current_hs_class)

        print_class(current_hs_class, padding=20)

        user_input = prompt_user(
            "\nPress Enter to get another class | 'q' to exit | 'b' to go back\n"
        )

        check_user_input(user_input)
        clear_console()


def prompt_user(question=""):
    return input(question).lower().strip()


def check_user_input(user_input):
    if user_input == "q":
        sys.exit()
    if user_input == 'b':
        clear_console()
        main()


if __name__ == "__main__":
    main()
