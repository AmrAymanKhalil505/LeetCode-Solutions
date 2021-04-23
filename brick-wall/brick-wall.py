class Solution:
    def leastBricks(self, wall ) :
        gaps = dict()
        for i in range(len (wall)):
            gap_place = 0
            for j in range (len (wall[i])-1):
                gap_place += wall [i][j]
                if( gaps.get(gap_place) is None):
                    gaps[gap_place] = 1
                else:
                    gaps[gap_place] = gaps[gap_place] + 1
        if( bool (gaps)):
            mykey = max(gaps, key=gaps.get)
            return len(wall) - gaps[mykey]
        else:
            return len(wall)
        