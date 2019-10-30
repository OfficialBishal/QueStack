import image_phase

image_path = 'images/'
document_path = 'document/'

# image_phase.rename_files()
# image_phase.count_files()
# image_phase.convert_images_to_text()


#           Handling Keywords

fhandle = open(f'{document_path}keywords.txt')
original_keywords = fhandle.read()
count_chapters = len(open(f'{document_path}keywords.txt').readlines())
fhandle.close()

print("-" * 200)
print(f"Total Number of Chapters: {count_chapters}")
# print("-"*200)
print("List of Chapters & their Keywords: ")
# print("-"*200)
keywords_lines = original_keywords.split("\n")
keywords_words = original_keywords.split("\n")
i = 0
while i < count_chapters:
    keywords_words[i] = keywords_words[i].split()
    # print(f"{i+1}. {keywords_words[i]}")
    i += 1

#           Handling Questions

fhandle = open(f'{document_path}scannedquestion.txt')
original_questions = fhandle.read()
count_questions = len(open(f'{document_path}scannedquestion.txt').readlines())
fhandle.close()

print("-" * 200)
print(f"Total Number of Lines: {count_questions}")
print("List of Questions: ")
questions_lines = original_questions.split("\n")
questions_words = original_questions.split("\n")
i = 0
while i < count_questions:
    questions_words[i] = questions_words[i].split()
    # print(f"{i+1}. {questions_words[i]}")
    i += 1
print("-" * 200)

i = 0
while i < count_questions:
    match_point = [0] * count_chapters
    j = 0
    while j < count_chapters:
        count_keywords_words = len(keywords_words[j])
        k = 0
        while k < count_keywords_words:
            if questions_lines[i].count(keywords_words[j][k]) != 0:
                match_point[j] += questions_lines[i].count(keywords_words[j][k])
            k += 1
        print(match_point)
        j += 1
    max_value = max(match_point)
    i += 1



