# Enter your code here. Read input from STDIN. Print output to STDOUT
q=int(input())
stpush=[]
stpop=[]
for _ in range(q): 
    l=list(map(int,input().split()))
    if l[0]==1:stpush.append(l[1])
    elif l[0]==2:
        stpush.pop(0)
    else: 
        print(stpush[0])
