class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        m = len(digits) - 1

        for i in range(m, -1, -1):
            digits[i] += carry

            if digits[i] < 10:
                carry = 0
                break
            else:
                digits[i] = 0
                carry = 1

        if carry == 1:
            digits.insert(0, 1)

        return digits


        return digits


