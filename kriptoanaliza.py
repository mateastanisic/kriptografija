from bigrams_freq import print_bigram_freq, bigrams
from letters_freq import print_letter_frequencies
from affine_crypto_analysis import print_affine
from cezar import print_ctext, print_ccipher
from vigener import print_cvigenere, print_cvigenere_autokey, print_vigenere_cis, print_vigenere_crypto_analysis_with_best_possibility
from playfair import print_cplayfair, print_playfair_decrypt
#from hill import print_hill_cipher

while(1):
	print("Possibilities:")
	print("A. letters frequency")
	print("B. bigrams frequency")
	print("C. affine crypto analysis")
	print("D. cezar cipher maker")
	print("E. cezar crypto analysis")
	print("F. vigenere cipher maker")
	print("G. vigenere cipher maker with autokey")
	print("H. vigenere crypto analysis -- [only best probable m] coincidence index")
	print("I. vigenere crypto analysis with coincidence index -- with most possible plain text ")
	print("J. playfair cipher maker ")
	print("K. playfair crypto analysis with known keyword")
	print("L. hill cipher maker with given keyword(matrix) ")
	print("EXIT \n")

	respond = input("""What do you want? -- type \"EXIT\",\"A\",\"B\",\"C\",\"D\"...  
""")
	if( respond == "A" or respond == "a" ):
		print_letter_frequencies(input("""Type cipher...  """))
	elif( respond == "B" or respond == "b" ):
		print_bigram_freq(input("""Type cipher...  """))
	elif( respond == "C" or respond == "c" ):
		print_affine(input("""Type cipher...  """))
	elif( respond == "EXIT" or respond == "exit" ):
		break
	elif( respond == "D" or respond == "d" ):
		print_ccipher()
	elif( respond == "E" or respond == "e" ):
		print_ctext(input("""Type cipher...  """))
	elif( respond == "F" or respond == "f" ):
		print_cvigenere()
	elif( respond == "G" or respond == "g" ):
		print_cvigenere_autokey()
	elif( respond == "H" or respond == "h" ):
		print_vigenere_cis()
	elif( respond == "I" or respond == "i" ):
		print_vigenere_crypto_analysis_with_best_possibility()
	elif( respond == "J" or respond == "j" ):
		print_cplayfair()
	elif( respond == "K" or respond == "k" ):
		print_playfair_decrypt()
	#elif( respond == "L" or respond == "l" ):
	#	print_hill_cipher() #samo iz power shella mogu pokrenuti zbog numpya
	else:
		print("Type something of proposed options!")
