"""saitama"""

import math

widpeun = int(input())
situp = int(input())
looknung = int(input())
wing = int(input())

can_widpeun = int(input())
can_situp = int(input())
can_wing = int(input())
can_looknung = int(input())

wid_peun_time = widpeun / can_widpeun
situp_time = situp / can_situp
looknung_time = looknung / can_looknung
wing_time = wing / can_wing

min_time = max(wid_peun_time, situp_time, looknung_time, wing_time)

print(math.ceil(min_time))
