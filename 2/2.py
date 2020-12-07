import os
import typing

os.chdir(os.path.dirname(os.path.realpath(__file__)))


def load_data(file_path: str) -> list:
    with open(file_path, "r") as data_file:
        out = data_file.read().splitlines()
    return out


def check_passwords_part1(passwords: list) -> int:
    valid = 0
    for password in passwords:
        times, char, pwd = [x.removesuffix(":") for x in password.split(" ")]
        low, high = [int(x) for x in times.split("-")]
        if pwd.count(char) in range(low, high + 1):
            valid += 1
    return valid


def check_passwords_part2(passwords: list) -> int:
    valid = 0
    for password in passwords:
        times, char, pwd = [x.removesuffix(":") for x in password.split(" ")]
        low, high = [int(x) for x in times.split("-")]
        if pwd[low - 1] == char and pwd[high - 1] == char:
            continue
        if pwd[low - 1] == char or pwd[high - 1] == char:
            valid += 1
    return valid


if __name__ == "__main__":
    assert check_passwords_part1(load_data("test_data.txt")) == 6
    print(check_passwords_part1(load_data("input.txt")))
    assert check_passwords_part2(load_data("test_data.txt")) == 8
    print(check_passwords_part2(load_data("input.txt")))
