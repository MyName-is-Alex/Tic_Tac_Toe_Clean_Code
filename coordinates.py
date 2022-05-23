def get_human_coordinates(board, current_player):
    valid_input_row = {"A": 0, "B": 1, "C": 2}
    valid_input_column = {"1": 0, "2": 1, "3": 2}

    while True:
        user_input = input("Please insert the coordinates!: ")
        if user_input.lower() == "quit":
            exit(0)
        if len(user_input) == 2 and user_input[0].upper() in valid_input_row\
           and user_input[1] in valid_input_column:
            row = valid_input_row[user_input[0].upper()]
            column = valid_input_column[user_input[1]]
            position = (row, column)
            if board[position[0]][position[1]] == ".":
                return position
            else:
                print("Position already taken!: ")
        else:
            print("Invalid input")


def get_random_ai_coordinates(board, current_player):
    for row in board:
        for column in row:
            if column == ".":
                return tuple((board.index(row), row.index(column)))
    return None


def get_unbeatable_ai_coordinates(board, current_player):
    # Try to win
    for row in board:
        if row[0] == current_player and row[1] == current_player and row[2] == ".":
            return (board.index(row), 2)
        if row[1] == current_player and row[2] == current_player and row[0] == ".":
            return (board.index(row), 0)
        if row[0] == current_player and row[2] == current_player and row[1] == ".":
            return (board.index(row), 1)
    for i in range(len(board)):
        if board[0][i] == current_player and board[1][i] == current_player and board[2][i] == ".":
            return (2, i)
        if board[1][i] == current_player and board[2][i] == current_player and board[0][i] == ".":
            return(0, i)
        if board[0][i] == current_player and board[2][i] == current_player and board[1][i] == ".":
            return(1, i)
    if board[0][0] == current_player and board[1][1] == current_player and board[2][2] == ".":
        return(2, 2)
    if board[0][2] == current_player and board[1][1] == current_player and board[2][0] == ".":
        return(2, 0)
    if board[0][0] == current_player and board[2][2] == current_player and board[1][1] == ".":
        return(1, 1)
    if board[1][1] == current_player and board[2][2] == current_player and board[0][0] == ".":
        return(0, 0)
    if board[2][0] == current_player and board[1][1] == current_player and board[0][2] == ".":
        return(0, 2)
    if board[0][2] == current_player and board[2][0] == current_player and board[1][1] == ".":
        return(1, 1)

    # Try not to lose
    prev_player = "O" if current_player == "X" else "X"
    for row in board:
        if row[0] == prev_player and row[1] == prev_player and row[2] == ".":
            return (board.index(row), 2)
        if row[1] == prev_player and row[2] == prev_player and row[0] == ".":
            return (board.index(row), 0)
        if row[0] == prev_player and row[2] == prev_player and row[1] == ".":
            return (board.index(row), 1)
    for i in range(len(board)):
        if board[0][i] == prev_player and board[1][i] == prev_player and board[2][i] == ".":
            return (2, i)
        if board[1][i] == prev_player and board[2][i] == prev_player and board[0][i] == ".":
            return(0, i)
        if board[0][i] == prev_player and board[2][i] == prev_player and board[1][i] == ".":
            return(1, i)

    if board[0][0] == prev_player and board[1][1] == prev_player and board[2][2] == ".":
        return(2, 2)
    if board[0][2] == prev_player and board[1][1] == prev_player and board[2][0] == ".":
        return(2, 0)
    if board[0][0] == prev_player and board[2][2] == prev_player and board[1][1] == ".":
        return(1, 1)
    if board[1][1] == prev_player and board[2][2] == prev_player and board[0][0] == ".":
        return(0, 0)
    if board[2][0] == prev_player and board[1][1] == prev_player and board[0][2] == ".":
        return(0, 2)
    if board[0][2] == prev_player and board[2][0] == prev_player and board[1][1] == ".":
        return(1, 1)

    if board[1][1] == ".":
        return(1, 1)

    if board[1][1] == "X" and current_player == "O":
        for row in board:
            for column in row:
                if column == ".":
                    return tuple((board.index(row), row.index(column)))

    for i in range(len(board)):
        if board[1][i] == ".":
            return tuple((1, i))

    for row in board:
        for column in row:
            if column == ".":
                return tuple((board.index(row), row.index(column)))

    return None


# run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
    board_1 = [
      ["X", "X", "."],
      ["X", ".", "."],
      ["X", "X", "."],
    ]
    print("It should print the coordinates selected by the human player")
    coordinates = get_human_coordinates(board_1)
    print(coordinates)

    board_2 = [
      ["O", "O", "."],
      ["X", "O", "."],
      ["X", "X", "O"],
    ]
    print("The printed coordinate should be only (0,2) or (1,2)")
    print(get_random_ai_coordinates(board_2))
    print("The printed coordinate should be only (0,2) or (1,2)")
    print(get_random_ai_coordinates(board_2))
    print("The printed coordinate should be only (0,2) or (1,2)")
    print(get_random_ai_coordinates(board_2))

    board_3 = [
      ["O", "X", "X"],
      ["X", "O", "X"],
      ["X", "O", "X"],
    ]
    print("The printed coordinate should be None")
    print(get_random_ai_coordinates(board_3))

    board_4 = [
      [".", "O", "O"],
      ["X", "O", "."],
      ["X", "X", "O"],
    ]
    print("The printed coordinate should always be (0, 0)")
    print(get_unbeatable_ai_coordinates(board_4))

    board_5 = [
      ["X", "O", "."],
      ["X", ".", "."],
      ["O", "O", "X"],
    ]
    print("The printed coordinate should always be (1, 1)")
    print(get_unbeatable_ai_coordinates(board_5))

    board_6 = [
      ["O", "O", "."],
      ["O", "X", "."],
      [".", "X", "."],
    ]
    print("The printed coordinate should either (0, 2) or (2, 0)")
    print(get_unbeatable_ai_coordinates(board_6))
