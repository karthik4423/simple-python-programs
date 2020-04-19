# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    highest=0
    max_index=0
    smax_index=0
    for i in range(n):
        if (numbers[i]>highest):
            highest = numbers[i]
            max_index=i
    
    highest=0
    for i in range(n):
        if(numbers[i]>highest and max_index!=i):
            highest=numbers[i]
            smax_index=i
    
    return(numbers[max_index]*numbers[smax_index])


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
