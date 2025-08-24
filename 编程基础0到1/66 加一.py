class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        sum = 1
        for i, digit in enumerate(digits):
            sum += digit * 10 ** (n - i - 1)

        # digits_new = [sum % (10 ** i) for i in range(sum)]
        # return digits_new
        result = []
        while sum > 0:
            a = sum % 10
            result.append(a)
            sum = sum // 10
        result.reverse()
        return result



solv = Solution()
digits1 = [1,2,3]
digits2 = [4,3,2,1]
digits3 = [9]
print(solv.plusOne(digits1))
print(solv.plusOne(digits2))
print(solv.plusOne(digits3))