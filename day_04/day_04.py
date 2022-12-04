from auxiliary_functions import read_csv_data


def solve_part_1(path: str):
    data = read_csv_data(path)

    result = 0
    for row in data:
        first_elf = row[0]
        second_elf = row[1]

        # Get ranges from string: 'a-b' --> Get a: all chars before '-'. Get b: rest, or all chars after '-'
        first_start, first_end = map(int, first_elf.split('-'))
        second_start, second_end = map(int, second_elf.split('-'))

        if first_start <= second_start:
            # second might be contained in first
            if first_end >= second_end:
                # second is contained in first
                result += 1
                continue

        if second_start <= first_start:
            # first might be contained in second
            if second_end >= first_end:
                # first is contained in second
                result += 1

    print(f'Solution of part 1 = {result}')


def solve_part_2(path: str):
    data = read_csv_data(path)
    result = 0
    for row in data:
        first_elf = row[0]
        second_elf = row[1]

        # Get start and end of first and second elf
        first_start, first_end = map(int, first_elf.split('-'))
        second_start, second_end = map(int, second_elf.split('-'))

        # Get ranges for first and second elf
        first_range = list(range(first_start,first_end+1))
        second_range = list(range(second_start,second_end+1))

        # Check if lists overlap using intersection
        does_overlap = bool(set(first_range) & set(second_range))
        if does_overlap:
            result += 1

    print(f'Solution of part 2 = {result}')


def solve():
    path = 'day_04/input.txt'
    solve_part_1(path)
    solve_part_2(path)
    
# Time to solve: 00:26:39
