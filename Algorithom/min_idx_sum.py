import math
class Solution(object):
    def findRestaurant(self, list1, list2):
        word1 = {word:idx for idx, word in enumerate(list1)}
        min_sum = math.inf
        for idx2, word2 in enumerate(list2):
            if word2 in word1:
                if word1[word2] + idx2 < min_sum:
                    min_sum = word1[word2] + idx2
                    print(min_sum)
                    min_words = [word2]
                elif word1[word2] + idx2 == min_sum:
                    min_words.append(word2)
        return min_words
        


list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
a = Solution()
print(a.findRestaurant(list1, list2))