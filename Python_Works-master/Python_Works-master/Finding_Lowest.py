liste = [1, 2, 52, -500, 65, 12]
lowest = liste[0]

for x in liste:
    if(lowest > x): lowest = x
    
print(lowest)
