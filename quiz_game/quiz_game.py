print('Welcome to Computer Quiz Game!')

response = input('Do you want to play game,Vijay ? ')
if response.lower() != 'yes':
    quit()
score = 0
print('Ok, Lets play the game..')

answer = input("What does CPU stands for ? ")
if answer.lower() == 'central processing unit':
    print('Correct!')
    score += 10
else:
    print('Incorrect')

answer = input("What does HDD stands for ? ")
if answer.lower() == 'hybrid disk drive':
    print('Correct!')
    score += 10
else:
    print('Incorrect')

answer = input("What does SSD stands for ? ")
if answer.lower() == 'solid state drive':
    print('Correct!')
    score += 10
else:
    print('Incorrect')

answer = input("What does RAM stands for ? ")
if answer.lower() == 'random access memory':
    print('Correct!')
    score += 10
else:
    print('Incorrect')

answer = input("What does GPU stands for ? ")
if answer.lower() == 'graphics processing unit':
    print('Correct!')
    score += 10
else:
    print('Incorrect')

answer = input("What does FTP stands for ? ")
if answer.lower() == 'file transfer protocol':
    print('Correct!')
    score += 10
else:
    print('Incorrect')

print("Your total score is : "+str(score))
print("Your success percentage is "+str((score/60)*100))
