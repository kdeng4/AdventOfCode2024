def read_input(data_path):
    with open(data_path) as f:
        data = f.read().splitlines()
    order_set = {}
    line_set = []
    for elem in data:
        if '|' in elem:
            a, b, *_ = elem.split('|')
            if int(a) not in order_set:
                order_set[int(a)] = [int(b)]
            else:
                order_set[int(a)].append(int(b))
        elif ',' in elem:
            line = [int(x) for x in elem.split(',')]
            line_set.append(line)
    return order_set, line_set

def find_middle(order_line):
    return order_line[len(order_line) // 2]

def main():
    order_set, line_set = read_input('data/input-5.txt')
    accurate_answer = []
    for line in line_set:
        continue_check = True
        i_cnt = 1
        while i_cnt < len(line) and continue_check:
            check_point = len(line) - i_cnt
            if line[len(line) - i_cnt] in order_set:
                order_checklist = order_set[line[len(line) - i_cnt]]
                print_checklist = line[:check_point]
                e_pos = 0
                while e_pos < len(print_checklist) and continue_check:
                    if print_checklist[e_pos] in order_checklist:
                        continue_check = False
                    e_pos += 1
            i_cnt += 1
        if continue_check:
            accurate_answer.append(line)

    middle_nbr_total = 0
    for line in accurate_answer:
        middle_nbr_total += find_middle(line)
    
    print(f"Middle number total: {middle_nbr_total}")

if __name__ == '__main__':
    main()