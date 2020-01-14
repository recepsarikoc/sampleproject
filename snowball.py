from datetime import datetime
s = "20200103"
s_datetime = datetime.strptime(s, '%Y%m%d')
print(s_datetime)
a = [s_datetime,s_datetime,s_datetime,s_datetime,s_datetime,s_datetime]
b = [400, 401, 402, 403, 404, 405]
c = [400, 401, 402, 411, 412]
d = [['kadıköy', 'maltepe', 'ataşehir'], ['kadıköy', 'üsküdar', 'beykoz'],
     ['kadıköy', 'üsküdar', 'beykoz'], ['kadıköy', 'üsküdar', 'beykoz'], ['kadıköy', 'sancaktepe', 'tuzla'],
     ['kadıköy', 'kartal', 'pendik']]
# print(d[5][2])
e = [0, 0, 0, 0, 0, 0]
f = datetime.now()
print(f)
print(type(f))
i = 0
j = 0
queue = []
e[i] = f - a[i]
g = e[i].days + 10
print(g)

#hizmet talep edilen bölge
k = 'kadıköy'
print(type(e[i]))

#timedelta olduğu için days kullanılıyor
print(e[i].days)

#datetime olduğu için day kullanılıyor
print(s_datetime.day)

if b[i] in c:
    e[i] = e[i].days + 10

if j < 3:

    if k == d[m][n]:
        e[i] = e[i] + 5
    j = j+1

queue.append(e[i])

print(e)