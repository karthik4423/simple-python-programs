# Uses python3
import sys

def get_change(m):
    c=int(m/10)
    m=m%10
    c=c+int(m/5)
    m=m%5
    c=c+int(m)
    return c

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
