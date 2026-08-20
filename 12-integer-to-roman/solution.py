class Solution:
    def intToRoman(self, num: int) -> str:
        # Values and symbols ordered from largest to smallest.
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]

        result = []
        remaining = num

        for val, sym in zip(values, symbols):
            if remaining <= 0:
                break
            count, remaining = divmod(remaining, val)
            if count:
                result.append(sym * count)

        return "".join(result)
