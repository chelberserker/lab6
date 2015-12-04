with open('input.txt', 'r') as inp:
    with open('output.txt', 'w') as out:
        data = list(map(int, inp.readline().split()))
        k = data[0]
        n = data[1]
        minimums = [-1 for i in range(n)]
        for i in range(k):
            vvod = list(map(int, inp.readline().split()))
            for j in range(n):
                # print(n, j)
                if vvod[j] < minimums[j] or minimums[j] == -1:
                    minimums[j] = vvod[j]
        print(' '.join(map(str, minimums)), file=out)
