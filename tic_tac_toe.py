from board import display_board, get_empty_board, is_board_full, get_winning_player
from coordinates import get_human_coordinates, get_random_ai_coordinates, get_unbeatable_ai_coordinates
from menu import get_menu_option


HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4


def play_again(game_function):
    while True:
        user_input = input("     Play again?(y/n): ")
        print("")
        if user_input == "y":
            return game_function()
        elif user_input == "n":
            exit(0)
        else:
            print("")
            print("     WRONG OPTION, BOY!")
            print("")


def main():
    game_mode = get_menu_option()
    board = get_empty_board()
    is_game_running = True
    current_player = "O"
    while is_game_running:
        display_board(board)

        if current_player == "O":
            current_player = "X"
        else:
            current_player = "O"

        try:
            if game_mode == "1":
                x, y = get_human_coordinates(board, current_player)
            elif game_mode == "2":
                x, y = get_random_ai_coordinates(board, current_player)
            elif game_mode == "3":
                if current_player == "X":
                    x, y = get_human_coordinates(board, current_player)
                elif current_player == "O":
                    x, y = get_random_ai_coordinates(board, current_player)
            elif game_mode == "4":
                if current_player == "X":
                    x, y = get_human_coordinates(board, current_player)
                elif current_player == "O":
                    x, y = get_unbeatable_ai_coordinates(board, current_player)
        except TypeError:
            continue

        board[x][y] = current_player

        winning_player = get_winning_player(board)
        its_a_tie = is_board_full(board)
        if its_a_tie:
            display_board(board)
            print("     It's a tie")
            play_again(main)
            break

        if winning_player is not None:
            display_board(board)
            print(f"Player '{winning_player}' won the game")
            play_again(main)
            break


if __name__ == "__main__":
    main()
