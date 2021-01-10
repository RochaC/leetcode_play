class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        depth = len(triangle)
        wide = len(triangle[-1])
        f = [1e9] * wide

        if depth < 1:
            return 0

        # > 2 level
        for i in range(0, depth):
            w = len(triangle[i]) - 1
            for j in range(w, -1, -1):
                if i == 0:
                    f[j] = triangle[i][j]
                elif j == w:
                    f[j] = f[j-1] + triangle[i][j]
                elif j == 0:
                    f[j] = f[j] + triangle[i][j]
                else:
                    f[j] = min(f[j-1], f[j]) + triangle[i][j]


        return min(f)


if __name__ == '__main__':
    input = [[2],[3,4],[6,5,7],[4,1,8,3]]
    so = Solution()
    print("res: %s"  % so.minimumTotal(input))