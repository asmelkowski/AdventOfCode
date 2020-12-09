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
    for passport in passports:
        passport = {
            field.split(":")[0]: field.split(":")[1]
            for field in " ".join(passport.split("\n")).split(" ")
        }
        if not required_fields.issubset(passport.keys()):
            continue
        if not re.match(r"^#[0-9a-f]{3,6}$", passport["hcl"]):
            continue
        byr = int(passport["byr"]) in range(1920, 2003)
        iyr = int(passport["iyr"]) in range(2010, 2021)
        eyr = int(passport["eyr"]) in range(2020, 2031)
        hgh_unit = "".join([i if not i.isdigit() else "" for i in passport["hgt"]])
        hgh_value = "".join([i if i.isdigit() else "" for i in passport["hgt"]])
        hgh = (
            int(hgh_value) in range(150, 194)
            if hgh_unit == "cm"
            else int(hgh_value) in range(59, 77)
        )
        ecl = passport["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        pid = passport["pid"].isdigit() and len(passport["pid"]) == 9
        if all((byr, iyr, eyr, hgh, ecl, pid)):
            valid += 1
    return valid


if __name__ == "__main__":
    assert validate_passports_part1(load_data("test_data.txt")) == 2
    print(validate_passports_part1(load_data("input.txt")))
    assert validate_passports_part2(load_data("test_data.txt")) == 2
    print(validate_passports_part2(load_data("input.txt")))
