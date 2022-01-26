import image_phase
import utils
import pdf_processing

image_path = 'images/'
input_path = 'inputs/'
output_path = 'outputs/'


def image_phase_processing():
    image_phase.rename_files()
    image_phase.count_files()
    image_phase.convert_images_to_text()    # Need to work on it (Not Finalized)


#           Handling Keywords       -       Assuming keywords.txt is derived from book
def handle_keywords():
    global count_chapters, keywords_words
    fhandle = open(f'{input_path}keywords.txt')
    original_keywords = fhandle.read()
    count_chapters = len(open(f'{input_path}keywords.txt').readlines())
    fhandle.close()

    print("-" * 100)
    print(f"Total Number of Chapters: {count_chapters}")
    # print("-"*100)
    print("List of Chapters & their Keywords: ")
    # print("-"*100)
    keywords_lines = original_keywords.split("\n")
    keywords_words = original_keywords.split("\n")
    i = 0
    while i < count_chapters:
        keywords_words[i] = keywords_words[i].split()
        # converting to lower case
        keywords_words[i] = [element.lower() for element in keywords_words[i]]
        print(f"{i+1}. {keywords_words[i]}")
        i += 1


#           Handling Questions
def handle_questions():
    global count_chapters, keywords_words, questions_lines, result
    fhandle = open(f'{input_path}scannedquestion.txt')
    original_questions = fhandle.read()
    count_questions = len(
        open(f'{input_path}scannedquestion.txt').readlines())
    fhandle.close()

    print("-" * 100)
    print(f"Total Number of Question Lines: {count_questions}")
    print("List of Questions: ")
    questions_lines = original_questions.split("\n")
    questions_words = original_questions.split("\n")
    questions_lines_temp = []
    questions_lines_temp = questions_lines.copy()
    questions_lines_temp = [element.lower()
                            for element in questions_lines_temp]
    i = 0
    while i < count_questions:
        questions_words[i] = questions_words[i].split()
        print(f"{i+1}. {questions_words[i]}")
        i += 1
    print("-" * 100)

    i = 0
    result = [0] * count_questions
    while i < count_questions:                      # Questions List, i
        match_point = [0] * count_chapters
        j = 0
        while j < count_chapters:                   # Chapters List, j
            count_keywords_words = len(keywords_words[j])
            k = 0
            while k < count_keywords_words:         # Keywords Word, k
                if questions_lines_temp[i].count(keywords_words[j][k]) != 0:
                    # questions_lines_temp[i].count(keywords_words[j][k])
                    match_point[j] += 1
                k += 1
            j += 1
        print(f'{i+1}. {match_point}')
        max_value = max(match_point)
        result[i] = match_point.index(max_value)
        i += 1
    print(f"Result: {result}")


#           Saving Sorted Questions to respective chapter file name
def save_questions():
    global count_chapters, keywords_words, questions_lines, result
    print("[INFO] Saving Sorted Questions")
    list_chapters = [*range(0, count_chapters, 1)]
    for i in list_chapters:
        f = open(f"{output_path}/Chapter{i+1}.txt", "w+")
        for j in range(len(result)):
            if (i == result[j]):
                # print(f"chapter: {i}, result index: {j}, question:{result[j]}")
                f.write(f"{questions_lines[j]}\r\n")
        f.close()


if __name__ == '__main__':
    utils.clearConsole()
    print("WELCOME TO QUESTACK\n"+"-"*20)
    print("A program that automatically organizes questions from your question bank according to it's respective chapters that it belongs to using our scoring algorithm.")
    print("-" * 100)
    print("ReadMe:\n[File iNFO]"
          "\n - 'inputs/keywords.txt': Keywords are seperated by single space in each line representing keywords of the chapter in ascending order."
          "\n\tEvery line represents single chapter in ascending order."
          "\n - 'inputs/scannedquestion.txt': Every line represents a single question."
          "\n[Mode iNFO]"
          "\nThere are two modes you can work on: Manual Mode & Automatic Mode."
          "\nIn Manual Mode, you need to manually prepare 'inputs/keywords.txt' and 'inputs/scannedquestion.txt'"
          "\nIn Automatic Mode, insert the book as 'inputs/book.pdf' and question bank as 'inputs/question.pdf'."
          "\n\tYou will also need to mention page intervals of every chapters of the book.")
    mode = input("Enter your choice:\n1. Manual Mode\n2. Automatic Mode\n-> ")
    if (mode == '1'):
        print("-" * 100 + "\nManual Mode")
        handle_keywords()
        handle_questions()
        save_questions()
    elif (mode == '2'):
        print("-" * 100 + "\Automatic Mode")
        pdf_processing.main()
        handle_keywords()
        handle_questions()
        save_questions()
