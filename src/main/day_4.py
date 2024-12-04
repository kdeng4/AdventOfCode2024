def read_input(data_path):
    with open(data_path) as f:
        data = f.read().splitlines()
    return data

def string_search(data, search_string):
    found_cnt = 0
    for search in search_string:
        for line in data:
            found_cnt += line.count(search)
    return found_cnt

def create_vertical_dataset(data):
    return [''.join(row[i] for row in data) for i in range(len(data[0]))]

def create_diagonal_dataset(data):
    diagonals = []
    n = len(data)
    m = len(data[0])
    for d in range(n + m - 1):
        diag = []
        for i in range(max(0, d - m + 1), min(n, d + 1)):
            diag.append(data[i][d - i])
        diagonals.append(''.join(diag))
    for d in range(n + m - 1):
        diag = []
        for i in range(max(0, d - m + 1), min(n, d + 1)):
            diag.append(data[i][m - 1 - (d - i)])
        diagonals.append(''.join(diag))
    return diagonals

def main(vocal=True):
    data = read_input('data/input-4.txt')
    cnt = 0
    search_string = ['XMAS', 'SAMX']

    count_line = string_search(data, search_string)
    cnt += count_line
    if vocal:
        print(f"'{search_string}' found {count_line} times in the string")

    vertical_data = create_vertical_dataset(data)
    count_vertical = string_search(vertical_data, search_string)
    cnt += count_vertical
    if vocal:
        print(f"'{search_string}' found {count_vertical} times in the vertical dataset")

    diagonal_data = create_diagonal_dataset(data)
    count_diagonal = string_search(diagonal_data, search_string)
    cnt += count_diagonal
    if vocal:
        print(f"'{search_string}' found {count_diagonal} times in the diagonal dataset")
    
    if vocal:
        print(f"Total count: {cnt}")

if __name__ == '__main__':
    main(vocal=True)