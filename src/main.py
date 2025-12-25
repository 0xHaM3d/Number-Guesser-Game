from utils.input_validator import get_valid_input
from game_logic.number_generator import generate_random_number
from game_logic.hint_generator import provide_hint

def main():
    score = 100
    actual_num = int(generate_random_number(1, 100))  

    while True:
        user_input = get_valid_input(1, 100)
        if user_input == actual_num:
            print("Congratulations, You gussed the number correctly")
            print(f"Your score is {score}")
            break
        else:
           provide_hint(user_input, actual_num)
           score -= 10
           score = max(score, 0)



if __name__ == '__main__':
    main()



