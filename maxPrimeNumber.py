def maxPrimeNumber(num):
    for n in range(1, num+1):
        flag = 1
        for i in range(2, int(n**0.5) + 1):
            if n%i == 0:
                flag = 0
                break
    if flag == 1:
        return n
if __name__ == '__main__':
    print(maxPrimeNumber(10))