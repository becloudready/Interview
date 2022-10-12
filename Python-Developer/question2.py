from math import floor


def center_zeros(array):
    # write your function here
    # center means the floor(x / 2) where floor means rounding a float (decimal number) down to the nearest integer
    # i.e. floor(1) = 1, floor(1.5) = 1, floor(1.75) = 1, floor(2) = 2
    count_zero = 0
    for i in array:
        if i==0:
            count_zero+=1

    mid = floor(int(len(array)/2))
    li= []

    for i in range(0,(mid-count_zero)+1):
        if array[i]!=0:
            li.append(array[i])

    for i in range(count_zero):
        li.append(0)

    for i in range(mid-1,len(array)):
        if array[i]!=0:
            li.append(array[i])
    return li


if __name__ == "__main__":
    # write your debug code here
    pass
