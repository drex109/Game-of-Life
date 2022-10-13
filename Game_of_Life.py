import random
import time
import os

#create function to generate dead board state full of 0's/dead cells
def dead_state(width, height):
        board_state = [[0]*width for i in range(height)]
        return board_state

#create function to generate random board state using dead state function
def random_state(width, height):
    board_state = dead_state(width, height)

    #create function for generating random number for the cell state
    def cellState():
        random_number = random.random()
        if random_number >= 0.5:
            cell_state = 0
        else:
            cell_state = 1
        return cell_state

    #replacing each cell with random number using cell state function/ 1 is alive 0 is dead
    for row in board_state:
        for i in range(len(row)):
            row[i] += cellState()
    return board_state

def loaded_state(file):
    #open file and make it readable to other functions
    with open(os.path.join('GameOfLife','patterns',file)) as f:
        load_state = []
        for i in f.readlines():
            for x in i.split():
                load_state.append([int(n) for n in x])
    return load_state


def render(board_state):
    #define empty board to use for rendering without causing int vs str errors in final loop
    width = len(board_state[0])
    height = len(board_state)
    rendered_state = dead_state(width, height)
    #replacing numbers for dead/alive with symbols
    for x in range(0, height):
        for y in range(0, width):
            current_cell = board_state[x][y]
            if current_cell == 1:
                rendered_state[x][y] = '+'
            else:
                rendered_state[x][y] = ' '
    
    #creating 'render' of the grid passed by the board_state argument
    rows = ''
    lines = '-' + ('-'* width) + '-'
    for row in rendered_state:
        row = '|' + ''.join(row) + '| '+'\n'
        rows += row
    rendered_state = lines + '\n' + rows + lines
    return print(rendered_state)

def next_board_state(initial_state):
    #define dimensions and create fresh board to use for new state
    width = len(initial_state[0])
    height = len(initial_state)
    new_state = dead_state(width, height)
    #loop through the board to find each cell
    for x in range(0, height):
        for y in range(0, width):
            current_cell = initial_state[x][y]
            #define and add up all the neighbors #with modulus operator for wrapping
            neighbors = [initial_state[(x-1)%height][(y-1)%width], initial_state[x][(y-1)%width], 
            initial_state[(x+1)%height][(y-1)%width], initial_state[(x-1)%height][y], 
            initial_state[(x+1)%height][y], initial_state[(x-1)%height][(y+1)%width], 
            initial_state[x][(y+1)%width], initial_state[(x+1)%height][(y+1)%width]]
            neighbor_count = sum(neighbors)
            #use neighbor count against ruleset
            if current_cell == 0 and neighbor_count == 3:
                new_state[x][y] = 1
            if current_cell == 1 and (neighbor_count == 2 or neighbor_count == 3):
                new_state[x][y] = 1     
    return new_state

def day_and_night_next_board_state(initial_state):
    #define dimensions and create fresh board to use for new state
    width = len(initial_state[0])
    height = len(initial_state)
    new_state = dead_state(width, height)
    #loop through the board to find each cell
    for x in range(0, height):
        for y in range(0, width):
            current_cell = initial_state[x][y]
            #define and add up all the neighbors #with modulus operator for wrapping
            neighbors = [initial_state[(x-1)%height][(y-1)%width], initial_state[x][(y-1)%width], 
            initial_state[(x+1)%height][(y-1)%width], initial_state[(x-1)%height][y], 
            initial_state[(x+1)%height][y], initial_state[(x-1)%height][(y+1)%width], 
            initial_state[x][(y+1)%width], initial_state[(x+1)%height][(y+1)%width]]
            neighbor_count = sum(neighbors)
            #use neighbor count against ruleset
            if current_cell == 0 and (neighbor_count == 3 or neighbor_count == 6 or neighbor_count == 7 or neighbor_count == 8):
                new_state[x][y] = 1   
            if current_cell == 1 and (neighbor_count == 3 or neighbor_count == 4 or neighbor_count == 6 or neighbor_count == 7):
                new_state[x][y] = 1
    return new_state

#this function was used to fiddle around with rule changes
def other_next_board_state(initial_state):
    #define dimensions and create fresh board to use for new state
    width = len(initial_state[0])
    height = len(initial_state)
    new_state = dead_state(width, height)
    #loop through the board to find each cell
    for x in range(0, height):
        for y in range(0, width):
            current_cell = initial_state[x][y]
            #define and add up all the neighbors #with modulus operator for wrapping
            neighbors = [initial_state[(x-1)%height][(y-1)%width], initial_state[x][(y-1)%width], 
            initial_state[(x+1)%height][(y-1)%width], initial_state[(x-1)%height][y], 
            initial_state[(x+1)%height][y], initial_state[(x-1)%height][(y+1)%width], 
            initial_state[x][(y+1)%width], initial_state[(x+1)%height][(y+1)%width]]
            neighbor_count = sum(neighbors)
            #use neighbor count against ruleset
            if current_cell == 0 and (neighbor_count == 3):
                new_state[x][y] = 1   
            if current_cell == 1 and (neighbor_count == 0 or neighbor_count == 1 or neighbor_count == 2 or neighbor_count == 3 or neighbor_count == 4 or neighbor_count == 5 or neighbor_count == 6 or neighbor_count == 7 or neighbor_count == 8):
                new_state[x][y] = 1
    return new_state   

def runGame():
    user_input1 = input('Please choose one \n -1- random soup \n -2- load pattern \n')
    if user_input1 == '2':
        user_inputL = input('Choose a pattern \n -1- Toad \n -2- Gosper Glider Gun \n -3- Pulsar \n')
        
        if user_inputL == '1':
            start = loaded_state('toad.txt')
            board = next_board_state(start)
            while True:
                board = next_board_state(board)
                render(board)
                time.sleep(.3)
        
        if user_inputL == '2':
            start = loaded_state('GGG.txt')
            board = next_board_state(start)
            while True:
                board = next_board_state(board)
                render(board)
                time.sleep(.2)
        
        if user_inputL == '3':
            start = loaded_state('pulsar.txt')
            board = next_board_state(start)
            while True:
                board = next_board_state(board)
                render(board)
                time.sleep(.4)
        
        else:
            print('ERROR:Please enter a 1, 2, or 3')


    if user_input1 == '1':
        start = random_state(312,83)
        board = next_board_state(start)
        while True:
            board = next_board_state(board)
            render(board)
    
    else:
        print('ERROR: Please enter a 1 or 2')

runGame()

#terminal in fullcreen (312,83)
#Conway -b3s23-
#Day and Night -b3678s34678-
#High Life -b36s23-
#Life Without Death -b3s012345678-
#Seeds -b2-
#??? -b36s237