from letters_and_freq import frequency_cro, letters
abeceda ='abcdefghijklmnopqrstuvwxyz'.upper()

def print_ccipher():
	key = input("""Type key...  """)
	plain_text = input("""Type text...  """)
	text = plain_text.upper()
	cipher = ''

	for l in text:
		try:
			i = ( abeceda.index(l) + int(key) ) % 26
			cipher += abeceda[i]
		except ValueError:
			cipher += l

	print("Cipher:", cipher.upper() )
	print("\n\n")

def cezar_with_known_key(k, cipher):
	""" Dešifriranje šifrata. Vraća otvoreni tekst. """
	text = '' 
	for l in cipher:
		try:
			i = ( abeceda.index(l) - k ) % 26
			text += abeceda[i]
		except ValueError:
			text += l
	return text

def print_ctext(cipher):
	""" Dešifriranje šifrata bez znanja ključa. [BRUTE FORCE] Vraća otvoreni tekst. """
	rezultati = []

	print("All possible results: ")
	for i in range(0,26):
		print("With K=", i, " the plain text is: ", cezar_with_known_key(i, cipher) )

	print("\n\n")