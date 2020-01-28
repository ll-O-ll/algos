import collections
def maxPointsOnLine(points):
    if len(points) <= 2:
            return len(points)        
    max_n = 0
    for i in range(len(points)):
        dic = collections.defaultdict(int)
        line_n, same_n = 0, 0
        for j in range(i+1, len(points)):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            if dx== 0 and dy == 0: # Case: [[0,0],[0,0]], the result should be 2. So we should count the number of duplicates points.
                same_n += 1
                continue
            gcd = getGCD(dx, dy)
            slope = str(dx//gcd) + ' ' + str(dy//gcd) # If use /, there will be '-0.0'
            dic[slope] += 1
            line_n = max(line_n, dic[slope])
        max_n = max(max_n, line_n+same_n+1) # add duplicate point counter if nonzero and add the point (i) on which we evaluate all lines that could traverse it 
    print(max_n) 

def getGCD(a, b): #find greatest common divider to normalize slopes in hash table
    if a == 0:
        return b
    return getGCD(b % a, a)
if __name__ == '__main__':
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    maxPointsOnLine(points)
    