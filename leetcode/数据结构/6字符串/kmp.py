def Strstr(s, p):
    def get_next(p):
        next_ = [0] * len(p)
        j = 0
        for i in range(1, len(p)):
            while j and p[i] != p[j]:
                j = next_[j - 1]
            if p[i] == p[j]:
                j += 1
            next_[i] = j
        return next_
    j = 0
    next_ = get_next(p)
    for i in range(len(s)):
        while j and s[i] != p[j]:
            j = next_[j - 1]
        if s[i] == p[j]:
            j += 1
        if j == len(p):
            return i - len(p) + 1
    return -1


s = 'aabaabaaf'
p = 'aabaaf'
print(Strstr(s, p))
