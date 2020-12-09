import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))


def load_data(file_path: str) -> list:
    with open(file_path, "r") as data_file:
        out = data_file.read().splitlines()
    return out


def find_seat(data: list) -> list:
    results = []
    for seat_data in data:
        row = [i for i in range(0, 128)]
        for letter in seat_data[: len(seat_data) - 3]:
            mid = int(len(row) / 2)
            if letter == "F":
                row = row[:mid]
            elif letter == "B":
                row = row[mid:]
        column = [i for i in range(0, 8)]
        for letter in seat_data[len(seat_data) - 3 :]:
            mid = int(len(column) / 2)
            if letter == "L":
                column = column[:mid]
            elif letter == "R":
                column = column[mid:]
        results.append(row[0] * 8 + column[0])
    results = sorted(results)
    test = [i for i in range(results[0], results[-1])]
    diff = [i for i in test if i not in results]
    print(diff)
    return results[-1]


if __name__ == "__main__":
    assert find_seat(load_data("test_data.txt")) == 820
    print(find_seat(load_data("input.txt")))
