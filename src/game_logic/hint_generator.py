def provide_hint(guess, actual_num):
    if guess < actual_num:
        print("Your guess is too low.")
    elif guess > actual_num:
        print("Your guess is too high.")