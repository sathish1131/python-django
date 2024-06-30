x = int(input('Enter the number of rows: '))


def patternPrint(rows):
    for i in range(1,rows+1,1):
        for j in range(0,i,1):
            print('*',end='')
        print()

patternPrint(x)
