from letters_and_freq import letters, letters_revert, frequency_cro, frequency_cro_revert, abeceda
from letters_freq import count_letter_frequencies


def vigener_cipher(text, key, version):
	K = []
	W = []
	OUT = []

	for l in key:
		K.append(letters[l])
	for l in text:
		W.append(letters[l])

	j = 0
	test = 1
	for i in range(0,len(W)):
		if( version ):
			if(test): OUT.append( (W[i] + K[j]) % 26 )
			else: OUT.append( (W[i] + W[j]) % 26 )
		else:
			OUT.append( (W[i] + K[j]) % 26 )

		j += 1
		if( j == len(K) and( (version == 1 and test == 1 ) or version == 0) ): 
			j = 0
			test = 0

	cipher = ''
	for i in range(0, len(OUT)):
		cipher += letters_revert[OUT[i]]

	return cipher

def print_cvigenere():
	key = input("Type key word: ")
	text = input("Type plain text: ")
	print( "Cipher: ", vigener_cipher(text.upper(), key.upper(), 0) )
	print("\n\n")

def print_cvigenere_autokey():
	key = input("Type key word: ")
	text = input("Type plain text: ")
	print( "Cipher: ", vigener_cipher(text.upper(), key.upper(), 1) )
	print("\n\n")

def coincidence_index(text, m):
	if( m == 1 ):
		f = count_letter_frequencies(text)

		n = len(text)
		ic = 0
		for i in f:
			ic += ( i[1]*(i[1]-1) ) / ( n*(n-1) )
		#print(ic)
		return [ abs( 0.064 - ic ), ic ]		
	else:
		row = make_matrix_for_ic(text, m)
		dif = 0
		ics = []

		for i in range(0,m):
			texti = row[i]
			#print(texti)
			f = count_letter_frequencies(texti)

			n = len(texti)
			ic = 0
			for i in f:
				ic += ( i[1]*(i[1]-1) ) / ( n*(n-1) )
			ics.append(ic)
			#print(ic)
			dif += (0.064 - ic ) #ako je ic veći od 0.064 vjerojatnost je veća da je to dobro pa on zapravo smanjuje razliku -> dobro
		return [dif/m , ics ]

def make_matrix_for_ic(text, m):
	rows = []
	if( m == 1 ): return text
	else:
		M = []
		test = 1 
		j = 0
		for i in range(0,len(text)):
			if( test ): M.append( text[i] )
			else: M[j] += text[i]
			j += 1
			if( j == m ): 
				j = 0 
				test = 0

		for i in range(0,m):
			rows.append(M[i])

	return rows

def find_most_probable_m(cipher):
	most_probable_m = 0
	most_probable_dif = 0
	ics = []

	for m in range(3,10):
		#print("m = ", m )
		[ dif, ici ] = coincidence_index(cipher, m)
		ics.append(ici)

		if( m == 1 ): 
			most_probable_m = 1
			most_probable_dif = dif
		elif( dif< most_probable_dif ):
			most_probable_dif = dif
			most_probable_m = m

	return [most_probable_m, ics ]

def print_vigenere_cis():
	cipher = input("""Type cipher...
""")
	[ most_probable_m, ics ] = find_most_probable_m(cipher)

	print("Most probable m is: ", most_probable_m)
	for i in range(0, len(ics[most_probable_m-1])):
		print(ics[most_probable_m-1][i])
	print("\n\n")

def vigenere_decrypt(text, m):
	K = ''
	K_numerical = []
	row = make_matrix_for_ic(text, m)
	
	for j in range(0,m):
		#tražimo j-to slovo u kljućnoj riječi, odnosno njen numerički ekvivalent
		#prvo pronađemo sve Mg-ove , 0<=g<=25
		M_max = 0
		h = 0
		#j-ti redak
		if( m == 1 ): zj = text
		else: zj = row[j]
		n = len(zj)
		#print("slovo: ",j)
		#print("Mg-ovi")
		print(n)
		for g in range(0,26):
			#pomaknuti red zj za g mjesta
			zjg = ''
			for li in range(0, len(zj) ): 
				slovo = zj[li]
				num_ekvivalent = abeceda.index(slovo)
				novo_slovo = abeceda[ (num_ekvivalent + g) % 26 ]
				zjg += novo_slovo 

			#izračunamo frekvencije takvog teksta (frekvencije su sortirane)
			freq = count_letter_frequencies(zjg)

			#izračunamo takav Mg
			Mg = 0
			for ls in freq:
				#ls[0] je slovo, ls[1] je broj njegovog pojavljivanja u tekstu zjg
				Mg += (frequency_cro[ls[0]]/100)*(ls[1]) #odredo ovo
			Mg = Mg / n

			#provjerimo je li takav Mg najveći do sada
			if( Mg > M_max ): 
				M_max = Mg
				h = g

		print("najbolji g: ", h, " najbolji Mg: ", M_max)
		K_numerical.append( (26-h) % 26 )
		K += abeceda[ (26-h) % 26 ]
	return [K_numerical, K ]

def vigenere_decrypt_cipher(cipher, key):
	m = len(key)
	plain_text = ''
	j = 0

	for l in cipher:
		numerical = letters[l]
		numerical = ( numerical - key[j] )
		if( numerical < 0 ): numerical = 26 + numerical
		plain_text += letters_revert[numerical]

		j += 1
		if( j == m ): j = 0

	return plain_text

def print_vigenere_crypto_analysis_with_best_possibility():
	cipher = input("""Type cipher...
""")
	[most_probable_m, ics] = find_most_probable_m(cipher)

	[key, key_word] = vigenere_decrypt(cipher, most_probable_m)
	plain_text = vigenere_decrypt_cipher(cipher, key)
	print("Most probable m: ", most_probable_m)
	print("Key word: ", key_word)
	print("Plain text:\n", plain_text)

	print("\n\n")

# #ja sljiva
# text = "WFAWKABPDAMEVYSMHVAUNSPGGORVVMSZBBVLSKJLJVGWSVVRSKWQHVJDCIHAKTOZDKGUNAPSETBTDLALUQVRSARVDSMRDJDLAGAQEEEPCWXNAUNSJRADCQGIKFPIUAAKDKVVSYSMFUJLWI"
# #mia tadic - kivi  text = "XRDPYDJZOTDOSRNSYQNBBIUQFIIROKZQWWHWQCXQDQYITWNLOAZBVRZKSUVLYUDVSZVREAKQTCIAUWHHKRZLXQXWWSVSYAPJSTDUXWBWXIKZOLIQTQJLCDJRSPZCBWKAUQCSYTZOK"
# #mage - grejp text = "GIEYXYLMVPRZHXKUCNWDFEEWYGFWCPZZWCXIZOXYKJYXCJRSMAATMUXAGSCGOAIKXZZRJGOAILXAJZNIUAOWYOQMVJYCMVPTRGRAPZQSTHZSXIQIMCXQFNNHKIMSTIZGNHIVTXYGMPSJPLETDPZLKPYZRNBG"

# [mpm, ics ] = find_most_probable_m(text)
# print("Most probable m:", mpm)
# [k1, kw] = vigenere_decrypt(text, mpm)
# key = [18, 11, 9, 8, 21, 0] #sljiva
# plain_text = vigenere_decrypt_cipher(text, key) 
# print( plain_text )
# print("\n")

"""CIPHER = "AHNKJPJVMCJSJARZZJCNKJSJAJQPKIDRRAHIDIJHJMJIDSJIXUVSHIASVIACEIJZDJCUD
	   NVIVFJQJRYSKJNDRDXLBDXLTBRFKQEMRMJKJQJIDREDNSVLKIDVXFRZCNKJSJIYQPKVVSJS"
print(decrypt_playfair_with_known_keyword(cipher,make_m5x5("SREDNJIVIJEK")))"""