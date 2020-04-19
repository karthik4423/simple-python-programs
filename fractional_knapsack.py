# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    ratio=[]
    for i in range(len(weights)):
        ratio.append(values[i]/weights[i])

    for i in range(len(weights)):
        if capacity ==0:
            return value
        else:
            while(True):
                if weights[ratio.index(max(ratio))]>0:
                    w = ratio.index(max(ratio))
                    a=min(weights[ratio.index(max(ratio))],capacity)
                    value = value + a*ratio[w]
                    weights[w]-=a
                    capacity-=a
                    break
                else:
                    ratio[ratio.index(max(ratio))]=0



    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
