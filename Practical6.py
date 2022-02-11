#Code written by 20CE072 Nirava Parikh
"""AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. 
See the sample input/output for clarification. 
Sample Input 
4 
bcdef 
abcdefg 
bcde 
bcdef 
Sample Output 
3 
2 1 1 """
from contextlib import nullcontext


s = []
n = int(input())
for i in range(0,n):
    ele = input()
    s.append(ele)
st = []
for i in s:
    if i not in st:
        st.append(i)

print(s)
print(st)
print(len(st))
for i in st:
    cnt=0
    for j in s:
        if i==j:
            cnt = cnt+1
    print(cnt)

