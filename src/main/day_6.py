def read_input(data_path):
    with open(data_path) as f:
        data = f.read().splitlines()
    return [[char for char in line] for line in data]

def search_guard(maze, guard='^'):
    guard_pos = None
    for i, line in enumerate(maze):
        if guard in line:
            for j, char in enumerate(line):
                if char == guard:
                    guard_pos = (i, j)
                    return guard_pos
    return guard_pos

def walk_maze(maze, guard_pos, direction=(-1,0)):
    current_maze = maze
    if guard_pos is None:
        return None
    i, j = guard_pos
    i_propose, j_propose = i, j
    walk_path = []
    while True:
        walk_path.append((i, j))
        current_maze[i][j] = 'X'
        x_step, y_step = direction
        i_propose += x_step
        j_propose += y_step
        if i_propose < 0 or j_propose < 0 or i_propose >= len(current_maze) or j_propose >= len(current_maze[0]):
            return current_maze, walk_path, (i, j), True
        if current_maze[i_propose][j_propose] == '#':
            return current_maze, walk_path, (i, j), False
        i, j = i_propose, j_propose

def main():
    data = read_input('data/input-6.txt')
    guard_pos = search_guard(data, "^")
    direction_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_direction_index = 0
    is_end = False
    current_maze = data
    walk_path = []
    while not is_end:
        current_direction = direction_list[current_direction_index]
        current_maze, line_path, guard_pos, is_end = walk_maze(current_maze, guard_pos, current_direction)
        walk_path += line_path
        current_direction_index += 1
        current_direction_index %= len(direction_list)
    print(f"Walk path:\t{walk_path}")

    cnt = 0
    counted = []
    for step in walk_path:
        if step not in counted:
            cnt += 1
            counted.append(step)
    print(f"Unique steps: {cnt}")
    
if __name__ == '__main__':
    main()