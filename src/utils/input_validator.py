def get_valid_input(start, end):
    while True:

        try:
            user_input = int(input("Please enter a number: "))
            if start <= user_input <= end:
                return user_input
            else:
                print(f"Please enter a valid number between {start} and {end}")
                continue
        except ValueError:
            print("Invalid input, Please enter a valid number.")
            continue


if __name__ == '__main__':
    print(get_valid_input(1, 100))