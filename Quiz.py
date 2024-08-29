import random
import time

time.sleep(1)
print("Hello World!")

text = "Welcome to HangMan..."
lives = 3

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
    global lives, easy_answers, easy_ques, medium_answers, medium_ques, hard_answers, hard_ques, impossible_answers, impossible_ques
    
    while True:
        mode = input("What mode would you like to play? (easy, medium, hard or impossible): ").lower()

        questions_left = 5

        if mode == "easy":
            quest = easy_ques
            answers = easy_answers
            break
        elif mode == "medium":
            quest = medium_ques
            answers = medium_answers
            break
        elif mode == "hard":
            quest = hard_ques
            answers = hard_answers
            break
        elif mode == "impossible":
            quest = impossible_ques
            answers = impossible_answers
            questions_left = 2
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

    # Loop through questions
    for i in range(questions_left):
        if lives == 0:
            print("You're out of lives! Game Over!")
            break

        print(f"Question {i + 1}: {quest[i]}")
        guess = input("True or False: ").strip().lower().capitalize()

        if guess == str(answers[i]):
            print("Correct!")
        else:
            print("Incorrect!")
            lives -= 1
            print(f"Lives left: {lives}")

    if lives > 0:
        print("Congratulations, you completed the quiz!")

# Run the game
game()
