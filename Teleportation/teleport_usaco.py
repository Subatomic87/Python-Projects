a, b, x, y=map(int,input().split())
sum=0

if abs(a-x)>=abs(a-y):
    sum=sum+abs(a-y)
    sum=sum+abs(b-x)

else:
    sum=sum+abs(a-x)
    sum=sum+abs(b-y)

if abs(b-a)<=sum:
    print(abs(b-a))
else:
    print(sum)