class Solution:
       def countBinarySubstrings(self, s: str) -> int:
        count_one = 0
        count_zero = 0
        fun_output = 0

        i = 0
        while i < len(s):
            while (i < len(s) and s[i] == '0'):
                count_zero += 1
                i += 1
                if (count_one > 0):
                    count_one -= 1
                    fun_output += 1
            count_one = 0
            while (i < len(s) and s[i] == '1'):
                count_one += 1
                i += 1
                if (count_zero > 0):
                    count_zero -= 1
                    fun_output += 1
            count_zero = 0
        return fun_output
