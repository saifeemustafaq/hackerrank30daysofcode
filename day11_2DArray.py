if __name__ == '__main__':
    arr = []
    mega = []
    for x in range(6):
        temp_ar = [int(x) for x in input().split()]
        arr.append(temp_ar)
    
    for y in range(4):
        for z in range(4):
            temp = (arr[y][z]+arr[y][z+1]+arr[y][z+2]) + (arr[y+1][z+1]) + (arr[y+2][z]+arr[y+2][z+1]+arr[y+2][z+2])
            mega.append(temp)
    print(max(mega))
