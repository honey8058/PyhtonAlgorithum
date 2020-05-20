print('enter a number')
num = int(input())
for i in range( 1, num+1):
    for j in range(i, num-i+1):
        print(end=" ")
    for j in reversed(range(i,0,-1)):
        print(j,end=" ")
    for j in reversed(range(1,i+1-1)):
        print(j,end=" ")
    print()
