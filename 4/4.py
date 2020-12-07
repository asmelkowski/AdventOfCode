import os
import re

os.chdir(os.path.dirname(os.path.realpath(__file__)))


def load_data(file_path: str) -> list:
    with open(file_path, "r") as data_file:
        out = data_file.read().split("\n\n")
    return out


def validate_passports_part1(passports: list) -> int:
    valid = 0
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    for passport in passports:
        passport = " ".join(passport.split("\n")).split(" ")
        if not required_fields.issubset([field.split(":")[0] for field in passport]):
            continue
        valid += 1
    return valid


def validate_passports_part2(passports: list) -> int:
    valid = 0
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    ranges = {
        "byr": (1920, 2003),
        "iyr": (2010, 2021),
        "eyr": (2020, 2031),
        "hgh": {
            "cm": (150, 194),
            "in": (59, 77),
        },
    }
    for passport in passports:
        passport = {
            field.split(":")[0]: field.split(":")[1]
            for field in " ".join(passport.split("\n")).split(" ")
        }
        if not required_fields.issubset(passport.keys()):
            continue

        valid += 1
    return valid


if __name__ == "__main__":
    assert validate_passports_part1(load_data("test_data.txt")) == 2
    print(validate_passports_part1(load_data("input.txt")))
    # assert validate_passports_part2(load_data("test_data.txt")) == 2
    print(validate_passports_part2(load_data("input.txt")))
