i = 0
l=10
while i <= 10:
    print(i, end='')
    if i == 3:
        i -= 1
    i+=1
    l-=1
    if(l==0):break