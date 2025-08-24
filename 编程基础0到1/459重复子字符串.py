class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False

        for i in range(1, len(s)):
            if s[i] != s[0]:
                flag = False
                break
            else:
                flag = True
        if flag == True:
            return True

        flag = False
        for i in range(2, len(s)//2+1):  # 每段1个字母到len(s)//2个字母
            print(i)
            print('len(s)%i', len(s)%i)
            if len(s)%i == 0:
                print('len(s)//i', len(s)//i)
                for j in range(0, len(s)//i+i, i):  # 判断这些len(s)//i个字符段相不相等
                    print(j)
                    print('s[j:j+i]:',s[j:j+i],'s[0:i]:', s[0:i])
                    if s[j:j+i] != s[0:i]:
                        flag = False
                        break
                    else:
                        flag = True

                if flag == True:
                    return True
        return False

        # # 法2
        if len(s) == 1:
            return False

        for i in range(1, len(s)):
            if s[i] != s[0]:
                flag = False
                break
            else:
                flag = True
        if flag == True:
            return True

        flag = False
        for i in range(2, len(s) // 2 + 1):  # 每段1个字母到len(s)//2个字母
            if len(s) % i == 0:
                for j in range(0, len(s) // i + i, i):  # 判断这些len(s)//i个字符段相不相等
                    if s[j:j + i] != s[0:i]:
                        flag = False
                        break
                    else:
                        flag = True

                if flag == True:
                    return True
        return False
solv = Solution()
# s = "abab"
# s = "aba"
# s = "abcabcabcabc"
# s ="abac"
s ="bb"
# s = "ababba"
print(solv.repeatedSubstringPattern(s))