from auxiliary_functions import read_lines


def solve_part_1(path: str):
    lines = read_lines(path)

    max_calories = 0
    current_calories = 0
    for line in lines:
        if line == '':
            if current_calories>max_calories:
                max_calories=current_calories
            current_calories = 0
        else:
            current_calories += int(line)
    print(f'Solution of part 1 = {max_calories}')


def solve_part_2(path: str):
    lines = read_lines(path)

    top1_calories = 0
    top2_calories = 0
    top3_calories = 0
    current_calories = 0
    for line in lines:
        if line == '':
            if current_calories>top1_calories:
                top3_calories=top2_calories
                top2_calories=top1_calories
                top1_calories=current_calories
            elif current_calories>top2_calories:
                top3_calories=top2_calories
                top2_calories=current_calories
            elif current_calories>top3_calories:
                top3_calories=current_calories
            current_calories = 0
        else:
            current_calories += int(line)

    sum_top3_calories = top1_calories + top2_calories + top3_calories
    print(f'Solution of part 2 = {sum_top3_calories}')


def solve():
    path = 'day_01/input.txt'
    solve_part_1(path)
    solve_part_2(path)
