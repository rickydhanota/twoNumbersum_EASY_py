# write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. if no two numbers sum up to the target sum, the function should return an empoty arrya

# The tagrte sum has to be obtained by summing teo different integers in the array; you cant add a single integer in the array to the same integer. You can assume that there will be at most one pair of numbers summing up to the target sum


def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i]+array[j] == targetSum:
                return [array[i], array[j]]
    return []
                

print(twoNumberSum([ 3, 5, -4, 8, 11, 1, -1, 6], 10))