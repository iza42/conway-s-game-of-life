def main_menu_select():
    main_menu_select = int(input("""1. Select initial pattern
2. Control simulation speed
3. Start Game
4. Quit Game
Your selection: """))
    return main_menu_select


def initial_pattern_select():
    initial_pattern_select = int(input("""Select Initial Pattern
1. Gosper's Glider Gun
2. Berger's Skewed Quad
3. Conway's Pulsar
4. Back to Main Menu
Your selection: """))  # after this choice, it goes directly to the main menu
    return initial_pattern_select


def table_choice(table,
                 initial_pattern=3):  # if user did not choose any pattern specifically, conway's pulsar will be the one by default
    for i in range(30):
        row = []
        for j in range(30):
            row.append(0)
        table.append(row)
    if initial_pattern == 3:  # pulsar
        conways_pulsar = [
            (8, 11), (8, 12), (8, 13), (8, 17),
            (8, 18), (8, 19), (13, 11), (13, 12), (13, 13), (13, 17),
            (13, 18), (13, 19), (15, 11), (15, 12), (15, 13), (15, 17),
            (15, 18), (15, 19), (20, 11), (20, 12), (20, 13), (20, 17),
            (20, 18), (20, 19), (10, 9), (11, 9), (12, 9), (10, 14), (11, 14), (12, 14), (10, 16), (11, 16),
            (12, 16), (10, 21), (11, 21), (12, 21), (16, 9), (17, 9),
            (18, 9), (16, 14), (17, 14), (18, 14), (16, 16), (17, 16), (18, 16), (16, 21), (17, 21), (18, 21)

        ]
        for x, y in conways_pulsar:
            table[x][y] = 1


    elif initial_pattern == 1:  # glider gun
        gosper_glider_gun = [
            (14, 0), (14, 1), (15, 0), (15, 1),
            (14, 10), (15, 10), (16, 10), (13, 11), (17, 11), (15, 14), (12, 12), (12, 13), (18, 12), (18, 13),
            (13, 15), (14, 16),
            (15, 16), (16, 16), (17, 15), (15, 17),
            (12, 20), (13, 20), (14, 20), (12, 21), (13, 21), (14, 21), (10, 24), (11, 24),
            (11, 22), (15, 24), (16, 24), (15, 22)
        ]
        for x, y in gosper_glider_gun:
            table[x][y] = 1
    elif initial_pattern == 2:  # berger's skewed quad
        berger_skewed_quad = [
            (9, 9), (10, 9), (11, 9), (8, 10), (8, 11), (9, 12), (10, 12), (9, 17), (9, 18),
            (9, 19), (10, 17), (11, 17), (12, 18), (12, 19), (10, 20), (11, 20), (16, 9), (16, 10),
            (17, 8), (18, 8), (19, 9), (19, 10), (19, 11), (18, 11), (17, 11), (20, 17), (20, 18),
            (18, 16), (19, 16), (17, 17), (17, 18), (17, 19), (18, 19), (19, 19), (11, 10), (11, 11)
        ]
        for x, y in berger_skewed_quad:
            table[x][y] = 1

    return table


def speed_menu_select():
    speed_menu_select = int(input("""Control Simulation Speed
1. One generation at a time
2. Three generations at a time
3. Ten generations at a time
4. Back to Main Menu
Your selection: """))
    return speed_menu_select


def nextGeneration(grid, M, N):
    future = [[0 for c in range(N)] for b in range(M)]

    # Loop through every cell
    for l in range(M):

        for m in range(N):

            # finding no Of Neighbours that are alive
            aliveNeighbours = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (l + i >= 0 and l + i < M) and (m + j >= 0 and m + j < N):
                        aliveNeighbours += grid[l + i][m + j]

            # The cell needs to be subtracted from
            # its neighbours as it was counted before
            aliveNeighbours -= grid[l][m]

            # Implementing the Rules of Life

            # Cell is lonely and dies
            if (grid[l][m] == 1) and (aliveNeighbours < 2):
                future[l][m] = 0

            # Cell dies due to over population
            elif (grid[l][m] == 1) and (aliveNeighbours > 3):
                future[l][m] = 0

            # A new cell is born
            elif (grid[l][m] == 0) and (aliveNeighbours == 3):
                future[l][m] = 1

            # Remains the same
            else:
                future[l][m] = grid[l][m]
    return future


def advance_generations(grid, M, N,steps=1):  # if the number of steps is not specified, one generation at a time by default
    """it shows the next generation as much as the number of steps specified by the user"""
    current_grid = grid  # Initialize current grid with the initial grid
    for _ in range(steps):
        current_grid = nextGeneration(current_grid, M, N)
    return current_grid


def live_cells(grid):
    """ gives the live cell number of the current state of the grid"""
    live = 0
    for row in grid:
        for point in row:
            if point == 1:  # 0's represent alive cell, "_" sign represent dead cell
                live += 1
    return live


def print_table(table):
    conservation = {1: "0", 0: "_"}
    new_table = [[conservation[item_] for item_ in row_] for row_ in table]

    print("""    0  1  2  3  4 | 5  6  7  8  9 |10 11 12 13 14 |15 16 17 18 19 |20 21 22 23 24 |25 26 27 28 29|
   ┌──────────────┬───────────────┬───────────────┬───────────────┬───────────────┬──────────────┐""")
    for index, row in enumerate(new_table):
        if index in range(10):
            print(f" {index}  ", end="")
        else:
            print(f"{index}  ", end="")
        for index1, item in enumerate(row):
            item = item.ljust(3, " ")

            if index1 in (
                    4, 9, 14, 19,
                    24):  # indexes of places where there are 3 spaces  instead of 2 in between the short lines
                item = item + " "
                print(item, end="")
            else:
                print(item, end="")
        print()  # to create a row, that is, to switch to the bottom row every 30 items
        if index in (4, 9, 14, 19, 24):
            print(
                """   ├──────────────┼───────────────┼───────────────┼───────────────┼───────────────┼──────────────┤""")
    print("""   └──────────────┴───────────────┴───────────────┴───────────────┴───────────────┴──────────────┘""")


def start_game(pattern, generation=1):
    print("Conway's Game of Life!")
    print_table(pattern)
    live_cell = live_cells(pattern)
    print(f"LIVE CELLS: {live_cell}")
    print(f"GENERATION: {generation}")
    menu = int(input("""1. Toggle cell state (to change)
2. Continue the next generation(s)
3. Quit Game
Your selection:"""))
    return menu, generation


def take_indices():
    indices = input(
        """Enter the row, column indices separated by a comma to be converted into the opposite value. There will be 
no whitespaces. Type 'r' for returning the game without any change: """)
    return indices


def change(table, indices):
    """ if the given indices is not equal to r this function toggle the cells in the given indices"""
    row = int(indices.strip(" ").split(",")[0])
    column = int(indices.strip(" ").split(",")[1])
    if table[row][column] == 1:
        table[row][column] = 0
    elif table[row][column] == 0:
        table[row][column] = 1
    return table


def main():
    """ in this menu that I created for example if you choose something in select initial pattern window(submenu) you will be again directed to
     the same submenu window until you press 4 for exit that menu and go to the main menu"""
    initial_pattern = table_choice(
        [])  # to make available outside  the while loops, the pulsar is also set by default at the moment, if the user does not specifically specify an initial pattern, the pulsar will execute
    step = 1  # if the user does not specify the number of steps specifically, the program takes it as 1
    advance_generations_counter = 1
    while True:

        main_select = main_menu_select()
        if main_select == 1:

            while True:
                pattern_select = initial_pattern_select()
                if pattern_select == 4:
                    break
                else:
                    initial_pattern = table_choice([], pattern_select)

                    continue

        elif main_select == 2:

            while True:

                speed_select = speed_menu_select()
                if speed_select == 4:
                    break
                elif speed_select == 1:
                    step = 1

                    continue
                elif speed_select == 2:
                    step = 3

                    continue
                elif speed_select == 3:
                    step = 10

                    continue

        elif main_select == 3:
            while True:

                menu, generation_count = start_game(initial_pattern, advance_generations_counter)
                if menu == 1:
                    while True:
                        indices = take_indices()
                        if indices == "r":
                            break
                        else:
                            initial_pattern = change(initial_pattern, indices)
                            break

                elif menu == 2:
                    advance_generations_counter += 1
                    next_generation = advance_generations(initial_pattern, 30, 30, step)
                    initial_pattern = next_generation  # to go to the next step, but according to the speed the user has determined

                    continue
                elif menu == 3:
                    break
            break

        elif main_select == 4:
            break


if __name__ == "__main__":
    main()
