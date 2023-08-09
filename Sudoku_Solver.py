import random

grid_global = [[0]*9, [0]*9, [0]*9, [0]*9, [0]*9, [0]*9, [0]*9, [0]*9, [0]*9]


def possible(value, y, x, grid):
    # X check
    if value in grid[y]:
        return False
    # Y check
    for test_y in grid:
        if value == test_y[x]:
            return False

    # Square Check
    square_index_y = (y//3)
    square_index_x = (x//3)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if y//3 == square_index_y and x//3 == square_index_x:
                if grid[y][x] == value:
                    return False

    # Final return
    return True


def fill(grid):
    random_x = random.randint(0, 8)
    random_y = random.randint(0, 8)
    random_value = random.randint(1, 9)

    if possible(random_value, random_y, random_x, grid) and grid[random_y][random_x] == 0:
        grid[random_y][random_x] = random_value
        return 1
    else:
        return 0


def populate(total_amount):
    acc = 0
    while total_amount != acc:
        acc += fill(grid_global)


def create(grid):
    for y in range(len(grid)):
        if 0 not in grid[y]:
            continue
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(n, y, x, grid):
                        grid[y][x] = n
                        create(grid)
                        grid[y][x] = 0
                    else:
                        continue
                return

    print(grid)
    print("\n")


def input_grid(grid):
    grid.clear()

    for i in range(9):
        line = input("Input line " + str(i+1) + " of the sudoku puzzle: ")
        new_inp = list(line)
        for j in range(len(new_inp)):
            new_inp[j] = int(new_inp[j])
        grid.append(new_inp)


# populate(24)
input_grid(grid_global)
create(grid_global)
