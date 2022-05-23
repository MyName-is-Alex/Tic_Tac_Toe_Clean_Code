

def get_empty_board(board_lenght):
    rows = board_lenght
    columns = rows
    board = [['.'] * columns for i in range(rows)]
    return board


def display_board(board):

    each_row = chr(65)
    board_length = len(board)
    counter = 1

    print("     ", end="")
    for column_index in range(1, board_length + 1):
        print(f"   {column_index}", end="")
    print("")

    for row_index in range(board_length):

        board_row = " | ".join(board[row_index])

        print(f"    {each_row}   {board_row}\n", end="   ")
        print("    ---+---+---")

        each_row = chr(65 + counter)
        counter += 1


def is_board_full(board):
    for row in board:
        for column in row:
            if column == ".":
                return False
    return True


def check_rows(players, board, min_streak):

    board_size = len(board)

    for row in range(board_size):
        counters = [0, 0]
        for column in range(board_size):
            for player in range(len(players)):
                if board[row][column] == players[player]:
                    counters[player] += 1
                    if counters[player] >= min_streak:
                        return players[player]
                else:
                    counters[player] = 0


def check_columns(players, board, min_streak):

    board_size = len(board)

    for column in range(board_size):
        counters = [0, 0]
        for row in range(board_size):
            for player in range(len(players)):
                if board[row][column] == players[player]:
                    counters[player] += 1
                    if counters[player] >= min_streak:
                        return players[player]
                else:
                    counters[player] = 0


def check_diags(players, board, min_streak):

    diags_list = []
    board_size = len(board)
    diags_board = board_size - min_streak
    reversed_board = []
    for row in board:
        row.reverse()
        reversed_board.append(row)

    for row in range(diags_board + 1):
        for column in range(diags_board + 1):
            diag = [board[row + i][column + i] for i in range(min_streak)]
            diags_list.append(diag)

    for row in range(diags_board + 1):
        for column in range(diags_board + 1):
            diag = [reversed_board[row + i][column + i] for i in range(min_streak)]
            diags_list.append(diag)

    for player in players:
        counter = 0
        for diag in diags_list:
            for element in diag:
                if element == player:
                    counter += 1
        if counter >= min_streak:
            return player


def get_winning_player(board, min_streak, players):

    # min_streak = 3
    # players = ["X", "O"]

    # Check Rows
    winner = check_rows(players, board, min_streak)
    if winner:
        return winner
    # Check Columns
    winner = check_columns(players, board, min_streak)
    if winner:
        return winner
    # Check Diags
    winner = check_diags(players, board, min_streak)
    if winner:
        return winner

    return None


if __name__ == "__main__":
    empty_board = get_empty_board(3)
    print(empty_board)
    current_player = 'X'    # added
    winner = None           # added

    board = [
      ['X', "O", "."],
      ['X', "O", "."],
      ['0', "X", "."],
    ]

    print("""
    should print
        1   2   3
    A   X | O | .
       ---+---+---
    B   X | O | .
       ---+---+---
    C   0 | X | .
       ---+---+---
    """)

    display_board(board)

    board_1 = [
      ["X", "O", "."],
      ["X", "O", "."],
      ["X", "X", "O"],
    ]
    print("Should return False")
    print(is_board_full(board_1))

    board_2 = [
      [".", "O", "O"],
      [".", "O", "X"],
      [".", "X", "X"],
    ]
    print("Should return False")
    print(is_board_full(board_2))

    board_3 = [
      ["O", "O", "X"],
      ["O", "X", "O"],
      ["O", "X", "X"],
    ]
    print("Should return True")
    print(is_board_full(board_3))

    board_4 = [
      ["O", ".", "O", "X"],
      ["X", ".", "X", "O"],
      ["O", ".", "O", "X"],
      ["X", "O", "X", "O"]
    ]
    print("Should return X")
    print(get_winning_player(board_4))

    board_5 = [
      ["X", "O", "O"],
      ["X", "O", "."],
      ["O", "X", "X"],
    ]
    print("Should return O")
    print(get_winning_player(board_5))

    board_6 = [
      ["O", "O", "."],
      ["O", "X", "."],
      [".", "X", "."],
    ]
    print("Should return None")
    print(get_winning_player(board_6))
