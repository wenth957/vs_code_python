# -*- Coding: UTF-8 -*-
# queue.py
# @作者 ML_get ML
# @创建日期 2022-09-11T22:35:18.279Z+08:00
# @最后修改日期 2022-09-11T22:35:18.279Z+08:00
# 实现单调队列：求滑动窗口最大值


def queue(nums, k):
    """
    k为滑动窗口的大小, 当i大于等于k时打印且队列头向右移动
    """
    head = 0
    que = []
    res = []
    for i in range(len(nums)):
        if head < len(que) and i - que[head] == k:
            # 当i-队头idx==k即超出滑动窗口长度时，滑动窗口向右移动一个单位
            head += 1
        while head < len(que) and nums[que[-1]] < nums[i]:
            # 当队尾元素非单调递减时，队尾元素一定不是该窗内最大值，队尾元素出队
            que.pop()
        que.append(i)
        if i >= k - 1:
            res.append(nums[que[head]])

    return res


print(queue([1,3,-1,-3,5,3,6,7],3))

