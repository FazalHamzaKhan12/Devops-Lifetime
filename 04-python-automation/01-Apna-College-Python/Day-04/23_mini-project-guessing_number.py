import random

def play_game():
    lucky_num = random.randint(1,50)

    while True:
        user_num = int(input("Guess the lucky Number: "))

        if user_num == lucky_num:
            print("you won the game")
            break
        elif user_num > lucky_num:
            print("too high")
        else:
            print("too low")

    print("thanks For playing the game")


play_game()