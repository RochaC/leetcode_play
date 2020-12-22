class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.sorted_candidates = sorted(candidates)
        self.len = len(self.sorted_candidates)
        self.dfs(target, 0, [])

        return self.res

    def dfs(self,target, pos_start, vlist):
        print("Search target: %s, Pos start: %s, vlist: %s" %(target, pos_start, vlist))
        if target == 0:
            self.res.append(vlist)
            return
        elif target < 0:
            print("break")
            return True
        else:
            for i in range(pos_start, self.len):
                if(i > pos_start and self.sorted_candidates[i] == self.sorted_candidates[i-1]):
                    continue     # remove duplicate

                if_break = self.dfs(target-self.sorted_candidates[i], i+1, vlist + [self.sorted_candidates[i]])
                if if_break:
                    break


if __name__ == '__main__':
    candidates = [2,5,2,1,2]
    target = 5
    so = Solution()
    print(so.combinationSum2(candidates, target))
