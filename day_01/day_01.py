import time


# # start execution time
# start_time = time.perf_counter()
# # stop execution time
# end_time = time.perf_counter()
# print('Day 1_1 solution: {} (execution time: {} ms)'.format(solution, round((end_time - start_time) * 1000, 2)))


def read_data(path: str):
    # read file using readlines()
    data = open(path, 'r')
    rows = data.readlines()

    # remove \n and whitespaces
    rows = [x.replace("\n", "").strip() for x in rows]

    return rows


def solve_part_1(path: str):
    rows = read_data(path)

    max_calories = 0
    current_calories = 0
    for row in rows:
        if row == '':
            if current_calories>max_calories:
                max_calories=current_calories
            current_calories = 0
        else:
            current_calories += int(row)
    print(f'Solution of part 1 = {max_calories}')


def solve_part_2(path: str):
    rows = read_data(path)

    top1_calories = 0
    top2_calories = 0
    top3_calories = 0
    current_calories = 0
    for row in rows:
        if row == '':
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
            current_calories += int(row)

    sum_top3_calories = top1_calories + top2_calories + top3_calories
    print(f'Solution of part 2 = {sum_top3_calories}')


def solve(path: str):
    solve_part_1(path)
    solve_part_2(path)
