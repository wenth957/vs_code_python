# 给定一个序列，得到两个序列，一个递增子序列 另一个递减子序列 不连续
nums = [8, 6, 1, 3, 2, 4, 5]


def find_inc_des(nums):
    up = []
    down = []

    def dfs(nums, index, up, down):
        if index == len(nums):
            print(up)
            print(down)
            return True
        num = nums[index]
        if up == [] or num > up[-1]:
            up.append(nums[index])
            if dfs(nums, index + 1, up, down):
                # 不满足条件时，回溯到最初，看是否满足递减序列
                # 找到一条序列即可返回
                return True
            up.pop()
        # 找递增子序列的同时要找到递减子序列
        if down == [] or num < down[-1]:
            down.append(nums[index])
            if dfs(nums, index + 1, up, down):
                # 不满足条件时，直接回溯,因为进入递减的必然不满足递增的性质
                return True
            down.pop()
        # 递增递减均不满足即无法按照当前顺序拆分，回溯到最初，开始重新收集序列
        return False
    return dfs(nums, 0, up, down)


print(find_inc_des(nums))
