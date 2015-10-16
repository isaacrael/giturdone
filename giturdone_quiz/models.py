from django.db import models

# Create your models here.

"""
__author__ = '184766'
""" The following program quizzes the computer user on the python programming language.
"""

from questionanswer import question_answer
import random
#from colorama import init
#from colorama import Fore, Back

#init()


questions = list(question_answer.keys())
question = random.choice(questions)

#print(Fore.RED + 'some red text')

name = raw_input("Please enter your name")
print"\n******************************************** Welcome to Python Quiz",(name) + " ***************************"
print("\n")


motivationalText = ["Awesome Keep It Up!", "Great Job!!!", "Yeah Buddy :>)", "Just Do It!", "Your Kickin Ass Dude!",
                    "Don't Get Mad Get Even!", "Teach These Monkey's A Lesson", "I'm Coming For You Beeacchhes!",
                    "A Fire Has Been Lit That Will Never Be Extinguished!"]



while True:
    question = random.choice(questions)
    answer = question_answer[question]
    user_answer = raw_input(question)
# Creates a random number so that a different motivationalText message is displayed when a correct answer is given
    for x in range(1):
        value = random.randint(1,5)
#        print(value)
    if user_answer == answer:
        print("\n")
        print(motivationalText[value])
        print("\n")
    elif user_answer == "quit":
        print"\n********************************** Thank you for using Python Quiz", (name) + " *******************Bye For Now!!"
        break
    else:
        print("Wrong! ... The correct answer is ", answer)


"""

