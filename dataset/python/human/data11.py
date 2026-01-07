
Liste = [7,3,9,2,5,10,6,1,4,8]
print ("Unsortierte Liste:",Liste)

def SelectionSort(Liste):
    x = 0
    for i in range(len(Liste)):
        zk = i
        for z in range(i,len(Liste)):
            if Liste[z] < Liste[zk]:
                zk = z
        y = Liste[i]
        Liste[i] = Liste[zk]
        Liste[zk] = y
        x = x + 1
        print(x,".Durchlauf:",Liste)
      
    return Liste
print("Sortierte Liste:",SelectionSort(Liste))