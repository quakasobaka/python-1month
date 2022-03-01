some_list = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
             'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
def num_trans(num_word):
    return some_list.get(num_word)