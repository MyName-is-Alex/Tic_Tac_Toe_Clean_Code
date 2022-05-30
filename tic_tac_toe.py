from board import display_board, get_empty_board, is_board_full, get_winning_player
from coordinates import get_human_coordinates, get_random_ai_coordinates
from menu import get_menu_option


HUMAN_VS_HUMAN = "1"
RANDOM_AI_VS_RANDOM_AI = "2"
HUMAN_VS_RANDOM_AI = "3"
HUMAN_VS_UNBEATABLE_AI = "4"


def play_again():
    while True:
        user_input = input("     Play again?(y/n): ")
        print("")
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("")
            print("     WRONG OPTION, BOY!")
            print("")


def main():

    first_player = "X"
    second_player = "O"

    menu_options = ["Human vs Human", "Random AI vs Random AI", "Human vs Random AI", "Human vs Unbeatable AI"]
    game_mode = get_menu_option(menu_options)

    board_lenght = 4
    board = get_empty_board(board_lenght)

    is_game_running = True
    current_player = "O"

    while is_game_running:

        display_board(board)

        if current_player == "O":
            current_player = "X"
        else:
            current_player = "O"

        if game_mode == HUMAN_VS_HUMAN:
            row, column = get_human_coordinates(board)
        elif game_mode == RANDOM_AI_VS_RANDOM_AI:
            row, column = get_random_ai_coordinates(board)
        elif game_mode == HUMAN_VS_RANDOM_AI:
            if current_player == first_player:
                row, column = get_human_coordinates(board)
            elif current_player == second_player:
                row, column = get_random_ai_coordinates(board)
        # elif game_mode == HUMAN_VS_UNBEATABLE_AI:
        #     if current_player == first_player:
        #         row, column = get_human_coordinates(board)
        #     elif current_player == second_player:
        #         row, column = get_unbeatable_ai_coordinates(board)

        board[row][column] = current_player

        winning_player = get_winning_player(board)
        its_a_tie = is_board_full(board)

        if its_a_tie:
            display_board(board)
            print("     It's a tie")
            if play_again():
                main()
            else:
                exit(0)

        if winning_player is not None:
            display_board(board)
            print(f"Player '{winning_player}' won the game")
            if play_again():
                main()
            else:
                exit(0)


if __name__ == "__main__":
    main()
