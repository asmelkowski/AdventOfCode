import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))


def load_data(file_path: str) -> list:
    with open(file_path, "r") as data_file:
        out = data_file.read().splitlines()
    return out


def count_trees(tree_map: list, step: int, down: int) -> int:
    index = step
    trees = 0
    for line in tree_map[down::down]:
        if line[index] == "#":
            trees += 1
        if index >= len(line) - step:
            index = index - len(line) + step
        else:
            index += step
    return trees


if __name__ == "__main__":
    assert count_trees(load_data("test_data.txt"), 1, 1) == 2
    assert count_trees(load_data("test_data.txt"), 3, 1) == 7
    assert count_trees(load_data("test_data.txt"), 5, 1) == 3
    assert count_trees(load_data("test_data.txt"), 7, 1) == 4
    assert count_trees(load_data("test_data.txt"), 1, 2) == 2
    print(count_trees(load_data("input.txt"), 1, 1))
    print(count_trees(load_data("input.txt"), 3, 1))
    print(count_trees(load_data("input.txt"), 5, 1))
    print(count_trees(load_data("input.txt"), 7, 1))
    print(count_trees(load_data("input.txt"), 1, 2))
