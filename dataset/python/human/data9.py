Liste = [24,3,-10,7,5,-5,12,0]

def mergesort(liste):

    if len(liste) <= 1:
        return liste
    
    else:
        linkeliste = mergesort(liste[0:int(len(liste)/2)])
        rechteliste = mergesort(liste[int(len(liste)/2):])
        
    return merge(linkeliste,rechteliste)

def merge(linkeliste,rechteliste):
    
    verbindungsliste = []
    
    while linkeliste and rechteliste != []:
        if linkeliste[0] > rechteliste[0]:
            verbindungsliste = verbindungsliste+[rechteliste[0]]
            rechteliste = rechteliste[1:]
            
        else:
            verbindungsliste = verbindungsliste+[linkeliste[0]]
            linkeliste = linkeliste[1:]
            
    while rechteliste != []:
        verbindungsliste = verbindungsliste+[rechteliste[0]]
        rechteliste = rechteliste[1:]
            
    while linkeliste != []:
        verbindungsliste = verbindungsliste+[linkeliste[0]]
        linkeliste = linkeliste[1:]

    return verbindungsliste

print(mergesort(Liste))