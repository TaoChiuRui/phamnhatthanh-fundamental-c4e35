s = "ThiS is String with Upper and lower case Letters"
counts={}
for i in s.lower():
    counts[i]=counts.get(i,0)+1
items=list(counts.items())
items.sort()
del items[0]
for i,j in items:
    print(i,j)

    # # khieu cho lam, bao anh thay giang lai tren lop duoc khong?