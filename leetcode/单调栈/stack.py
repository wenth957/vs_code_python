# -*- Coding: UTF-8 -*-
# stack.py
# @作者 ML_get ML
# @创建日期 2022-09-11T22:11:21.558Z+08:00
# @最后修改日期 2022-09-11T22:29:34.899Z+08:00
#

def stack(nums):
    """实现单调栈功能：打印左边离得最近的smaller
      将左边的数存到一个栈中，然后从栈顶取元素
      入栈过程中pop掉哪些不可能小于当前位置的数（保持一个单调递增的栈: 底-顶）
    """
    stack = []
    for i in range(len(nums)):
        while (stack and stack[-1] >= nums[i]):
            stack.pop()
        if stack:
            print(stack[-1])
        else:
            print(-1)
        stack.append(nums[i])

        
stack([3, 4, 2, 7, 5])
