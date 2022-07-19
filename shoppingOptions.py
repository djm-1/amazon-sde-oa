"""
Alternative Question: Find All Combination of Numbers Sum to Target

Given a positive integer, target, print all possible combinations of positive integers that sum up to
the target number.

For example, if we are given input ‘5’, these are the possible sum combinations.

1, 4
2, 3
1, 1, 3
1, 2, 2
1, 1, 1, 2
1, 1, 1, 1, 1

The output will be in the form a list of lists or an array of arrays. Each element in the list will be another list
containing a possible sum combination.

Hint
===============
Recursion
Two lists
"""
import copy

def print_all_sum_rec(target, current_sum, start, output, result):
    if current_sum == target:
        output.append(copy.copy(result))
        
    for i in range(start, target):
        temp_sum = current_sum + i
        if temp_sum <= target:
            result.append(i)
            print_all_sum_rec(target, temp_sum, i, output, result)
            result.pop()
        else:
            return 
        

def print_all_sum(target):
    output = []
    result = []
    
    print_all_sum_rec(target, 0, 1, output, result)
    return output

n = 4
res = print_all_sum(n)
print(res)