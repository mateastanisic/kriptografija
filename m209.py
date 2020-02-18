import numpy as np
abeceda ='abcdefghijklmnopqrstuvwxyz'.upper()

M = [ [0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1], [1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0], 
	  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,1,1,1,1,1], 
	  [0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0]]

# v = [0,1,0,1,1,0]
# rezultat = np.dot(v,M) 
# print(rezultat)

# broj = 0
# for i in range(len(rezultat)):
# 	if( rezultat[i] != 0 ): broj += 1

# print(broj)

figura = [ [0,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,1,0,0], 
		   [0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0], 
		   [0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0], 
		   [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,0], 
		   [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], 
		   [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1] ]

def broj_bodova(v):
	rezultat = np.dot(v,M) 
	broj = 0
	for i in range(len(rezultat)):
		if( rezultat[i] != 0 ): broj += 1
	return broj

cipher = "ZZPXZAEZAMZYLHYY"
plain_text = ''
for i in range(len(cipher)):
	v = np.empty(6)
	for j in range(6):
		v[j] = figura[j][i]
	#print(v)
	hi = broj_bodova(v)
	#print(hi)
	yi = hi - abeceda.index(cipher[i]) - 1
	if( yi < 0 ): yi = 26 + yi
	#print(yi)
	yi = yi % 26
	plain_text += abeceda[yi]

print(plain_text)