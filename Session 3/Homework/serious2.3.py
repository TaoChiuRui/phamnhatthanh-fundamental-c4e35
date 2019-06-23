n=int(input('Enter the number of sheep you have : '))
sizes=[]
max_=0
for i in range(n):
    k=int(input('Enter the size of the sheep '+ str(i+1) +' : '))
    sizes.append(k)
    if max_<sizes[i]:
        max_=sizes[i]
        position = i
print('Hello, My name is Thanh and these are the ship sizes: ',sizes)
print('Now my biggest sheep has size ' + str(max_)+ " let's shear it")
sizes[position]=8
print('After shearing, here is my flock : ',sizes)