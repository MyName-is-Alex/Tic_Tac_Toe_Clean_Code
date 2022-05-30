def get_human_coordinates(board):

    row_index = 0
    column_index = 1
    board_length = len(board)

    while True:
        try:
            user_input = input("Please insert the coordinates!: ").lower()
            row = ord(user_input[row_index]) - 97
            column = int(user_input[column_index]) - 1

            if user_input.lower() == "quit":
                exit(0)
            if len(user_input) != 2:
                print("Please insert a valid input! (Eg: a1): ")
            if row > board_length-1 or column > board_length-1:
                print("Out of range!: ")
            else:
                if board[row][column] != ".":
                    print("Position allready taken!: ")
                else:
                    return row, column
        except ValueError:
            print("Column must be a number!: ")
        except IndexError:
            print("Row must be a letter!: ")


def get_random_ai_coordinates(board):
    for row in board:
        for column in row:
            if column == ".":
                return tuple((board.index(row), row.index(column)))
    return None


# def get_unbeatable_ai_coordinates(board, current_player):
#     # Try to win
#     for row in board:
#         if row[0] == current_player and row[1] == current_player and row[2] == ".":
#             return (board.index(row), 2)
#         if row[1] == current_player and row[2] == current_player and row[0] == ".":
#             return (board.index(row), 0)
#         if row[0] == current_player and row[2] == current_player and row[1] == ".":
#             return (board.index(row), 1)
#     for i in range(len(board)):
#         if board[0][i] == current_player and board[1][i] == current_player and board[2][i] == ".":
#             return (2, i)
#         if board[1][i] == current_player and board[2][i] == current_player and board[0][i] == ".":
#             return(0, i)
#         if board[0][i] == current_player and board[2][i] == current_player and board[1][i] == ".":
#             return(1, i)
#     if board[0][0] == current_player and board[1][1] == current_player and board[2][2] == ".":
#         return(2, 2)
#     if board[0][2] == current_player and board[1][1] == current_player and board[2][0] == ".":
#         return(2, 0)
#     if board[0][0] == current_player and board[2][2] == current_player and board[1][1] == ".":
#         return(1, 1)
#     if board[1][1] == current_player and board[2][2] == current_player and board[0][0] == ".":
#         return(0, 0)
#     if board[2][0] == current_player and board[1][1] == current_player and board[0][2] == ".":
#         return(0, 2)
#     if board[0][2] == current_player and board[2][0] == current_player and board[1][1] == ".":
#         return(1, 1)

#     # Try not to lose
#     prev_player = "O" if current_player == "X" else "X"
#     for row in board:
#         if row[0] == prev_player and row[1] == prev_player and row[2] == ".":
#             return (board.index(row), 2)
#         if row[1] == prev_player and row[2] == prev_player and row[0] == ".":
#             return (board.index(row), 0)
#         if row[0] == prev_player and row[2] == prev_player and row[1] == ".":
#             return (board.index(row), 1)
#     for i in range(len(board)):
#         if board[0][i] == prev_player and board[1][i] == prev_player and board[2][i] == ".":
#             return (2, i)
#         if board[1][i] == prev_player and board[2][i] == prev_player and board[0][i] == ".":
#             return(0, i)
#         if board[0][i] == prev_player and board[2][i] == prev_player and board[1][i] == ".":
#             return(1, i)

#     if board[0][0] == prev_player and board[1][1] == prev_player and board[2][2] == ".":
#         return(2, 2)
#     if board[0][2] == prev_player and board[1][1] == prev_player and board[2][0] == ".":
#         return(2, 0)
#     if board[0][0] == prev_player and board[2][2] == prev_player and board[1][1] == ".":
#         return(1, 1)
#     if board[1][1] == prev_player and board[2][2] == prev_player and board[0][0] == ".":
#         return(0, 0)
#     if board[2][0] == prev_player and board[1][1] == prev_player and board[0][2] == ".":
#         return(0, 2)
#     if board[0][2] == prev_player and board[2][0] == prev_player and board[1][1] == ".":
#         return(1, 1)

#     if board[1][1] == ".":
#         return(1, 1)

#     if board[1][1] == "X" and current_player == "O":
#         for row in board:
#             for column in row:
#                 if column == ".":
#                     return tuple((board.index(row), row.index(column)))

#     for i in range(len(board)):
#         if board[1][i] == ".":
#             return tuple((1, i))

#     for row in board:
#         for column in row:
#             if column == ".":
#                 return tuple((board.index(row), row.index(column)))

#     return None


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

    # board_3 = [
    #   ["O", "X", "X"],
    #   ["X", "O", "X"],
    #   ["X", "O", "X"],
    # ]
    # print("The printed coordinate should be None")
    # print(get_random_ai_coordinates(board_3))

    # board_4 = [
    #   [".", "O", "O"],
    #   ["X", "O", "."],
    #   ["X", "X", "O"],
    # ]
    # print("The printed coordinate should always be (0, 0)")
    # print(get_unbeatable_ai_coordinates(board_4))

    # board_5 = [
    #   ["X", "O", "."],
    #   ["X", ".", "."],
    #   ["O", "O", "X"],
    # ]
    # print("The printed coordinate should always be (1, 1)")
    # print(get_unbeatable_ai_coordinates(board_5))

    # board_6 = [
    #   ["O", "O", "."],
    #   ["O", "X", "."],
    #   [".", "X", "."],
    # ]
    # print("The printed coordinate should either (0, 2) or (2, 0)")
    # print(get_unbeatable_ai_coordinates(board_6))
