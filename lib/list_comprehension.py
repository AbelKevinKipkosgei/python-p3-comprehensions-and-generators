#!/usr/bin/env python3

def return_evens(num_list):
    even_list = [num for num in num_list if num % 2 == 0]
    print(even_list)
    return even_list


def make_exclamation(sentence_list):
    exclamation_list = [f"{string}!" for string in sentence_list]
    print(exclamation_list)
    return exclamation_list

return_evens([0, 1, 2, 5, 7, 9, 10])
make_exclamation(["Hello", "I'm doing great", "Python is fun"])