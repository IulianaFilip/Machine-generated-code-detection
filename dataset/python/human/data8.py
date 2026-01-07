def insertionSort(liste): 
    for i in range(1, len(liste)):

        schluessel = liste[i] 

        j = i-1
        while j >=0 and schluessel < liste[j]: 
            liste[j+1] = liste[j] 
            j -= 1
        liste[j+1] = schluessel
    return liste


liste = [12, 11, 13, 5, 6] 

print(insertionSort(liste))