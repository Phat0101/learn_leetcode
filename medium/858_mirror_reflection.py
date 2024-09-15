class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lcm = (p * q) // math.gcd(p, q)
        if (lcm // q) % 2 == 1 and (lcm // p) % 2 == 1:
            return 1
        elif (lcm // q) % 2 == 1 and (lcm // p) % 2 == 0:
            return 0
        else:
            return 2