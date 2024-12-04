def read_input(data_path):
    with open(data_path) as f:
        data = f.read().splitlines()
    data_list = [[int(value) for value in x.split()] for x in data]
    return data_list

def is_safe(row, safty=3):
    is_increase = True
    for i in range(len(row) - 1):
        if row[i] >= row[i + 1]:
            is_increase = False
            break
    if is_increase:
        for i in range(len(row) - 1):
            if row[i] >= row[i + 1]:
                return False
            if row[i + 1] - row[i] > safty:
                return False
    else:
        for i in range(len(row) - 1):
            if row[i] <= row[i + 1]:
                return False
            if row[i] - row[i + 1] > safty:
                return False
    return True

def list_safe(data_list, safty=3):
    saft_cnt = 0
    for row in data_list:
        if is_safe(row, safty):
            saft_cnt += 1
    return saft_cnt      

def main():
    data = read_input('data/day_2.txt')
    safe_sets_cnt = list_safe(data)
    print(safe_sets_cnt)

if __name__ == '__main__':
    main()