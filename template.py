from auxiliary_functions import read_csv_data


def solve_part_1(path: str):
    data = read_csv_data(path)
    result = 0
    for row in data:
        value = row[0]
        # ...

    print(f'Solution of part 1 = {result}')


def solve_part_2(path: str):
    data = read_csv_data(path)
    result = 0
    for row in data:
        value = row[0]
        # ...

    print(f'Solution of part 2 = {result}')


def solve():
    path = 'day_0X/input.txt'
    solve_part_1(path)
    solve_part_2(path)
