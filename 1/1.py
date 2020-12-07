import os
import typing

os.chdir(os.path.dirname(os.path.realpath(__file__)))


def load_data(file_path: str) -> list:
    with open(file_path, "r") as data_file:
        out = data_file.read().splitlines()
    return out


def main(numbers: list) -> int:
    result = []
    numbers = [int(i) for i in numbers]
    for i in range(len(numbers)):
        for y in range(i + 1, len(numbers)):
            for k in numbers[y:]:
                if numbers[i] + numbers[y] + k == 2020:
                    result.append(numbers[i])
                    result.append(numbers[y])
                    result.append(k)
    return result[0] * result[1] * result[2]


if __name__ == "__main__":
    print(main(load_data("input.txt")))
