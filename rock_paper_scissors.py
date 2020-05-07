import random
winning_choice = {'scissors': ['paper'], 'paper': ['rock'], 'rock': ['scissors']}
name = input('Enter your name: ')
print('Hello, {}'.format(name))
current_rating = 0
f = open('rating.txt')
for line in f:
    name_with_score = line.split()
    if name_with_score[0] == name:
        current_rating = int(name_with_score[1])
options = input().split(',')
default_options = ['scissors', 'paper', 'rock']
if not options[0]:
    options = default_options[:]
print("Okay, let's start")
while True:
    user_choice = input()
    if user_choice == '!exit':
        break
    computer_choice = random.choice(options)
    
    if user_choice == '!rating':
        print('Your rating: {}'.format(current_rating))
        continue
    
    if user_choice not in options:
        print('Invalid input')
        continue
    if options != default_options:
        user_choice_ind = options.index(user_choice)
        computer_choice_ind = options.index(computer_choice)
        winning_choice[user_choice] = options[user_choice_ind + 1:] + options[:user_choice_ind]
        winning_choice[user_choice] = winning_choice[user_choice][len(winning_choice[user_choice]) // 2:]
    if computer_choice == user_choice:
        print('There is a draw ({})'.format(user_choice))
        current_rating += 50
    elif computer_choice in winning_choice[user_choice]:
        print('Well done. Computer chose {} and failed'.format(computer_choice))
        current_rating += 100
    else:
        print('Sorry, but computer chose {}'.format(computer_choice))

print('Bye!')


