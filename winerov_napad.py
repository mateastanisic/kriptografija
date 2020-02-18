import math

def verizni(n,e):
	verizni = [ 0 ]
	while 1:
		b = math.floor(n/e)
		r = n % e 

		if r == 0: 
			return verizni

		verizni.append(b)

		n = e
		e = r

n = 16299067
e = 1253149	
verizni = verizni(n,e)
print(verizni)

def konvergente(a):
	konvergente = []
	konvergente.append([a[0], 1])
	konvergente.append([a[0]*a[1] + 1, a[1]])

	for k in range(2, len(a)):
		pk = a[k] * konvergente[k-1][0] + konvergente[k-2][0]
		qk = a[k] * konvergente[k-1][1] + konvergente[k-2][1]
		konvergente.append([pk, qk])

	return konvergente


konvergente = konvergente(verizni)


def wiener( konvergente, x, n, e):
	for razlomak in konvergente:
		nazivnik = razlomak[1]
		if x**(e*nazivnik) % n == x: return nazivnik

	return -1


print(wiener(konvergente,2,n,e))