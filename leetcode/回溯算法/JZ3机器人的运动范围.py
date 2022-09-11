# -*- Coding: UTF-8 -*-
# JZ3机器人的运动范围.py
# @作者 ML_get ML
# @创建日期 2022-08-31T22:10:17.943Z+08:00
# @最后修改日期 2022-08-31T22:13:40.369Z+08:00
#


class Solution:
    def sum_(self, num):
        res = 0
        while num:
            res += num % 10
            num //= 10
        return res

    def movingCount(self, threshold, rows, cols):
        def dfs(i, j, k):
            if i >= rows or j >= cols or (self.sum_(i) + self.sum_(j)) > k or (i, j) in visited:
                return 0
            visited.add((i, j))
            return 1 + dfs(i + 1, j, k) + dfs(i, j + 1, k)
        visited = set()
        return dfs(0, 0, threshold)

if __name__ == "__main__":
    solve = Solution().movingCount
    print(solve(1, 2, 3))
    print(solve(0, 1, 3))
    print(solve(10, 1, 100))



