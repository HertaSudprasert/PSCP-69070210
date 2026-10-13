"""shorten"""

hmm = []

num = 0
while num != -1:
    num = int(input())
    if num != -1:
        hmm.append(num)

result = []
if hmm:
    start = hmm[0]
    end = hmm[0]
    for i in range(1, len(hmm)):
        if not hmm:
            print("")
            break
        if hmm[i] == end + 1:
            end = hmm[i]
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}-{end}")

            start = hmm[i]
            end = hmm[i]

    if start == end:
        result.append(str(start))
    else:
        result.append(f"{start}-{end}")
else:
    print("")

print(", ".join(result))
