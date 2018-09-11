n= 5 #no. of webpages
a=[[0,1,1,1,0],[1,0,1,1,0],[0,0,0,1,0],[0,0,1,0,1],[0,1,1,1,0]] #matrix
A=[0 for x in range(n)]
H=[1 for x in range(n)]

it=int(input("Enter number of iterations:"))
for z in range(it):
    print ('\nInteration Number: ',z+1,'\n')
    for i in range(n):
        for j in range(n):
            if(a[j][i]!=0):
                A[i]=A[i]+H[j]
    s1=0
    for i in range(n):
        s1=s1+A[i]
    print("Authority Score: ",s1)
    for i in range(n):
        A[i]=float(A[i])/float(s1)
        print('Authority Score for ',i,' is ',A[i])
    for i in range(n):
        H[i]=0
    for i in range(n):
        for j in range(n):
            if(a[i][j]!=0):
                H[i]=H[i]+A[j]
    s2=0
    for i in range(n):
        s2=s2+H[i]
    print("\nHub Score: ",s2)
    for i in range(n):
        H[i]=float(H[i])/float(s2)
        print('Hub Score for ',i,' is ',H[i])



