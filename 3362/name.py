"""Yerrrrr"""
name_a = input()
name_b = input()

s_name = name_a if len(name_a) < len(name_b) else name_b
l_name = name_b if len(name_b) > len(name_a) else name_a

loop = len(l_name) // len(s_name)
s_name = s_name * loop + s_name[:len(l_name)-(loop*len(s_name))]
yan = [""] * len(l_name)
w_count = 0
w_con = []
consec_w = 0

for i, c_l in enumerate(l_name):
    if s_name[i].lower() in "love" or c_l.lower() in "love":
        yan[i] = "w"
        w_count += 1
        consec_w += 1
    else:
        yan[i] = "$"
        w_con.append(consec_w)
        consec_w = 0

w_con.append(consec_w)

if w_count % 2:
    yan.append(str(max(w_con)))
elif not sum(num > 1 for num in w_con):
    yan.append("#")

print("".join(yan))
