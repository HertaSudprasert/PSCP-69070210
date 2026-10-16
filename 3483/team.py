"""gdsgdsg"""

n, m = map(int, input().split())
incorrect = False
if n < 1 or n > 10 or m < 1 or m > 20:
    incorrect = True
overall_score = 0
teams = []

for _ in range(n):
    total = 0
    highest = 0

    for score in list(map(int, input().split())):
        if score < 0 or score > 100:
            incorrect = True
        if incorrect:
            break

        total += score
        highest = max(highest, score)
    overall_score += total
    teams.append({"Average": total / m, "Max": highest})

if incorrect:
    print("Data Incorrect")
else:
    for i, team in enumerate(teams):
        print(f"Team {i + 1}: Average = {team['Average']:.2f}, Max = {team['Max']}")

    print(f"Total Score of All Teams = {overall_score}")
