from letters_and_freq import letters, letters_revert, frequency_cro, frequency_cro_revert, abeceda
from letters_freq import count_letter_frequencies
from bigrams_freq import bigrams, freq_bigrams

def make_m5x5(key):
	m5x5 = []
	test = 1
	count = 0
	help_key = ''
	for i in range(0,5):
		row = []
		for j in range(0,5):
			if( test and count < len(key) ):
				while( count < len(key) and key[count] in help_key ):
					count += 1 
				if( count == len(key) ): #ako smo dosli do kraja rijeci
					test = 0
					count = 0

				help_key += key[count]
				row.append(key[count])
				count += 1
				if( count == len(key) ): #ako smo dosli do kraja rijeci
					test = 0
					count = 0
			else:
				while( count < 26 ):
					if( abeceda[count] in key or count == 22 ): #w ne gledamo
						count += 1
					else: #( abeceda[count] not in key )
						row.append( abeceda[count] )
						count += 1
						break
		m5x5.append(row)
	return m5x5

def chript(text,m5x5):
	chiper = ''
	#za svaki blok šifriraj drugi
	for i in range(0, len(text), 2):
		b1_r = 0
		b1_c = 0 
		b0_r = 0
		b0_c = 0
		block = text[i]
		if( (i+1) != len(text) and text[i+1] != block ): block += text[i+1]
		else: block += 'X'

		test = 0
		for r in range(0,5):
			for c in range(0,5):
				if( block[0] == m5x5[r][c] ):
					b0_r = r
					b0_c = c
					test += 1
				elif( block[1] == m5x5[r][c] ):
					b1_r = r
					b1_c = c
					test += 1
				if( test == 2 ): break	#nasli smo oba slova

		if( b0_r == b1_r ): #isti redak
			chiper += m5x5[b0_r][(b0_c + 1) % 5]
			chiper += m5x5[b1_r][(b1_c + 1) % 5]
		elif( b0_c == b1_c ): #isti stupac
			chiper += m5x5[(b0_r + 1) % 5][b0_c]
			chiper += m5x5[(b1_r + 1) % 5][b0_c]
		else: #inače
			chiper += m5x5[b0_r][b1_c]
			chiper += m5x5[b1_r][b0_c]				

	return chiper


def print_cplayfair():
	key = input("Type key word: ")
	text = input("Type plain text: ")

	m5x5 = make_m5x5(key)
	print("Playfair square:")
	for i in range(0,5):
		print(m5x5[i][0]," ", m5x5[i][1], " ", m5x5[i][2], " ", m5x5[i][3], " ", m5x5[i][4])
	chiper = chript(text, m5x5)
	print("Chiper: ")
	print(chiper)
	print("\n\n")

def decrypt_playfair_with_known_keyword(keyword, cipher):
	m5x5 = make_m5x5(keyword.upper())
	for i in range(0,5):
 		print(m5x5[i][0]," ", m5x5[i][1], " ", m5x5[i][2], " ", m5x5[i][3], " ", m5x5[i][4])
	plain_text = ''

	for i in range(0, len(cipher), 2):
		b1_r = 0
		b1_c = 0 
		b0_r = 0
		b0_c = 0
		block = cipher[i]
		if( (i+1) != len(cipher) ): block += cipher[i+1]
		else: print("Nije dobro!")

		test = 0
		for r in range(0,5):
			for c in range(0,5):
				if( block[0] == m5x5[r][c] ):
					b0_r = r
					b0_c = c
					test += 1
				elif( block[1] == m5x5[r][c] ):
					b1_r = r
					b1_c = c
					test += 1
				if( test == 2 ): break	#nasli smo oba slova

		if( b0_r == b1_r ): #isti redak
			if( b0_c == 0 ): plain_text += m5x5[b0_r][4]
			else: plain_text += m5x5[b0_r][ b0_c - 1 ]
			if( b1_c == 0 ): plain_text += m5x5[b0_r][4]
			else: plain_text += m5x5[b0_r][ b1_c - 1 ]			
		elif( b0_c == b1_c ): #isti stupac
			if( b0_r == 0 ): plain_text += m5x5[4][b0_c]
			else: plain_text += m5x5[ b0_r - 1 ][b0_c]
			if( b1_r == 0 ): plain_text += m5x5[4][b0_c]
			else: plain_text += m5x5[b1_r-1][b0_c]
		else: #inače
			plain_text += m5x5[b0_r][b1_c]
			plain_text += m5x5[b1_r][b0_c]				

	return plain_text

# print_cplayfair()
# m5x5 = make_m5x5("TAJNOPIS")
# for i in range(0,5):
# 	print(m5x5[i][0]," ", m5x5[i][1], " ", m5x5[i][2], " ", m5x5[i][3], " ", m5x5[i][4])
# print(chript("MATEAUCIUUCIONICINACVJETNOM",m5x5))
# input("wait")

def print_playfair_decrypt():
	key = input("Type key word: ")
	cipher = input("Type cipher: ")

	m5x5 = make_m5x5(key)
	print("Playfair square:")
	for i in range(0,5):
		print(m5x5[i][0]," ", m5x5[i][1], " ", m5x5[i][2], " ", m5x5[i][3], " ", m5x5[i][4])
	plain_text = chript(cipher, m5x5)
	print("Plain text: ")
	print(plain_text)
	print("\n\n")

#text = "BJBEDELDAHJQIJMABJPDTHSCMGDEBACMNVZTSDEGXMXGMADLBBABZTECQJGTEQDJNQQDENLHQAIPAQLTCIBAFQABKPEJPTLDEEDICMMFRLCEGBHXOSCQCEGJKXGVVHXNXMZMFSELDMFMMC"
#print(decrypt_playfair_with_known_keyword("MEDICINA",text))