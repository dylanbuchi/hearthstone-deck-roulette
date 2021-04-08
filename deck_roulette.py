import random
import os

HS_CLASSES = {
    1: "ROGUE",
    2: "MAGE",
    3: "PALADIN",
    4: "HUNTER",
    5: "WARLOCK",
    6: "WARRIOR",
    7: "SHAMAN",
    8: "DEMON HUNTER",
    9: "DRUID",
    10: "PRIEST",
}


def clear_console():
    os.system('cls')


def generate_random_number(start, end):
    """random number from start to end (both inclusive)"""
    return random.randint(start, end)


def get_random_HS_class_to_play():
    number = generate_random_number(1, 10)
    return HS_CLASSES[number]


def print_stars(length):
    print("*" * length)


def print_class(padding):
    print_stars(padding)
    print()
    print(get_random_HS_class_to_play().center(padding))
    print()
    print_stars(padding)


def main():

    while True:
        user_input = input("\nPress enter to get a class:\n")
        if user_input:
            break

        clear_console()
        print_class(padding=20)


if __name__ == "__main__":
    main()
