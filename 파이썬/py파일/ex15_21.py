print("20211127 이건호")

import numpy as np

def calc(data):
    sum = np.sum(data)
    avg = np.mean(data)
    std = np.std(data)
    return sum, avg, std

def main():
    data1 = np.array( [[8,5,2,3,6],[5,4,1,3,5]] )
    sum1, avg1, std1 = calc(data1)
    print(sum1, avg1, std1)

if __name__=="__main__":
    main()
    input()