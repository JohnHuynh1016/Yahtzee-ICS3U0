lista = [1,4,12,5,13,532,23,25,34]

#comparing neighbours
arrs=len(lista)
for a in range(arrs-1):
    for i in range(arrs-1):
        if lista[i] > lista[i+1]:
            lista[i],lista[i+1]=lista[i+1],lista[i]

listb = [1,4,12,5,13,532,23,25,34]
#selection
oldlist = listb
newlist = []
arrsb=len(listb)
for i in range(arrsb-1):
    newlist.append(min(oldlist))
    oldlist.remove(min(oldlist))