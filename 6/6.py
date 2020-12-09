import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))


def load_data(file_path: str) -> list:
    with open(file_path, "r") as data_file:
        out = data_file.read().split("\n\n")
    return out


def count_answers_part1(data: list) -> int:
    yeses = 0
    for group in data:
        group = group.replace("\n", "")
        yeses += len(set(group))
    return yeses


def count_answers_part2(data: list) -> int:
    yeses = 0
    for group in data:
        subgroup = group.split("\n")
        print(subgroup)
    return yeses


if __name__ == "__main__":
    assert count_answers_part1(load_data("test_data.txt")) == 11
    print(count_answers_part1(load_data("input.txt")))
    print(count_answers_part2(load_data("test_data.txt")))
