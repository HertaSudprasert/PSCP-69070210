"""matrix"""

row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))
row4 = list(map(int, input().split()))
row5 = list(map(int, input().split()))

m1 = [
    row1,
    row2,
    row3,
    row4,
    row5
]

odd_row = -1
odd_col = -1

for i in range(5):
    if sum(m1[i]) % 2:
        odd_row = i

for j in range(5):
    if sum(m1[i][j] for i in range(5)) % 2:
        odd_col = j

print(odd_row, odd_col)
