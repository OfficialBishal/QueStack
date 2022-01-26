import os
import utils
import PyPDF2

input_path = 'inputs/'
pdfs_path = 'inputs/book/'


def PDFmerge(pdfs, output):

    print("-"*100, "\n[INFO]Merging the pdfs...")

    # creating pdf file merger object
    pdfMerger = PyPDF2.PdfFileMerger()

    # appending pdfs one by one
    for pdf in pdfs:
        pdfMerger.append(f"{pdfs_path}{pdf}")

    # writing combined pdf to output pdf file
    with open(output, 'wb') as f:
        pdfMerger.write(f)

    print("[INFO]Merge Successful")


def merge_pdf():

    # pdf files to merges
    pdfs = [''] * utils.count_files(pdfs_path)
    pdfs = [file_name for file_name in os.listdir(pdfs_path)]
    pdfs.sort()     # Sort the file_name list in ascending order

    # output pdf file name
    output = 'inputs/book.pdf'

    # calling pdf merge function
    PDFmerge(pdfs=pdfs, output=output)


def pdf_to_text(page):

    # creating a pdf file object
    pdfFileObj = open(f'{input_path}book.pdf', 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file
    # print("Total number of pages: ", pdfReader.numPages)

    text = ""

    # creating a page object
    pageObj = pdfReader.getPage(page)

    # extracting text from page
    text += pageObj.extractText()

    # closing the pdf file object
    pdfFileObj.close()

    return text


def filter(text):

    # Convert everything to lowercase
    text = text.lower()

    # Get rid of unwanted symbols
    chars_to_remove = '.,:()-|'
    text = text.translate(str.maketrans('', '', chars_to_remove))

    # Get rid of unwanted words
    chars = ['a', 'an', 'the', 'by', 'is', 'as', 'with', 'and']
    for character in chars:
        text = text.replace(f" {character} ", " ")

    # Get rid of single character
    text = ' '.join([w for w in text.split() if len(w) > 1])

    # Get rid of all the duplicate whitespaces and newline characters.
    text = " ".join(text.split())

    # Get rid of duplicate words
    text = ' '.join(dict.fromkeys(text.split()))

    return text


def extract_keywords():

    print("-"*100, "\n[INFO]Extracting keywords from book.pdf...")

    num_chapters = int(input("Enter the number of Chapters: "))
    keywords = [''] * num_chapters
    start_page_no = [''] * num_chapters
    end_page_no = [''] * num_chapters

    for i in range(num_chapters):
        start_page_no[i] = input(f"Starting page no. of Chapter {i+1}: ")
        end_page_no[i] = input(f"Ending page no. of Chapter {i+1}: ")

    for i in range(num_chapters):
        keywords_collected = ''
        for page in range(int(start_page_no[i]), (int(end_page_no[i])+1), 1):
            keywords_temp = ''
            keywords_temp = pdf_to_text(page)
            keywords_temp = filter(keywords_temp)
            keywords_collected += keywords_temp
        keywords[i] = keywords_collected

    # Converting list to string
    keywords_final = '\n'.join([str(elem) for elem in keywords])

    # Saving the keywords
    with open(f"{input_path}keywords.txt", mode='w') as file:
        file.write(keywords_final)
    print(
        f'[INFO]Extraction Successful: Book({input_path}book.pdf) -> keywords({input_path}keywords.txt)')


def extract_questions():
    print("-"*100, "\n[INFO]Extracting questions from question.pdf...")


def main():

    if utils.count_files(pdfs_path) != 0:
        merge_pdf()

    extract_keywords()
    extract_questions()


if __name__ == "__main__":
    # calling the function
    utils.clearConsole()
    main()
