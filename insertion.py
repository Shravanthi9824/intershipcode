l=[1,3,7,8,4,6]
n=len(l)
for i in range(1,len(l)):
    key=l[i]
    j=i-1
    while j>=0 and l[j]>key:
         l[j+1]=l[j]
         j=j-1
    l[j+1]=key
print(l)