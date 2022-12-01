import csv
import time

# start execution time
start_time = time.perf_counter()


line_count = 0
result=[]
with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row==[]:
            result.append(0)
        else:
            result.append(int(row[0]))
        line_count += 1
#print(f'line_count={line_count}')

max_calories = 0
current_calories=0
for index, value in enumerate(result):
    #print(f'index={index}, value={value}')
    
    if value == 0:
        if current_calories>max_calories:
            max_calories=current_calories
        current_calories=0
    else:
        current_calories+=value
print(f'max_calories={max_calories}')


# top1_calories = 0
# top2_calories = 0
# top3_calories = 0
# current_calories = 0
# for value in result:
#     if value == 0:
#         if current_calories>top1_calories:
#             top3_calories=top2_calories
#             top2_calories=top1_calories
#             top1_calories=current_calories
#         elif current_calories>top2_calories:
#             top3_calories=top2_calories
#             top2_calories=current_calories
#         elif current_calories>top3_calories:
#             top3_calories=current_calories
#         current_calories=0
#     else:
#         current_calories+=value

# sum_top3_calories = top1_calories + top2_calories + top3_calories
# print(f'sum_top3_calories={sum_top3_calories}')




# # stop execution time
end_time = time.perf_counter()
solution=max_calories
print('Day 1_1 solution: {} (execution time: {} ms)'.format(solution, round((end_time - start_time) * 1000, 2)))