class Solution:
    def romanToInt(self, s: str) -> int:
        t=0
        for st in s:
            if st == 'I':
                i=1
                t = t+i
            elif st == 'V':
                i=5
                if t==1:
                    t=i-t
                else:
                    t=t+i
            elif st == 'X':
                i=10
                if t==1:
                    t = i-t
                else:
                    t=t+i
            elif st == 'L':
                i=50
                if t==10:
                    t=i-t
                else:
                    t=i+t
            elif st == 'C':
                i=100
                if t==10:
                    t = i-t
                else:
                    t=i+t
            elif st == 'D':
                i=500
                if t==100:
                    t = i-t
                else:
                    t = i+t
            elif st == 'M':
                i=1000
                if t == 100:
                    t=i-t
                else:
                    i=i+t
r = roman