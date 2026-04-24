from datetime import time,datetime,date,timedelta
"""a=datetime(2026,12,5)
print(a.strftime("%A,%d."
"%b.%y"))"""


"""a="15 08 2024"
b=datetime.strptime(a, "%d %m %Y")
print(b)"""
"""
a=datetime.now()
b=a+timedelta(hours=320)
print(b.strftime("%d"))
"""
"""
a = datetime.now()
new_time = b.replace(hour=21, minute=30, second=0,microsecond=0)

print(new_time)"""

"""from datetime import datetime, timedelta

now = datetime.now()

# set 9:30 PM
target = now.replace(hour=21, minute=30, second=0, microsecond=0)

# handle past time

if now > target:
    target = target + timedelta(days=1)

# convert both to timestamp
now_ts = now.timestamp()
target_ts = target.timestamp()

# difference in seconds
diff_seconds = target_ts - now_ts

# convert to minutes
minutes = diff_seconds // 60

print(int(minutes))"""

"""a=datetime.now()
b=a.replace(hour=18,minute=00,second=00)
c=a.timestamp()
d=b.timestamp()
d=d-c
minutes=d//60
print(minutes)"""

"""a=datetime.now()
b=a+timedelta(minutes=135)
print(b.hour)"""

"""a=datetime.now()
print(a.strftime("%IH:%MM %p"))
"""

"""d=datetime(2026,2,1)
a=datetime.now()
res=("future"if d>a else "past")
print(res)"""

"""a=date(2004,9,12)
b=date.today()
c=b-a
d=c/365
print(d.days)"""
"""
a=datetime(2026,3,29)
b=a.strftime("%w")
print(b)
if(b=="0" or b=="6"):
    print("Weekend")
else:
    print("weekday")
"""
"""from datetime import datetime, timedelta

now = datetime.now()

# Step 1: go to first day of next month
next_month = now.replace(day=28) + timedelta(days=4)
print(next_month)
# Step 2: go back to last day of current month
last_day = next_month - timedelta(days=next_month.day)

print(last_day.day)

"""
a=date.today()
next_month=a.replace(day=28) + timedelta(days=4)


