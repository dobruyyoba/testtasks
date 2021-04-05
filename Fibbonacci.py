from math import sqrt


def Fibonacci(n):
    return (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n) / sqrt(5)


if __name__ == '__main__':
    for i in range(int(input())):
        print(int(Fibonacci(i*3)), end = " ")
    
