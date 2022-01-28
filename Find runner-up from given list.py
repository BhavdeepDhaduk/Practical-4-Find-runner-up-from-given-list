"""BHAVDEEP DHADUK -20CE024
Practical 4: Find runner-up from given list"""

print("Name :- Bhavdeep Dhaduk\nRollno :- 20CE024")
n = int(input())

set_1 = set(map(int,input().split()))

print(list(set_1)[-2])