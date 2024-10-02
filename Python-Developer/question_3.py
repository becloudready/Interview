def minRecursive(threshold, points):
    if len(points)==1:
        return 0
    if len(points)==2:
        return 1
    if len(points)>=3:
        return minRecursive(threshold-points[0], points[2:len(points)]) + 1

def minimum_points(threshold, points):
    # write your code here
    if len(points) <=0:
        return 0
    #since array is sorted, we check the difference between the max and min points and compare with the threshold, if less perform all the problems
    if points[len(points)-1] - points[0] < threshold:
        return len(points)
    else:
        return minRecursive(threshold, points) +1


if __name__ == "__main__":
    # write your debug code here
    pass
