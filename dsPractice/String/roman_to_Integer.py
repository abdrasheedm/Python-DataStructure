class Solution:
    def __init__(self) -> None:
        self.I = 1
        self.V = 5
        self.X = 10
        self.L = 50
        self.C = 100
        self.D = 500
        self.M = 1000

    def romanToInt(self, s: str) -> int:
        output = 0
        for i in range(len(s)):
            if s[i] == 'M':
                if i != 0 and s[i - 1] == 'C':
                    continue
                else:
                    output += 1000

            elif s[i] == 'D':
                if i != 0 and s[i - 1] == 'C':
                    continue
                else:
                    output += 500

            elif s[i] == 'C':
                if i != (len(s) - 1) and s[i + 1] == 'M':
                    output += 900
                elif i != (len(s) - 1) and s[i + 1] == "D":
                    output += 400
                elif i != 0 and s[i - 1] == 'X':
                    continue
                else:
                    output += 100

            elif s[i] == 'L':
                if i != 0 and s[i - 1] == 'X':
                    continue
                else:
                    output += 50

            elif s[i] == 'X':
                if i != (len(s) - 1) and s[i + 1] == 'L':
                    output += 40
                elif i != (len(s) - 1) and s[i + 1] == 'C':
                    output += 90
                elif i != 0 and s[i - 1] == 'I':
                    continue
                else:
                    output += 10

            elif s[i] == 'V':
                if i != 0 and s[i - 1] == "I":
                    continue
                else:
                    output += 5

            elif s[i] == "I":
                if i != (len(s) - 1) and s[i + 1] == 'V':
                    output += 4
                elif i != (len(s) - 1) and s[i + 1] == 'X':
                    output += 9
                else:
                    output += 1
            else:
                print("please enter a valid roman number")

        return output

    def romIntSimple(self, s: str) -> None:
        dicts = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        output = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD",
                                                                                                                "CCCC").replace(
            "CM", "DCCCC")
        for i in s:
            output += dicts[i]

        return output


x = Solution()
print(x.romIntSimple('MCMXCIV'))