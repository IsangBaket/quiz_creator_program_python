# For Assignment 9: Quiz Creator
# Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. 
# Write the collected data to a text file. Ask another question until the user chose to exit.

# loop that asks users for input for answers and questions until stop
# save those inputs to another text file

# while True
# ask user for question
# ask user for answers a to d
# ask user for correct answer
# ask user if he likes to continue
#   if user does not like to continue
#       break
# 
# save questions and answers
# figure out how to save them to a text file (probably gonna import some modules arono)
# 
# run quiz
# program an answer checker
# 
# ask user if he wants to make another quiz
# 
# end

# asks user for inputs
while True:
    question = input("Enter Question: ")
    print("Choices A to D")
    A = input("A. ")
    B= input("B. ")
    C = input("C. ")
    D = input("D. ")
    correct_answer = input("letter of correct answer: ").upper()
    cont = input("Do you wish to continue? y or n: ")

    quiz_data = {
        question,
        A,
        B,
        C,
        D,
    }


    if cont == "n":
        print(quiz_data)
        break
    

