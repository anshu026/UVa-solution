t=int(input())
for _ in range(1,t+1):
    li=[int(x) for x in input().split()]
    print("Case ",_,":"," ",max(li),sep="")
