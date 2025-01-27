class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1): #jika panjang str2 lebih besar dari str1, maka panggil fungsi gcdOfStrings dengan parameter str2 dan str1
            print("pilihan 1")
            return self.gcdOfStrings(str2, str1)
        
        if str1 == str2: #jika str1 sama dengan str2, maka kembalikan str1
            print("pilihan 2")
            return str1
        
        if str1.startswith(str2): #jika str1 diawali dengan str2, maka panggil fungsi gcdOfStrings dengan parameter str1 yang dihilangkan str2 dan str2
            print("pilihan 3")
            return self.gcdOfStrings(str1[len(str2):], str2)
            
        
        return ""

# Contoh penggunaan
solution = Solution()
str1 = "AB"
str2 = "ABABABAB"
result = solution.gcdOfStrings(str1, str2)
print(result)  # Output: "ABC"