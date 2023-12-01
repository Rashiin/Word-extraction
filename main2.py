from tkinter import Tk,filedialog
import re
Tk().withdraw()
txt_file = filedialog.askopenfilename()
with open(txt_file, 'r') as file:
    txt = file.read()
    clean=re.sub(r'[^a-zA-Z\s]','',txt.lower())
    all_words=clean.split()
#
#
# # word_indices = {word: index for index, word in enumerate(all_words)}
# #
# # for word, index in word_indices.items():
# #     print(f"{word}: {index}")
#
# indexed_rows = {index + 1: row.strip() for index, row in enumerate(txt_rows)}
#
# for index, row in indexed_rows.items():
#     print(f"Row {index}: {row}")
#
# file_path = 'D:/123.txt'

# Open the file and read lines
with open(txt_file, 'r') as file:
    rows = file.readlines()

# Assign indices to each row
indexed_rows = {index + 1: row.strip() for index, row in enumerate(rows)}

# Print indexed rows
for index, row in indexed_rows.items():
    print(f"Row {index}: {row}")

dictionary={}
yes_list=['yes','Yes','y','YES']
no_list=['no', 'No','n','NO']

def operation(all_words):
    my_search=input('type your K-gram sequence... ')
    for word in all_words:
        for i in range(len(word)-1):
            k_gram=word[i:i+len(my_search)]
            if k_gram in dictionary:
                dictionary[k_gram].append(word)
            else:
                dictionary[k_gram]= [word]
    print('all the k-grams include: ')
    for k_gram, k_words in dictionary.items():
        print(f'{k_gram} : {k_words}')
    if my_search in dictionary:
        result = dictionary[my_search]
        print(f'search results are | {result}')
        ask = input('would you like to know the exact position of the words? YES/NO')
        while ask not in yes_list and ask not in no_list:
            ask=input('please type the correct form of the word YES/NO')
        if ask in yes_list:
            for index, x_word in enumerate(all_words):
                if my_search in x_word:
                    print(f'the position of your results in  order | {x_word} : {index}')
        elif ask in no_list:
            return None

operation(all_words)