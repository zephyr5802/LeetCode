class Solution:
    def gcd(a,b):
        while b:
            a,b =b , a%b
        return a

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1,l2= len(str1),len(str2)
        gcd_length=gcd(l1,l2)
        merger = str1[:gcd_length]
        
        if merger * (l1 // gcd_length) == str1 and merger * (l2 //gcd_length) ==str2:
            return merger
        else:
            return ""