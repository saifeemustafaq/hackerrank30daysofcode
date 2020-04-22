if __name__ == '__main__':
    n = int(input())
    bin_n = list((bin(n)[2:]))
    
    count, result = 0, 0

    for x in range(0,len(bin_n)):
        if bin_n[x] == '0':
            count = 0
        else:
            count+=1
            result = max(result,count)
    print(result)
