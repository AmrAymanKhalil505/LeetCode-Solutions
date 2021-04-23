class Solution(object):
    oo = float(1e9)
    dp = [None]
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        Solution.dp = triangle[len(triangle)-1].copy()

        return Solution.stepUp(triangle)
    @staticmethod
    def stepDown (indexX, indexY, tringle, mysum):

        right = Solution.oo
        left = Solution.oo
        print(indexX, indexY, tringle[indexY][indexX], mysum, sep=',')
        if(indexY == len(tringle)-1):
            return tringle[indexY][indexX]
        #if((len(tringle[indexY+1]))<indexX+1):
        if(Solution.dp[indexY] is None):
            right = Solution.stepDown(indexX + 1,indexY+1, tringle, mysum)
            left = Solution.stepDown(indexX,indexY+1, tringle, mysum)
            Solution.dp[indexY] = tringle[indexY][indexX] + min(left,right)

        return Solution.dp[indexY]

    @staticmethod
    def stepUp(triangle):
        for i in range(len(triangle)-2,-1,-1):
            #print(i)
            #print(Solution.dp)
            for j in range(i+1):
               # print(j ,Solution.dp[j],Solution.dp[j+1],min(Solution.dp[j],Solution.dp[j+1]),triangle[i][j],sep=" , " )
                Solution.dp[j]= min(Solution.dp[j],Solution.dp[j+1])+triangle[i][j]
        return Solution.dp[0]