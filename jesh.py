s=input()
g=[]
for i in s:
    g.append(i)
h=[]
for i in g:
    n=0
    for j in g:
        if(j==i):
            n=n+1
        h.append(n)    
    print(i)
    print(n)
print(max(h))
