import random

def get_random_letter(letters, counts=None):
    if counts is None:
        counts = [1]*len(letters)
    letter_list = ""
    for i in range(len(letters)):
        letter = letters[i]
        count = counts[i]
        for j in range(count):  
            letter_list = letter_list+letter
    l = random.choice(letter_list)
    return l

def get_vowel():
    vowels = "AEIOU"
    vowel_counts = [ 15, 21, 13, 13, 5 ]
    v = get_random_letter(vowels, vowel_counts)
    return v

def get_consonant():
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    consonant_counts = [ 2,3,6,2,3,2,1,1,5,4,8,4,1,9,9,9,1,1,1,1,1 ]
    c = get_random_letter(consonants, consonant_counts)
    return c

if __name__ == "__main__":
    print(get_random_letter("ABC",[3,2,1])) 