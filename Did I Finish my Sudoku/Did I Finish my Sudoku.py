#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

def done_or_not(board): #board[i][j]
    valid_board = "Finished!"

    print_board(board)

    #Check each row
    ##print("Rows:")
    for y in range(0,9):
        ##print(board[y])
        if not check_set(board[y]):
            valid_board = "Try again!"
            break

    #Check each column
    ##print("\nColumns:")
    for x in range(0,9):
        column = []
        for y in range(0,9):
            column.append(board[y][x])
        ##print(column)
        if not check_set(column):
            valid_board = "Try again!"
            break

    #Check each section
    ##print("\nSections:")
    #Find each 3x3 section
    for x in range(0,3):
        for y in range(0,3):
            section = []
            #Add each number in section to list
            for a in range(0,3):
                for b in range(0,3):
                    section.append(board[(3*x)+a][(3*y)+b])
            ##print(section)
            if not check_set(section):
                valid_board = "Try again!"
                break

    # for x in range(0,9,3):
    #     section = []
    #     for y in range(0,9,3):
    #         section.append(board[x][y:y+3])

    return valid_board

def check_set(set):
    valid_list = [1,2,3,4,5,6,7,8,9]
    return sorted(set) == valid_list

def print_board(board):
    for x in range(0,9):
        for y in range(0,9):
            print(board[x][y], end='')
        print("")

board1 = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
    ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
    ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
    ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
    ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
    ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
    ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
    ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
    ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]

done_or_not(board1)
