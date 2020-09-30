# This program creates a quiz game based of the Nickelodeon show SpongeBob SquarePants
import random
question1 = '''What were the first words spoken by SpongeBob in the series?" 
               a. "Are ya’ ready, kids?"
               b. "I’m ready!"
               c. "Aye-aye, captain!"
               d. "May I take your order?"
            '''

question2 = '''What object is the Krusty Krab (Spongebob’s place of work) building?
               a. A wooden crate
               b. A barrel
               c. A lobster trap
               d. A fish bowl
            '''

question3 = '''How many tentacles does Squidward the octopus have?
               a. 6
               b. 8
               c. 10
               d. 7
            '''

question4 = '''What is the name of the fish in Spongebob who usually yells “My leg!” whenever chaos ensues in the show?
               a. Fred
               b. Dave
               c. Jim
               d. Craig
            '''

question5 = '''What are the names of Patrick Star’s parents?
               a. Marty and Janet Star
               b. Herb and Margie Star
               c. Manny and Jenine Star
               d. Herbert and Denice Star
            '''

question6 = '''How are Gary the snail and Patrick Star related?
               a. They are brothers-in-law
               b. They are cousins
               c. Gary is Patrick’s legal nephew
               d. Patrick is Gary’s father
            '''

question7 = '''The undersea superhero Mermaid Man has a belt with the letter “M” that can also be turned to be the letter “W”. What does the “W” stand for?"
               a. Wonder
               b. Wumbo
               c. Wavy
               d. Wowza
            '''

question8 = '''What is the nationality of the narrator that introduces many of the episodes and reads the time cards?
               a. Australian
               b. British
               c. American
               d. French
            '''

question9 = '''What drink did Spongebob and Squidward forget to bring a customer in the “Pizza Delivery” episode?
               a. A Kelp Shake
               b. A Diet Dr. Kelp
               c. A Diet Bikini Fizz
               d. A Krusty Pop
            '''

question10 = '''In the episode “Mermaid Man and Barnacle Boy V” where Spongebob and his friends become superheroes, what was Sandy Cheeks’ power?
                a. Invisibility
                b. To stretch her body to incredible lengths
                c. Heat ray vision
                d. Super speed
            '''

question11 = '''In the episode “Life of Crime”, in which SpongeBob and Patrick decide to leave town, what crime did they believe they had committed? (in reality they were innocent)
                a. They stole a chocolate bar
                b. They trespassed
                c. They stole a balloon
                d. They hit someone while driving
            '''

question12 = '''In the episode “Clams,” what lipstick is spongebob shown wearing?
                a. Sea Green #6 semi-gloss lipstick
                b. Jellyfish Pink #4 semi-gloss lipstick
                c. Beach Coconut #3 semi-gloss lipstick
                d. Coral Blue #2 semi-gloss lipstick
            '''

def getScore(num):
    print("Your score is: " + str(num))
    if num >= 11:
        print("You did AMAZING! You're an honorary bubble buddy. :)")
    elif num == 10 or num == 9:
        print("You did great! You seem to know a lot about SpongeBob and his pals.")
    elif num == 8 or num == 7:
        print("That's pretty good, but I'm sure you can do even better!")
    elif num == 6 or num == 5:
        print("Eh, not so bad boyo. I'm a little impressed.")
    elif num == 4 or num == 3:
        print("C'mon I know you can do better!")
    else:
        print("Wow, you belong in Weenie Hut Jr's. You really don't know much about the yellow sponge. :(")




def createQuestions(list):
    score = 0
    questionNum = 0
    for i in list:
        questionNum += 1
        print("QUESTION " + str(questionNum) + " :")
        if i == question1:
            print(i)
            answer = "d"
            userAnswer = input("Enter the correct letter: ")
            userAnswer.lower()
            if answer == userAnswer:
                print("That's Correct!")
                print("You gained one point.")
                score += 1
            else:
                print("Sorry, the correct answer is 'd': 'May I take your order?'")
            print(" ")

        elif i == question2:
            print(i)
            answer = "c"
            userAnswer = input("Enter the correct letter: ")
            userAnswer.lower()
            if answer == userAnswer:
                print("That's Correct!")
                print("You gained one point.")
                score += 1
            else:
                print("Sorry, the correct answer is 'c': A lobster trap")
            print(" ")

        elif i == question3:
            print(i)
            answer = "a"
            userAnswer = input("Enter the correct letter: ")
            userAnswer.lower()
            if answer == userAnswer:
                print("That's Correct!")
                print("You gained one point.")
                score += 1
            else:
                print("Sorry, the correct answer is 'a': 6")
            print(" ")


        elif i == question4:
            print(i)
            answer = "a"
            userAnswer = input("Enter the correct Letter: ")
            userAnswer.lower()
            if answer == userAnswer:
                print("That's Correct!")
                print("You gained one point.")
                score += 1
            else:
                print("Sorry, the correct answer is 'a': Fred")
            print(" ")

        elif i == question5:
            print(i)
            answer = "b"
            userAnswer = input("Enter the correct Letter: ")
            userAnswer.lower()
            if answer == userAnswer:
                print("That's Correct!")
                print("You gained one point.")
                score += 1
            else:
                print("Sorry, the correct answer is 'b': Herb and Margie Star")
            print(" ")

        elif i == question6:
            print(i)
            answer = "b"
            userAnswer = input("Enter the correct Letter: ")
            userAnswer.lower()
            if answer == userAnswer:
                print("That's Correct!")
                print("You gained one point.")
                score += 1
            else:
                print("Sorry, the correct answer is 'b': They are cousins")
            print(" ")

        elif i == question7:
            print(i)
            answer = "b"
            userAnswer = input("Enter the correct Letter: ")
            userAnswer.lower()
            if answer == userAnswer:
                print("That's Correct!")
                print("You gained one point.")
                score += 1
            else:
                print("Sorry, the correct answer is 'b': Wumbo")
            print(" ")

        elif i == question8:
            print(i)
            answer = "d"
            userAnswer = input("Enter the correct Letter: ")
            userAnswer.lower()
            if answer == userAnswer:
                print("That's Correct!")
                print("You gained one point.")
                score += 1
            else:
                print("Sorry, the correct answer is 'd': French")
            print(" ")

        elif i == question9:
            print(i)
            answer = "b"
            userAnswer = input("Enter the correct Letter: ")
            userAnswer.lower()
            if answer == userAnswer:
                print("That's Correct!")
                print("You gained one point.")
                score += 1
            else:
                print("Sorry, the correct answer is 'b': A Diet Dr. Kelp")
            print(" ")

        elif i == question10:
            print(i)
            answer = "a"
            userAnswer = input("Enter the correct Letter: ")
            userAnswer.lower()
            if answer == userAnswer:
                print("That's Correct!")
                print("You gained one point.")
                score += 1
            else:
                print("Sorry, the correct answer is 'a': Invisibilty")
            print(" ")

        elif i == question11:
            print(i)
            answer = "c"
            userAnswer = input("Enter the correct Letter: ")
            userAnswer.lower()
            if answer == userAnswer:
                print("That's Correct!")
                print("You gained one point.")
                score += 1
            else:
                print("Sorry, the correct answer is 'c': They stole a balloon")
            print(" ")

        else:
            print(i)
            answer = "d"
            userAnswer = input("Enter the correct Letter: ")
            userAnswer.lower()
            if answer == userAnswer:
                print("That's Correct!")
                print("You gained one point.")
                score += 1
            else:
                print("Sorry, the correct answer is 'd': Coral Blue #2 semi-gloss lipstick")
            print(" ")

    getScore(score)

def start():
    questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9,
                 question10, question11, question12]
    random.shuffle(questions)
    createQuestions(questions)


print('''SPONGEBOB SQUAREPANTS QUIZ GAME:
        Put your knowledge about the yellow sponge to the test!    
''')
play = input("Would you like to play? (Y/N) ")
play.upper()

while play == "Y":
        start()
        play = input("Would you like to play again? (Y/N) ")
        play.upper()
        print(" ")
