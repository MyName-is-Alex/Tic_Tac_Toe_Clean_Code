def get_menu_option():
    print("1. Human vs Human \n2. Random AI vs Random AI \n3. Human vs Random AI \n4. Human vs Unbeatable AI")

    valid_input = ["1", "2", "3", "4"]

    while True:
        user_input = input("Choose a game mode(1, 2, 3, 4)!: ")

        if user_input in valid_input:
            return user_input
        else:
            print("You must type a number between 1 and 4")


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print("If the user selected 1, it should print 1")
    print(option)
