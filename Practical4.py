#Code written by 20ce072 Nirava Parikh
#Problem Statement:
"""Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given n scores.
Store them in a list and find the score of the runner-up.
Input Format: The first line contains.
              The second line contains an array A[] of n integers each separated by a space.
Output Format: Print the runner-up score.
Sample Input
5
2 3 6 6 5
Sample Output
5
Explanation: Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5.
Hence, we print 5 as the runner-up score.
"""

from audioop import reverse


n = int(input())
arr = input()  
l = list(map(int,arr.split(' ')))
lst = list(arr)
lst.sort()
max = lst[n-1]
lst.reverse()
for i in lst:
    if i!=max:
        print("Runner Up: "+ i)
        break
