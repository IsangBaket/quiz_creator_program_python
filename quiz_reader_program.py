# Create the Quiz program that read the output file of the Quiz Creator. 
# The user will answer the randomly selected question and check if the answer is correct.

def file_name():    # added needed functions first
    while True:
        try:     # asks for user file name to read
            txt_file = input("file name with '.txt': ")
            if txt_file.endswith('.txt'):   # ensures that user puts file extension
                break
            with open(txt_file):
                pass
        except FileNotFoundError:
            print("File not found")
    return txt_file

def convert_quiz(txt_file):
    with open(txt_file, "r") as file:
        content = file.read()

    raw_questions = content.strip().split('------\n\n')
    quiz_data = []

    for item in raw_questions:
        lines = item.strip().split('\n')
        if len(lines) >= 6:
            question_data = {
                'question': lines[0][9:],  # remove "Question: "
                'A': lines[1][3:],         # remove "A: "
                'B': lines[2][3:],
                'C': lines[3][3:],
                'D': lines[4][3:],
                'answer': lines[5][-1].upper()  # get last character (letter of correct answer)
            }
            quiz_data.append(question_data)
    return quiz_data

def quiz():
    pass

def main():
    pass


