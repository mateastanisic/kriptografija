from operator import itemgetter
import sys
import math
from letters_and_freq import frequency_cro, letters
from letters_freq import count_letter_frequencies

# Extended Euclidean Algorithm for finding modular inverse 
# eg: modinv(7, 26) = 15 
def egcd(a, b): 
	x,y, u,v = 0,1, 1,0
	while a != 0: 
		q, r = b//a, b%a 
		m, n = x-u*q, y-v*q 
		b,a, x,y, u,v = a,r, u,v, m,n 
	gcd = b 
	return gcd, x, y 
  
def modinv(a, m): 
	gcd, x, y = egcd(a, m) 
	if gcd != 1: 
		return None  # modular inverse does not exist 
	else: 
		return x % m

def congr_equation_mod_26(x1, y1, x2, y2):
	""" Solving congruent linear equation ax + b congr y (mod 26)
		we assume (a,26) = 1
		x1, x2 are letters we assume it needs to be, and y1, y2 are letters that are in cipher
		we need at least two equations to get the correct answer
	"""
	a = [1,3,5,7,9,11,15,17,19,21,23,25]
	for i in a:
		for j in range(0,25):
			#b can be 0,1,2,...,25
			result1 = (i*x1 + j) % 26
			result2 = (i*x2 + j) % 26
			if ( result1 == y1 and result2 == y2 ): 
				return [i,j]

	return -1


def affine_decryption_with_known_key(text, a, b):
	plaintext = ''.join([ chr((( modinv(a, 26)*(ord(c) - ord('A') - b))  % 26) + ord('A')) for c in text ])
	return plaintext

def try_croatian(number_of_letters_in_text,cipher, alfa):
	print("Croatian frequency!")
	i = 0
	while(i<24): #for any letters in freq +-2% print possibilities
		inpt = input("Press ""c""  to continue guessing!")
		if inpt == 'c' or inpt == 'C':
			letter1 = number_of_letters_in_text[i][0]
			freq1 = (number_of_letters_in_text[i][1]*100)/len(cipher)
			letter2 = number_of_letters_in_text[i+1][0]
			freq2 = (number_of_letters_in_text[i+1][1]*100)/len(cipher)
			for l in frequency_cro:
				if  freq1 > ( frequency_cro[l[0]] - alfa ) or  freq1 < ( frequency_cro[l[0]] + alfa ) :
					for k in frequency_cro:
						if (k != l) and ( freq2 > ( frequency_cro[k[0]] - alfa ) or freq2 < ( frequency_cro[k[0]] + alfa ) ):
							#probaj sa ovom zamjenom letter1 -> l[0]
							x1 = letters[l[0]]
							y1 = letters[letter1]
							x2 = letters[k[0]]
							y2 = letters[letter2]
							result = congr_equation_mod_26(x1, y1, x2, y2)
							if result != -1:
								print("\n", letter1, "->", l[0], " && ", letter2, "->", k[0] )
								print("K=(", result[0],",",result[1],").")
								print( affine_decryption_with_known_key(cipher,result[0], result[1]))
		else:
			break


def print_affine(cipher):
	text = cipher.upper()
	number_of_letters_in_text_cro = count_letter_frequencies(text)
	try_croatian( number_of_letters_in_text_cro, text, 0.5 )
	print("\n\n")
