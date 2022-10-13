import random

def dead_state(width, height):
        board_state = [[0]*width for i in range(height)]
        return board_state

def random_state(width, height):
    board_state = dead_state(width, height)

    def cellState():
        random_number = random.random()
        if random_number >= 0.5:
            cell_state = 0
        else:
            cell_state = 1
        return cell_state

    for row in board_state:
        for i in range(len(row)):
            row[i] += cellState()
    return board_state

def render(board_state):
    width = len(board_state[0])
    height = len(board_state)
    rendered_state = dead_state(width, height)
    for x in range(0, height):
        for y in range(0, width):
            current_cell = board_state[x][y]
            if current_cell == 1:
                rendered_state[x][y] = '+'
            else:
                rendered_state[x][y] = ' '
    rows = ''
    lines = '-' + ('-'* width) + '-'
    for row in rendered_state:
        row = '|' + ''.join(row) + '| '+'\n'
        rows += row
    rendered_state = lines + '\n' + rows + lines
    return print(rendered_state)

def next_board_state(initial_state):
    width = len(initial_state[0])
    height = len(initial_state)
    new_state = dead_state(width, height)
    for x in range(0, height):
        for y in range(0, width):
            current_cell = initial_state[x][y]
            neighbors = [initial_state[(x-1)%height][(y-1)%width], initial_state[x][(y-1)%width], 
            initial_state[(x+1)%height][(y-1)%width], initial_state[(x-1)%height][y], 
            initial_state[(x+1)%height][y], initial_state[(x-1)%height][(y+1)%width], 
            initial_state[x][(y+1)%width], initial_state[(x+1)%height][(y+1)%width]]
            neighbor_count = sum(neighbors)
            if current_cell == 0 and neighbor_count == 3:
                new_state[x][y] = 1
            if current_cell == 1 and (neighbor_count == 2 or neighbor_count == 3):
                new_state[x][y] = 1     
    return new_state

def runGame(width, height):
        start = random_state(width, height)
        board = next_board_state(start)
        while True:
            board = next_board_state(board)
            render(board)

runGame(312,83)
#(312,83) fits cmd in fullcreen