# Uses python3
import sys

def gcd_naive(a, b):
    if b==0 :
        return a
    else:
        a1=a%b
        return gcd_naive(b,a1)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
