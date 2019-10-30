from operator import itemgetter
import sys
import math
from letters_and_freq import frequency_cro, letters

def count_letter_frequencies(text):
    frequencies = {}

    for asciicode in range(65, 91):
        frequencies[chr(asciicode)] = 0

    for letter in text:
        asciicode = ord(letter.upper())
        if asciicode >= 65 and asciicode <= 90:
            frequencies[chr(asciicode)] += 1

    sorted_by_frequency = sorted(frequencies.items(), key = itemgetter(1), reverse=True)

    return sorted_by_frequency

def print_letter_frequencies(chiper):
    text = chiper.upper()
    number_of_letters_in_text_cro = count_letter_frequencies(text)
    print("\nLetters frequency: ")
    num = 0
    for i in number_of_letters_in_text_cro:
	    print("Letter ", i[0], " is appearing ", i[1], " times in cipher." )
	    print("Therefore, frequency is: ", (i[1]*100)/len(text),"%  .\n")
	    num += 1
    print("\n\n")