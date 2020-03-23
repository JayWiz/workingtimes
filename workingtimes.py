from datetime import datetime
from datetime import timedelta

FMT = "%H:%M:%S"

def calculateTimespan(s1, s2):
    d1 = datetime.strptime(s1, FMT)
    d2 = datetime.strptime(s2, FMT)
    return (d2 - d1)

print("Ankunftszeit?")
a1 = input()
print("Abfahrtszeit?")
a2 = input()

a = calculateTimespan(a1, a2)

f1 = datetime.strptime("09:04:00", FMT)
f2 = datetime.strptime("09:07:00", FMT)
f = f2 - f1

m1 = datetime.strptime("12:00:00", FMT)
m2 = datetime.strptime("12:00:00", FMT)
m = m2 - m1

p = f + m

if a.seconds / 3600 > 6 and \
    a.seconds / 3600 < 9:
    if p.seconds / 60 < 30:
        p = timedelta(minutes=30)
elif a.seconds / 3600 > 9:
    if p.seconds / 60 < 45:
        p = timedelta(minutes=45)

s = timedelta(hours=8)    
g = a - s - p

print("Arbeitszeit: %s, Pausenzeit: %s, Gleitzeit: %s" % \
    (str(a), str(p), str(g)))

