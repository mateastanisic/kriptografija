from operator import itemgetter
import sys
import math
from letters_and_freq import frequency_cro, letters

def bigrams(text):
    #pravi tablicu s predavanja
    bigram_analysis = { "A" : [],  "B" : [],  "C" : [],  "D" : [],  "E" : [], "F" : [],  "G" : [],
    "H" : [],  "I" : [],  "J" : [],  "K" : [],  "L" : [],  "M" : [],  "N" : [],  "O" :   [],
    "P" : [],  "Q" : [],  "R" : [],  "S" : [],  "T" : [],  "U" : [],  "V" : [],  "W" : [],
    "X" : [],  "Y" : [],  "Z" : [] }
    for i in range(0, len(text)-1):
        bigram_analysis[text[i]].append(text[i+1])
    return bigram_analysis

def mini_freq(best_freq):
    #pomoćna funkcija za računanje frekvencije bigrama
    min_f = best_freq[0]
    min_k = 0
    for k in range(1,len(best_freq)):
        if best_freq[k] < min_f : 
            min_f = best_freq[k]
            min_k = k
    return [min_k, min_f]

def freq_bigrams(bigrams):
    best_ten_bi = []
    best_ten_freq = []
    for bi in bigrams: #za svako slovo abecede provjeri sve njegove bigrame
        polje = bigrams[bi[0]] 
        for i in range(0, len(polje)): #za svako drugo slovo bigrama gledaj koliko puta se pojavljuje 
            num = 1
            bigr = ""
            bigr += bi[0] 
            bigr += polje[i]
            if bigr in best_ten_bi: 
                continue
            for j in range(i+1, len(polje)): #gledaj koliko puta se pojavljuje tako da gledas samo ispred, iza nema smisla, vec bi nasli
                if polje[i] == polje[j]: 
                    num += 1
            #sad kad smo odredili freq "novopromatranog" bigrama usporedimo ih sa 10 najboljih
            if len(best_ten_bi) >= 10:
                mini = mini_freq(best_ten_freq)
                if mini[1] < num: #samo ako smo nasli bolje
                    best_ten_freq[mini[0]] = num
                    best_ten_bi[mini[0]] = bigr
            else: #još se nije ni popunilo polje
                best_ten_bi.append(bigr)
                best_ten_freq.append(num)
    return [ best_ten_bi, best_ten_freq ]


def print_bigram_freq(chiper):
    text = chiper.upper()
    bigram_freq_table = bigrams(text)
    result = freq_bigrams(bigram_freq_table)
    for i in range(0,len(result[0])):
        print("Bigram:", result[0][i]," with frequency ", result[1][i]) 
    print("\n\n")