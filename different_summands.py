# Uses python3
import sys

def optimal_summands(n):
    summands = []
    if(n==1):
        a=[1]
        return a
    elif(n==2):
        a=[2]
        return a
    else:
        summands=[1,2]
        i=3
        summ=sum(summands)
        while(summ<=n):
            if(summ==n):
                return summands
            if(summ+i<=n):
                summands.append(i)
                i+=1
            else:
                el=summands[i-2]
                summands[i-2]=n-summ+el
            summ=sum(summands)

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
