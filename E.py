with open('input.txt', 'r') as inp:
    with open('output.txt', 'w') as out:
        data = list(map(int, inp.readline().split()))
        N = data[0]
        K = data[1]
        dolgi = [0 for i in range(N)]
        for i in range(K):
            vvod = list(map(int, inp.readline().split()))
            doljnik = vvod[0]-1
            creditor = vvod[1]-1
            summa = vvod[2]
            dolgi[doljnik] -= summa
            dolgi[creditor] += summa
        print(' '.join(map(str, dolgi)), file=out)
