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

def convert_quiz():
    pass

def quiz():
    pass

def main():
    pass


