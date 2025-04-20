import random

def get_user_choice():
    choices = ['камень', 'ножницы', 'бумага']
    while True:
        user_input = input("Введите ваш выбор (камень, ножницы, бумага): ").strip().lower()
        if user_input in choices:
            return user_input
        else:
            print("Некорректный ввод. Пожалуйста, введите 'камень', 'ножницы' или 'бумага'.")

def get_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага'])

def determine_winner(user, computer):
    if user == computer:
        return 'ничья'
    elif (user == 'камень' and computer == 'ножницы') or \
         (user == 'ножницы' and computer == 'бумага') or \
         (user == 'бумага' and computer == 'камень'):
        return 'пользователь'
    else:
        return 'компьютер'

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Вы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == 'ничья':
            print("Ничья!")
        elif winner == 'пользователь':
            print("Вы выиграли этот раунд!")
            user_score += 1
        else:
            print("Победил компьютер!")
            computer_score += 1

        print(f"Счёт — Вы: {user_score}, Компьютер: {computer_score}")

        play_again = input("Хотите сыграть ещё раз? (да/нет): ").strip().lower()
        while play_again not in ['да', 'нет']:
            play_again = input("Пожалуйста, введите 'да' или 'нет': ").strip().lower()

        if play_again == 'нет':
            print("Спасибо за игру! До новых встреч!")
            break

if __name__ == "__main__":
    play_game()
