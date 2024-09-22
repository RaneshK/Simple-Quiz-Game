# Practice making a quiz game

# Import the random libary in python to be able to give the player a random quiz question
import random

# Add the quiz questions and answers to a dictionary
quizQuestionsAndAnswers = {
    "Which country has the highest life expectancy?": "Hong Kong",
    "What is the most common surname in the United States?": "Smith",
    "How many minutes are in a full week?": "10,080",
    "How many dots apperar on a pair of dice?": "42",
    "What is the worlds largest retailer? ": "Walmart"
}

def quizGame():
    # Give the player a random question

    # Get a random question with it's corrosponding answer
    question, answer = random.choice(list(quizQuestionsAndAnswers.items()))

    # Give the player a random question
    print(question)
    # Get the user's answer to the question
    playerAnswer = input()
    # Chek if the player got the question right or not
    if playerAnswer == answer:
        # The user has got the question corret
        print("Well done 🎉, that is the right answer")
    else:
        # The player got the answer wrong
        print("Sorry that is not the right answer")




def quizGameLoop():
    while True:
        # Give the player a random question

        # Get a random question with it's corrosponding answer
        question, answer = random.choice(list(quizQuestionsAndAnswers.items()))

        # Give the player a question to answer
        print(question)

        # Get the player's answer to the given question
        playerAnswer = input()

        if playerAnswer == "q":
            # Quit the game
            print("Thanks for playing 😁")
            break
        elif playerAnswer == answer:
            # The player got the answer correct
            print("Well done 🎉, that is the right answer")
            print("Here's another question for you")
        else:
            # The player got the answer wrong
            print("Sorry that is not the right answer")
            print("Try another question")
            # Get another random quiz question to give the player
            question, answer = random.choice(list(quizQuestionsAndAnswers.items()))
            print(question)

quizGameLoop()