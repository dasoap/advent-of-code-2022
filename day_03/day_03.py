from auxiliary_functions import read_csv_data

# See beautiful (AI generated!) solution here: https://imgur.com/Xd2ELkC

CHAR_PRIORITIES = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,

    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52
}

# This was the first attempt to solve the issue. It worked for part 1 but not for part 2. The current solution is better.
# import difflib
# def get_overlap(s1, s2):
#     s = difflib.SequenceMatcher(None, s1, s2)
#     pos_a, pos_b, size = s.find_longest_match(0, len(s1), 0, len(s2)) 
#     return s1[pos_a:pos_a+size]


def solve_part_1(path: str):
    data = read_csv_data(path)

    result = 0
    for row in data:
        rucksack_string = row[0]

        # Split compartment string in half
        first_half = rucksack_string[:len(rucksack_string)//2]
        second_half = rucksack_string[len(rucksack_string)//2:]

        # Calculate intersection of both strings
        intersection = set(first_half) & set(second_half)
        intersecting_char = next(iter(intersection))

        # Put intersectiing char into dict to get the priority value
        priority = CHAR_PRIORITIES[intersecting_char]

        # Sum results
        result += priority

    print(f'Solution of part 1 = {result}')


def solve_part_2(path: str):
    data = read_csv_data(path)

    result = 0
    while len(data) > 0:
        strings = []
        for x in range(3):
            row_value = data.pop(0)[0]
            strings.append(row_value)
        
        string_0 = strings[0]
        string_1 = strings[1]
        string_2 = strings[2]

        # get overlap in strings
        intersection = set(string_0) & set(string_1) & set(string_2)
        intersection_char = next(iter(intersection))
        
        priority = CHAR_PRIORITIES[intersection_char]
        result += priority
    print(f'Solution of part 2 = {result}')


def solve():
    path = 'day_03/input.txt'
    solve_part_1(path)
    solve_part_2(path)
