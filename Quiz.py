import random
import time

time.sleep(1)
print("Hello World!")

text = "Welcome to QuizTime..."
lives = 3
timesplayed = 0
roundslost = 0
roundswon = 0
anscor = 0
answro = 0

# Easy questions and answers
easy_ques = [
    "The capital of Italy is Rome.",
    "Humans have five senses.",
    "The sun rises in the west.",
    "Water freezes at 0 degrees Celsius.",
    "A triangle has four sides."
]

easy_answers = [True, True, False, True, False]

# Medium questions and answers
medium_ques = [
    "Mount Everest is the tallest mountain in the world.",
    "Sharks are mammals.",
    "Light travels faster than sound.",
    "Mercury is the hottest planet in the solar system.",
    "Venus is the second planet from the Sun."
]

medium_answers = [True, False, True, False, True]

# Hard questions and answers
hard_ques = [
    "The Great Wall of China is visible from space with the naked eye.",
    "Albert Einstein won the Nobel Prize in Physics for his theory of relativity.",
    "There are more stars in the Milky Way galaxy than grains of sand on Earth.",
    "Humans share 50% of their DNA with bananas.",
    "The atomic number of carbon is 6."
]

hard_answers = [False, False, False, True, True]

# Impossible questions and answers
impossible_ques = [
    "The number Pi (π) can be accurately written as a fraction.",
    "A human can survive in the vacuum of space unprotected for more than 2 minutes."
]

impossible_answers = [False, False]

def game():
    global lives, anscor, answro, roundslost, roundswon, timesplayed, easy_answers, easy_ques, medium_answers, medium_ques, hard_answers, hard_ques, impossible_answers, impossible_ques
    
    while True:
        mode = input("What mode would you like to play? (easy, medium, hard or impossible): ").lower()

        if mode == "easy":
            quest = easy_ques
            answers = easy_answers
            questions_left = len(easy_ques)
            break
        elif mode == "medium":
            quest = medium_ques
            answers = medium_answers
            questions_left = len(medium_ques)
            break
        elif mode == "hard":
            quest = hard_ques
            answers = hard_answers
            questions_left = len(hard_ques)
            break
        elif mode == "impossible":
            quest = impossible_ques
            answers = impossible_answers
            questions_left = len(impossible_ques)
            break
        else:
            print("Invalid mode. Please choose again.")

    print("We are going to start in...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("GO!")

    timesplayed += 1
    lives = 3  # Reset lives to 3 for each game
    questions_answered = 0

    # Loop through questions
    for i in range(questions_left):
        if lives == 0:
            print("You're out of lives! Game Over!")
            roundslost += 1
            break

        print(f"Question {i + 1}: {quest[i]}")
        guess = input("True or False: ").strip().capitalize()

        # Ensure guess is correctly compared with answers
        if (guess == "True" and answers[i]) or (guess == "False" and not answers[i]):
            anscor += 1
            print("Correct!")
        else:
            print("Incorrect!")
            answro += 1
            lives -= 1
            print(f"Lives left: {lives}")

        questions_answered += 1

    if questions_answered == questions_left and lives > 0:
        print("Congratulations, you completed the quiz!")
        roundswon += 1
    elif lives == 3:
        print("WOW!!!! You got 0 questions wrong.")
        roundswon += 1

# Welcome message
time.sleep(1)
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.1)

print("\n")
time.sleep(1)
print(" The aim of the game is to: ")
time.sleep(1)
print("1. Answer questions based on difficulty.")
time.sleep(1)
print("2. Gain points for each correct answer.")
time.sleep(1)
print("3. When you close the game, via the end screen, get your very own 'score' document.")
time.sleep(1)
print("\nLet's Play...")

# Main loop to play again
while True:
    game()
    
    with open("Scores.txt", "w") as file:
        file.write("Thank you for playing Quiz Time:\n")
        file.write("You can look at more projects like this on my GitHub profile:\n")
        file.write("\nhttps://github.com/hippogriff101\n\n")
        file.write("Thank you to arcade for the opportunity to advance my coding knowledge.\n")
        file.write("Find this on the repo called 'quiz_time'.\n\n")
        file.write(f"Scores:\nTimes Played: {timesplayed}\nRounds Won: {roundswon}\nRounds Lost: {roundslost}\n")
        file.write(f"Questions Correct: {anscor}\nQuestions Wrong: {answro}\n")

    print("\n")
    playagain = input("Do you want to play again? (yes/no): ").lower()

    if playagain == "yes":
        continue
    elif playagain == "no":
        print("Thanks for playing!")
        print("\n")
        break
    else:
        print("Sorry, what's that?")
