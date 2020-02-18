from random import randint
import math

def is_prime(x):
	for i in range( 2, math.floor( math.sqrt( x ) ) ):
		if x % i == 0:
			return False
	return True

def find_next_prime(m):
	x = m
	while(1):
		if is_prime(x):
			return x
		elif x == 9999:
			return find_next_prime(randint(1000, 9999))
		else:
			x += 1

def relative_prime(e,fi):
	for i in range( 2, min( e, fi ) + 1 ):
		if e % i == 0 and fi % i == 0:
			return False
	return True

def find_e(fi):
	if (fi-1) > 99999: 
		manji_od = 99999
	else:
		manji_od = fi - 1
	while 1:
		e = randint(10000,manji_od)
		if relative_prime(e,fi):
			return e

def find_d(e,fi):
	for d in range(1,fi):
		if (d*e) % fi == 1:
			return d
	return -1

#p = find_next_prime(randint(1000,9999))
#q = find_next_prime(randint(1000,9999))
#n = p*q
#fi = (p-1)*(q-1)
#e = find_e(fi)
#d = find_d(e,fi)

#plain_text = 112266
#cipher = plain_text**e % n 
print(relative_prime(341,329))

p = 7013
q = 8581
n = p*q
fi = (p-1)*(q-1)
e = 10679

#print(find_d(e,fi))
#print(12836790**21030839 % n)

