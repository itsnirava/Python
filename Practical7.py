#code written by 20ce072 Nirava Parikh
"""Lapindrome is defined as a string which when split in the middle, gives two halves having the same 
characters and same frequency of each character. If there are odd number of characters in the string, 
we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, 
since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and 
xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the
same characters but their frequencies do not match. Your task is simple. Given a string, you need to tell
if it is a lapindrome. 
Input: 
6 
gaga 
abcde 
rotor 
xyzxy 
abbaab 
ababc 
Output: 
YES 
NO 
YES 
YES 
NO 
NO"""

n = int(input())
s = []
st = []
st1 = []
for i in range(0,n):
    t = input()
    s.append(t)
mid = 0
if n%2!=0:
    mid = int(n/2)
    for i in range(0,mid+1):
        st.append(s[i])
    for i in range(mid,n):
        st1.append(s[i])
else: 
    mid = int(n/2)
    for i in range(0,mid):
        st.append(s[i])
    for i in range(mid,n):
        st1.append(s[i])

print(st)
print(st1)
