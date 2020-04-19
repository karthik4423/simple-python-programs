# python3
import sys


def compute_min_refills(distance, tank, stops):
    i=0
    s=0
    visited=[0]*(len(stops)+1)
    t=tank
    stops.append(distance)
    #if(distance < tank):
    #    return 0
    #if(tank > distance/2 and len(stops)>0):
    #    return 1
    while tank<distance and i<len(stops):
        if(s>len(stops)-1):
            return -1
        if(tank>stops[i]):
            i+=1
        elif(tank<stops[i]):
            if(visited[i]==1):
                return -1
            else:
                i-=1
                s+=1
                visited[i]=1
                tank=stops[i]+t
        elif(tank==stops[i]):
            if(visited[i]==1):
                return -1
            else:
                s+=1
                visited[i]=1
                tank=stops[i]+t
    #print("three")
    
    return s

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
