score = 0
questionnum = 0

def ques(questionnum):  #function that inputs the question number and outputs the desired question
                        # updates score depending on user's answer
    global score
    if questionnum == 1:
        answer = input('Q.1 True or False. Oranges are usually the color orange.')#answer = user input to the question
        if answer.lower() == 'true':
            print('You are correct!')
            score += 1                 #if user answer is correct then add one point to the score
        elif answer.lower() == 'false':
            print('You are incorrect!')
            score += -1
        else:
            print('Oh No! Please input "True" or "False"') #if the user answer is neither a variation of true or false the question will be asked again
            return ques(questionnum)
    if questionnum == 2:
        answer = input('Q.2 True or False. Dinosaurs still exist today.')
        if answer.lower() == 'false':
            print('You are correct!')
            score += 1
        elif answer.lower() == 'true':
            print('You are incorrect!')
            score += -1
        else:
            print('Oh No! Please input "True" or "False"')
            return ques(questionnum)
    if questionnum == 3:
        answer = input('Q.3 True or False. There are 365 days in one year')
        if answer.lower() == 'true':
            print('You are correct!')
            score += 1
        elif answer.lower() == 'false':
            print('You are incorrect!')
            score += -1
        else:
            print('Oh No! Please input "True" or "False"')
            return ques(questionnum)
    if questionnum == 4:
        answer = input('Q.4 How many continents are there in the world?')
        if answer.lower() == '7':
            print('You are correct!')
            score += 1
        else:
            print('You are incorrect!')
            score += -1
    if questionnum == 5:
        answer = input('Q.5 What is 2+2 equal to')
        if answer.lower() == '4':
            print('You are correct!')
            score+=1
        else:
            print('You are incorrect!')
            score+=-1
    if questionnum == 6:
        answer = input('Q.6 How many states are in the U.S.A?')
        if answer.lower() == '50':
            print('You are correct!')
            score += 1
        else:
            print('You are incorrect!')
            score += -1
    if questionnum == 7:
        answer = input('Q.7 Which city is Batman from')
        if answer.lower() == 'gotham city':
            print('You are correct!')
            score+=1
        else:
            print('You are incorrect!')
            score+=-1
    if questionnum == 8:
        answer = input('Q.8 How many wonders of the world are there?')
        if answer.lower() == 'seven' or '7':
            print('You are correct!')
            score += 1
        else:
            print('You are incorrect!')
            score += -1
    if questionnum == 9:
        answer = input('Q.9 True or False. Venus the closest planet to earth?')
        if answer.lower() == 'true':
            print('You are correct!')
            score+=1
        elif answer.lower() == 'false':
            print('You are incorrect!')
            score+=-1
        else:
            print('Oh No! Please input "True" or "False"')
            return ques(questionnum)
    if questionnum == 10:
        answer=input('Q.10 True or False. A guitar has seven strings.')
        if answer.lower() == 'false':
            print('You are correct!')
            score+=1
        elif answer.lower() ==  'true':
            print('You are incorrect!')
            score += -1
        else:
            print('Oh No! Please input "True" or "False"')
            return ques(questionnum)
    if questionnum == 11:
        answer = input('Q.11 True or False. Is chocolate brown?')
        if answer.lower() == 'true':
            print('You are correct!')
            score+=1
        elif answer.lower() == 'false':
            print('You are incorrect!')
            score+= -1
        else:
            print('Oh No! Please input "True" or "False"')
            return ques(questionnum)
    if questionnum == 12:
        answer = input('Q.12 What is the name of the city where the cartoon family The Simpsons live?')
        if answer.lower() == 'springfield':
            print('You are correct!')
            score+=1
        else:
            print('You are incorrect!')
            score+= -1
    if questionnum == 13:
        answer = input('Q.13 What year is it?')
        if answer.lower() == '2017':
            print('You are correct!')
            score += 1
        else:
            print('You are incorrect!')
            score+= -1
    if questionnum == 14:
        answer = input('Q.14 True or false. New York is the capital of the United States.')
        if answer.lower() == 'false':
            print('You are correct!')
            score += 1
        elif answer.lower() == 'true':
            print('You are incorrect!')
            score += -1
        else:
            print('Oh No! Please input "True" or "False"')
            return ques(questionnum)
    if questionnum == 15:
        answer = input('Q.15 True or False. The color red is a color.')
        if answer.lower() == 'true':
            print("You are correct!")
            score+=1
        elif answer.lower() == 'false':
            print('You are incorrect!')
            score+= -1
        else:
            print('Oh No! Please input "True" or "False"')
            return ques(questionnum)

#intro message
print('''

________                 __      _____       .__.__      __  .__    .__         ________        .__         ________        .__
\______ \   ____   _____/  |_  _/ ____\____  |__|  |   _/  |_|  |__ |__| ______ \_____  \  __ __|__|_______ \_____  \  __ __|__|_______
 |    |  \ /  _ \ /    \   __\ \   __\\__  \ |  |  |   \   __\  |  \|  |/  ___/  /  / \  \|  |  \  \___   /  /  / \  \|  |  \  \___   /
 |    `   (  <_> )   |  \  |    |  |   / __ \|  |  |__  |  | |   Y  \  |\___ \  /   \_/.  \  |  /  |/    /  /   \_/.  \  |  /  |/    /
/_______  /\____/|___|  /__|    |__|  (____  /__|____/  |__| |___|  /__/____  > \_____\ \_/____/|__/_____ \ \_____\ \_/____/|__/_____ \
        \/            \/                   \/                     \/        \/         \__>              \/        \__>              \/

Welcome to this quiz! You will be pressed with 15 questions.
For each correct answer you will GAIN one point and for each incorrect answer you will LOOSE one point.
With a score under 70% you will fail.
Scores of 70% will be a Pass
Scores of 80% will be a Merit
Scores of 90% will be a Distinction

Good Luck!


''')
#calls the function 15 times and changes questionnum paramter to output different question
while questionnum <= 15:
    ques(questionnum)
    print('Your score is', score)
    questionnum += 1

#closing sequence
print('''

Good job! You have completed the quiz
''')
if score/questionnum >= 0.7 and score/15 <= 0.8:
    print("Good Job! You passed this quiz.")
    print("Your final score is", score)
elif score/questionnum >= 0.8 and score/15 <= 0.9:
    print("Yay! You earned a Merit.")
    print("Your final score is", score)
elif score/questionnum >=0.9:
    print("WOW! You passed this quiz with Distinction")
    print("Your final score is", score)
elif score/questionnum <=0.6:
    print("Oh No! You have not passed this quiz!")
    print("Your final score is", score)
print("Thank you for playing!")
