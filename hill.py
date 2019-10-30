import numpy as np
from letters_and_freq import abeceda
from numpy.linalg import inv, matrix_rank
from itertools import starmap
from operator import mul

multiplikativni_inverzi = { 1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 15: 7, 17: 23, 19: 11, 21: 5, 23:17, 25:25 }

def getMatrixMinor(M,i,j):
    return [row[:j] + row[j+1:] for row in (M[:i]+M[i+1:])]

def getMatrixDeternminant(M, m):
    #base case for 2x2 matrix
    if m == 2:
        return M[0,0]*M[1,1]-M[0,1]*M[1,0]

    determinant = 0
    for c in range(m):
        determinant += ((-1)**c)*M[0,c]*getMatrixDeternminant(getMatrixMinor(M,0,c))
    return determinant

def getMatrixInverse(M, m):
    determinant = getMatrixDeternminant(M, m)
    determinant = determinant % 26
    determinant = multiplikativni_inverzi[determinant]
    #special case for 2x2 matrix:
    if m == 2:
        a1 = ( M[1,1]*determinant ) % 26
        a2 = (-1*M[0,1]*determinant) % 26
        a3 = (-1*M[1,0]*determinant) % 26
        a4 = ( M[0,0]*determinant ) % 26
        if( a1<0 ): a1 = 26+a1
        if( a2<0 ): a2 = 26+a2
        if( a3<0 ): a3 = 26+a3
        if( a4<0 ): a4 = 26+a4
        return np.array( [[ a1, a2  ],[ a3, a4 ]])

    #find matrix of cofactors
    #treba updejtati za m>=3
    cofactors = np.array((m,m))
    for r in range(m):
        for c in range(m):
            minor = getMatrixMinor(M,r,c)
            M[r,c] = ((-1)**(r+c)) * getMatrixDeternminant(minor)
    matr = np.asmatrix(cofactors)        
    matr2 = matr.T
    for r in range(m):
        for c in range(m):
            matr2[r,c] = matr2[r,c]/determinant
    return matr2



def hill_known_key_crypt(K, m, text):
    numerical = []
    for i in range(0, len(text), m ):
        block = []
        for j in range(0,m):
            if( i<len(text) ): block.append(abeceda.index(text[i]))
            else: block.append(23) #dodamo 'X'
            i += 1
        numerical.append(block)

    cipher = ''
    for i in range(0,len(numerical)):
        #svaki blok pomonozimo sa kljucem
        numerical_cipher = numerical[i] @ K
        for j in numerical_cipher:
            print(j)
            rest = int(j % 26)
            cipher += abeceda[rest]
    return cipher

def print_hill_cipher():
    text = input("Type plain text: ")
    hm = input("Type m: ")
    m = int(hm)
    key_word = input("Type key word: ")

    K = np.zeros((m,m))
    k = 0
    for i in range(0,m):
        for j in range(0,m):
            K[i][j] = int(abeceda.index(key_word[k]))
            k += 1

    for i in range(0,m):
        for j in range(0,m):
            print(K[i][j], end = ' ')
        print()
    print( hill_known_key_crypt(K, m, text) )

# print_hill_cipher()
# input("wait")

def get_row_of_plain_text_numerical(m, r, plain_text_numerical):
    result = []
    for i in range( int(m*r),int(m*r+m)):
        result.append(plain_text_numerical[i])
    return result

def make_matrix(options, m, numerical):
    M = np.empty( (m,m) )
    M.astype(int)
    for i in range(0, m):
        option =  options[i]
        for j in range(0,m):
            M[i,j] = int(numerical[int(option*m)+j])
    return np.asmatrix(M)

def hill_decrypt():
    #postoji m povrh 2 mogućnosti
    plain_text = input("Type plain text:")
    plain_text_numerical = []
    for i in plain_text:
        plain_text_numerical.append(abeceda.index(i))

    cipher = input("Type cipher:")
    cipher_numerical = []
    for i in cipher:
        cipher_numerical.append(abeceda.index(i))

    while( 1 ):  
        m = int(input("Type m: "))
        rest = len(plain_text) % m
        if( rest == 0 ): break
        print("Not good! Try again...")

    while(1):
        #pokušavamo invertirati
        print("Type option that you want to be the first row of X:")
        for i in range(0, int(len(plain_text)/m) ):
            print("Option: \"", i+1, "\". ", end=' ' )
            for j in range(m*i, m*i+m): print(plain_text[j], " ", end = ' ')
            print("\n")
        print("\n")

        options = np.empty( m )
        for i in range(0,m):
            print("For the ", i+1 ,"th row I want: ")
            option = int(input()) - 1
            while( option in options ):
                print("Already selected. Try again!")
                print("For the ", i+1 ,"th row I want: ")
                option = int(input())  - 1
            options[i] = option 

        #pogledajmo je li takva matrica invertibilna
        M = make_matrix( options, m, plain_text_numerical ) 
        print("M matrix:")
        print(M)
        print(matrix_rank(M))

        if np.isfinite(np.linalg.cond(M)):
            M_inv = getMatrixInverse(M, m)
            Y = make_matrix( options, m, cipher_numerical )

            #K = np.matmul(M_inv, Y)
            K = np.zeros((m,m))
            for i in range(m):  
                for j in range(m): 
                    for k in range(m):  
                        K[i,j] += (M_inv[i,k] * Y[k,j])
                    K[i, j] = K[i, j] % 26
            break
        else:
            print("Selected matrix is not invertible! Try again ...")
   
    print("Key matrix is: ") 
    print(K)
    print()

    print("Key matrix with actual letters: ")
    for i in range(m):
        for j in range(m):
            print(abeceda[int(K[i,j])], " ", end=' ')
        print("")
    print("\n\n")

hill_decrypt()