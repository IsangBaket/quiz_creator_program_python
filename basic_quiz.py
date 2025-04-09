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

print("-----WELCOME TO MY QUIZ CREATOR-----")

while True:
    question = input("Enter Question(enter e to exit): ") # asks user for question
    
    if question == 'e': # ends program 
        break

    print("Input answers for A to D") 
    choices = []
    for items in ['A', 'B', 'C', 'D']: # asks user for input for choices A to D
        answers = input(f"Choices {items}: ")
        choices.append(answers)

    correct_answer = input("letter of correct answer: ").upper() # asks user for the correct answer


    with open("max.txt", "a") as file: # saves input to external text file
        file.write(f"Question: {question}")
        file.write(f"A: {choices[0]}")
        file.write(f"B: {choices[1]}")
        file.write(f"C: {choices[2]}")
        file.write(f"D: {choices[3]}")
        file.write(f"Correct Answer: {correct_answer}")




    

