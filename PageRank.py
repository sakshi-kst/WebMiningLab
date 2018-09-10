def pagerank(matrix,o,n,p):
    a=0
    for i in range(0,n):
        if(int(matrix[i][o])==1):
            k=0
            for s in range(0,n):
                if(matrix[i][s]==1):
                    k=k+1
            a=a+float(p[i]/k)
    return a
n=5
matrix=[[0,1,1,1,0],[1,0,1,1,0],[0,0,0,1,0],[0,0,1,0,1],[0,1,1,1,0]]
d=0.5 #damping factor
print("Input number of iterations:")
o=int(input())
sum=0
p=[]
for i in range(0,n):
    p.append(1) #initially all nodes have value 1
for k in range(0,o):
    for u in range(0,n):
        g=pagerank(matrix,u,n,p)
        p[u]=(1-d)+d*g
for i in range(0,n):
    sum+=p[i]
    print("Page rank of node ", i+1,"is : ",p[i])
print("Sum of all page ranks: ",sum)
