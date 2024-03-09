import math
import matplotlib.pyplot as plt

def collatz_iterations(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        count += 1
    return count
def main():
    lim:int = 500
    lInters = []
    lYaxis = [x for x in range(1,lim+1)]
    for i in range(1, lim+1):
        lInters.append(collatz_iterations(i))
    plt.figure(figsize=(10,5))
    plt.ylim(0,100)
    plt.xlim(0,lim)
    plt.plot(lYaxis, lInters)
    plt.show()
if __name__ == "__main__":
    main()
