# 2 sample code , first code doesn't work right


# import re
# from tkinter import Tk, filedialog
# import fitz
# from langdetect import detect
# from langdetect.lang_detect_exception import LangDetectException
#
#
# def extract(pdf_path):
#     text = ''
#     with fitz.open(pdf_path) as doc:  # removed encoding argument
#         for page_num in range(doc.page_count):
#             page = doc[page_num]
#             text += page.get_text()
#     return text
#
#
# def detect_language(text):
#     try:
#         language = detect(text)
#         return language
#     except LangDetectException:
#         return None
#
#
# def process(file_path):
#     if file_path.endswith('.pdf'):
#         text = extract_text_from_pdf(file_path)
#         detected_language = detect_language(text)
#         print(f"Detected Language: {detected_language}")
#     else:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             text = file.read()
#         detected_language = detect_language(text)
#         print(f"Detected Language: {detected_language}")
#
#     clean = re.sub(r'[^\w\sآ-ی۰-۹٬،؛؟]', '', text, flags=re.UNICODE)
#     all_words = clean.split()
#
#     index = {index + 1: word for index, word in enumerate(all_words)}
#     for index, word in indexed_words.items():
#         print(f"Index {index}: {word}")
#
#     dictionary = {}
#     operation(all_words, dictionary, indexed_words)
#
#     num_rows = len(dictionary)
#     print(f"Number of rows in the index dictionary: {num_rows}")
#
#     for _ in range(3):
#         # Allow the user to insert three words expressions
#         expression = input('Type your 3-word expression... ')
#         words_to_insert = expression.split()
#         updated_text = insert_words_between(all_words, words_to_insert)
#         updated_all_words = updated_text.split()
#         updated_indexed_words = {index + 1: word for index, word in enumerate(updated_all_words)}
#         operation(updated_all_words, dictionary, updated_indexed_words)
#
#
# def insert(words, words_to_insert):
#     result = []
#     for i, word in enumerate(words):
#         result.append(word)
#         if i < len(words) - 1:
#             result.extend(words_to_insert)
#     return ' '.join(result)
#
#
# def operation(all_words, dictionary, indexed_words):
#     my_search = input('Type your K-gram sequence... ')
#     for word in all_words:
#         for i in range(len(word) - 1):
#             k_gram = word[i:i + len(my_search)]
#             if k_gram in dictionary:
#                 dictionary[k_gram].append(word)
#             else:
#                 dictionary[k_gram] = [word]
#
#     print('All the K-grams include:')
#     for k_gram, k_words in dictionary.items():
#         print(f'{k_gram} : {k_words}')
#
#     if my_search in dictionary:
#         result = dictionary[my_search]
#         print(f'Search results are | {result}')
#         ask = input('Would you like to know the exact position of the words? YES/NO ')
#         while ask.lower() not in ['yes', 'no']:
#             ask = input('Please type the correct form of the word YES/NO ')
#         if ask.lower() == 'yes':
#             search_in_indices(indexed_words, my_search)
#
#
# def search(indexed_words, my_search):
#     for index, word in indexed_words.items():
#         if my_search in word:
#             print(f'The position of your results in order | {word} : {index}')
#
#
# def indictionary(phrase_words, dictionary):
#     results = []
#     for word in phrase_words:
#         if word in dictionary:
#             results.extend(dictionary[word])
#     return list(set(results))
#
#
# if __name__ == "__main__":
#     Tk().withdraw()
#     file_paths = filedialog.askopenfilenames(title='Select PDF files', filetypes=[('PDF files', '*.pdf')])
#     for file_path in file_paths:
#         print(f"Processing file: {file_path}")
#         process_file(file_path)

import re
from tkinter import Tk, filedialog
import fitz
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException


def extracting_text(pdf_path):
    text = ''
    with fitz.open(pdf_path) as doc:
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text += page.get_text()
    return text


def choosing_language(text):
    try:
        language = detect(text)
        return language
    except LangDetectException:
        return None


def create_indexed(words):
    return {index + 1: word for index, word in enumerate(words)}


def find_indexed(indexed_words, search_phrase):
    search_words = search_phrase.split()
    indices = [index for index, word in indexed_words.items() if word in search_words]
    return indices


def insert_word(words, insert_after, words_to_insert):
    result = []
    for i in range(len(words)):
        result.append(words[i])
        if words[i:i + len(insert_after)] == insert_after:
            result.extend(words_to_insert)
    return result


def process_file(file_path):
    text = extracting_text(file_path)
    detected_language = choosing_language(text)
    print(f"Detected Language: {detected_language}")

    clean_text = re.sub(r'\W+', ' ', text)
    all_words = clean_text.split()
    indexed_words = create_indexed(all_words)


    for index, word in indexed_words.items():
        print(f"Index {index}: {word}")



    first_100_indexed_words = list(indexed_words.items())[:100]
    print(f"Indexed Words: {first_100_indexed_words}")
    num_rows = len(indexed_words)
    print(f"Number of rows in the index : {num_rows}")

    for _ in range(3):
        search_phrase = input('Enter a phrase to search: ')
        found_indices = find_indexed(indexed_words, search_phrase)
        print(f"Found at indices: {found_indices}")

        three_words = search_phrase.split()
        if len(three_words) != 3:
            print("error ,  enter exactly three words !!")
            continue

        result = find_indexed(indexed_words, search_phrase)
        print(f'Found the phrase {search_phrase} at positions: {result}')

        another_phrase = input('Enter 3 words to insert after  phrase: ').split()
        if len(another_phrase) != 3:
            print("Please enter exactly 3 words to insert.")
            continue

        updated_words = insert_word(all_words, three_words, another_phrase)
        indexed_updated_words = create_indexed(updated_words)
        print(f"Updated Indexed Words: {indexed_updated_words}")


if __name__ == "__main__":
    Tk().withdraw()
    file_paths = filedialog.askopenfilenames(title='Select PDF files', filetypes=[('PDF files', '*.pdf')])
    for file_path in file_paths:
        print(f"Processing file: {file_path}")
        process_file(file_path)

# Developed By Rashin Gholijani Farahani