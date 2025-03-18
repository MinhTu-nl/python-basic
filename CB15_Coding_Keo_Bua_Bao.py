'''
#GAME: KÉO - BÚA - BAO
'''
import random as r
def get_choice(choice):
    if choice == 'K':
        return 'KÉO'
    elif choice == 'Đ':
        return 'ĐẤM'
    elif choice == 'L':
        return 'LÁ'
    else:
        return 'NOT A VAIL CHOICE !'

def main():
    print('WELCOME TO ĐẤM LÁ KÉO GAME !! ')
    print('[K] :: KÉO')
    print('[Đ] :: ĐẤM')
    print('[L] :: LÁ ')
    print('[Q] :: OUT GAME')

    choices = ['K', 'Đ', 'L']
    counter = 1
    turn_on = True

    while turn_on:
        your_choice =input(f'Game #{counter}. ENTER YOUR CHOICE: ')
        your_choice = your_choice.upper()

        if your_choice == 'Q':
            print('Thanks for joinning !')
            turn_on = False
        else:
            random_index = r.randint(0, 2)
            bot_choice = choices[random_index]

            print(f'Your [{get_choice(your_choice)}] vs Bot [{get_choice(bot_choice)}]')

        #Winning Rules:
        #your win:
        if your_choice == 'K' and bot_choice == 'L':
            print('YOU WIN !')
        elif your_choice == 'Đ' and bot_choice == 'K':
            print('YOU WIN !')
        elif your_choice == 'L' and bot_choice == 'Đ':
            print('YOU WIN !')
        #bot win:
        if your_choice == 'Đ' and bot_choice == 'L':
            print('BOT WIN !')
        elif your_choice == 'L' and bot_choice == 'K':
            print('BOT WIN !')
        elif your_choice == 'K' and bot_choice == 'Đ':
            print('BOT WIN !')
        #BOT = YOUR = WIN:
        elif your_choice == bot_choice:
            print(f'WOW ! It is a DRAW. Bot and You selected [{get_choice(your_choice)}]')
        else:
            print('Invalid option: Please enter [Đ, L, K or Q] only')

        counter += 1
        print('_'*40)    
 

if __name__ == '__main__':
    main()