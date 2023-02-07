n=int(input())
count=1
for i in range(1, 10+1):
    t=str(i)
    count=n*i
    count=str(count)
    table=str(n)+" x "+t+" = "+count
    print(table)
