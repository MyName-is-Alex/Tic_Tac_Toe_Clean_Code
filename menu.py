def get_menu_option(menu_options):

    valid_input = []

    for option in menu_options:
        index = menu_options.index(option) + 1
        valid_input.append(str(index))
        print(f"{index}. {option}")

    valid_input_string = ", ".join(valid_input)

    while True:
        user_input = input(f"Choose a game mode({valid_input_string})!: ")

        if user_input in valid_input:
            return user_input
        else:
            print(f"You must type a number between {valid_input[0]} and {valid_input[-1]}")


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option(["Human vs Human", "Random AI vs Random AI", "Human vs Random AI",
                              "Human vs Unbeatable AI"])
    print("If the user selected 1, it should print 1")
    print(option)
