class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        min_length = min(len(word1), len(word2))
        
        # Merge characters from both strings
        for i in range(min_length):
            merged += word1[i] + word2[i]
        # Add any remaining characters from the longer string
        print(min_length)
        merged += word1[min_length:] + word2[min_length:]
        
        return merged

# Example usage
world1 = "abcdef"
world2 = "pqrs7"
solution = Solution()
result = solution.mergeAlternately(world1, world2)
print(result)  # Output: "apbqcr"