for sum in range(100,1000):
    low=sum%10
    mid=sum//10%10
    high=sum//100
    if sum==low**3+mid**3+high**3:
        print(sum)