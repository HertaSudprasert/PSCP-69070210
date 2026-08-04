"""afasf"""

kananruam = float(input())
kanan_sungsud = float(input())

kananmin = kananruam - kanan_sungsud * 2

if kananmin < 0:
    kananmin = 0

if kanan_sungsud - kananmin > 2:
    print("Surprising")
else:
    print("Not surprising")
