import random

def lst_fill_text(lst_text):
    content = ''
    with open('./data/answer_text.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if line == '----\n':
                lst_text.append(content)
                content = ''
            else:
                content += line


def lst_fill_photo(lst_photo):
    with open('./data/answer_photo_link.txt', 'r', encoding='utf-8') as f:
        for line in f:
            lst_photo.append(line)