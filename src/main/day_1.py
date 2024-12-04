def read_input(data_path):
    with open(data_path) as f:
        data = f.read().splitlines()
    col_one = [int(x.split()[0]) for x in data]
    col_two = [int(x.split()[1]) for x in data]
    return col_one, col_two

def list_gen(col_one, col_two):
    new_list = []
    diff = 0
    while len(col_one) > 0 and len(col_two) > 0:
        smallest_col_one = min(col_one)
        smallest_col_two = min(col_two)
        col_one.remove(smallest_col_one)
        col_two.remove(smallest_col_two)
        new_list.append([smallest_col_one, smallest_col_two])
        diff += abs(smallest_col_one - smallest_col_two)
    return new_list, diff

def main():
    col_one, col_two = read_input('data/day_1.txt')
    list_out, diff = list_gen(col_one, col_two)
    print(diff)

if __name__ == '__main__':
    main()