"""skul"""

school = input()

school_list = school.split()

first = school[0]
last = school[-1]

asc_first = ord(first)
asc_last = ord(first)

for i in school:
    if i % 2:
        school_list[i] = i + asc_first
    else:
        school_list[i] = asc_last - i

for j in school_list:
    if j % 10 > 9:
        j = j % 10
    school_list = j % len(school)

