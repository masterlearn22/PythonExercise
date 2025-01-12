class Solution :
    def kidsWithCandies(self, candies:int, extraCandies: int) ->bool :
        max_candies = max(candies)
        for i in range(len(candies)) :
            if candies[i] + extraCandies >= max_candies :
                candies[i] = True
            else :
                candies[i] = False
        return candies
                
candies = [2, 3, 6, 1, 3]
extraCandies = 3
solution = Solution()
result = solution.kidsWithCandies(candies, extraCandies)
print(result) 
#program diatas adalah program yang digunakan untuk menentukan apakah anak-anak dapat memiliki permen yang paling 
#banyak jika setiap anak-anak diberikan permen tambahan sebanyak `extraCandies` permen.