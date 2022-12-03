from functools import wraps
from time import time
import csv


def read_csv_data(path: str):
    csvfile = open(path, 'r', newline='')
    reader = csv.reader(csvfile, delimiter=' ')
    data = list(reader)
    # for row in data:
        # print(', '.join(row))
    return data


def read_lines(path: str):
    # read file using readlines()
    # 'r' is default
    file = open(path, 'r')
    lines = file.readlines()

    # remove \n and whitespaces
    # replace not needed. lines = [x.replace("\n", "").strip() for x in lines]
    lines = [x.strip() for x in lines]

    return lines


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f'Function {f.__name__} took {te-ts:2.4f} seconds')
        return result
    return wrap

# func:'f' args:[(100000000,), {}] took: 14.2240 secf(100000000)
