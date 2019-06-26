# answer1={1:35,2:36,3:40,4:44}
# answer2={1:'about'}
#question1:
a1=[35,36,40,44,4]
a2=[55,65,75,85,2]
count=0
print('If x=8, then what is the value of 4(x+3) ?')
for i in range(4):
    print(str(i+1),'. ',a1[i])
answer=input('Your choice: ')
if answer=='4':
    print('😎   😎')
    count+=1
else: print('😞')
#question2
print('Jack scored these marks in 5 math tests : 49, 81, 72, 66 and 52. What is the mean?')
for i in range(4):
    print(str(i+1),'. About',a2[i])
answer=input('Your choice: ')
if answer=='2':
    print('😎   😎')
    count+=1
else: print('😞')
print('You corectly answer '+ str(count) +' out of 2 question')