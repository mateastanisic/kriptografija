import numpy as np
from letters_freq import count_letter_frequencies 
abeceda ='abcdefghijklmnopqrstuvwxyz'.upper()

c1 = "SXFITSH"
c2 = "VRZSKUM"
#počinju sa jedinom od slova S, P, N, D


def guess_letter():
	c1 = input("Šifrat 1: ")
	c2 = input("Šifrat 2: ")
	cipher = input("Šifrat 1 ili 2? ")
	n = input("Koje po redu slovo? ")
	letter = input("Želiš izmjeniti sa ")

	if( cipher == 1 ):
		#c1[n] je slovo koje zelimo izmjeniti
		redni_br = abeceda.index(c2[n]) - abeceda.index(c1[n])
		if(redni_br<0): redni_br = 26 + redni_br
		redni_br = redni_br + abeceda.index(letter)
		c2[n] = 
		c1[n] = letter
	elif( cipher == 2 ):
