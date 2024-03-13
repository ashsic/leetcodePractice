class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(' ')
                
        if not s:
            return 0

        negative = False
        flag = True

        s2 = ''
        for c in s:
            if (c == '-' or c == '+') and flag and not s2:
                flag = False
                if c == '-':
                    negative = True
            elif not c.isdigit():
                break
            else:
                s2 += c 


        if len(s2) == 0:
            s2 = 0
        else:
            s2 = int(s2)

        if (s2 >= 2147483648):
            if negative:
                return -2147483648
            return 2147483647

        return -s2 if negative else s2
        