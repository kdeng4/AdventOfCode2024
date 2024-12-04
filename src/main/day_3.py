import re

def read_input(data_path):
    with open(data_path) as f:
        data = f.read()
    return data

def search_pattern(data):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, data)
    return [int(num1) * int(num2) for num1, num2 in matches]

data = read_input('data/day_3.txt')
print(sum(search_pattern(data)))