# Uses python3
def calc_fib(n):
    if n-1==0:
        return 0
    elif n-1==1:
        return 1
    else:
        num=[0]*n
        num[0]=0
        num[1]=1
        i=0
        for i in range (2,n):
            num[i]=(num[i-1]+num[i-2])
        #print(num)
    return(num[n-1])

n = int(input())
print(calc_fib(n+1))
