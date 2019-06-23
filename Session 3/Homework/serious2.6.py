n=int(input('Enter the number of sheep you have : '))
month=int(input('Enter the number of months you want : '))
sizes=[]
for i in range(n):
    k=int(input('Enter the size of the sheep '+ str(i+1) +' : '))
    sizes.append(k)
print('Hello, My name is Thanh and these are the ship sizes: ',sizes)
for i in range(month):
    print('MONTH '+str(i+1))
    for j in range(n):
        sizes[j]+=50
    print('One month has passed, now here is my flock : ',sizes)
    max_=0
    for j in range(n):
        if max_<sizes[j]:
            max_=sizes[j]
            position = j
    print('Now my biggest sheep has size ' + str(max_)+ " let's shear it")
    sizes[position]=8
    print('After shearing, here is my flock : ',sizes)
sumsize=0
for i in range(n):
    sumsize+=sizes[i]
print('My flock has size in total : ' + str(sumsize))
print('I would get '+str(sumsize)+'*2$ = '+str(2*sumsize))