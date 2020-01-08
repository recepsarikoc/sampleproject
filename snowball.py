from datetime import datetime
s1 = "20200103"
s2 = "20200102"
s_datetime1 = datetime.strptime(s1, '%Y%m%d')
s_datetime2 = datetime.strptime(s2, '%Y%m%d')

print(s_datetime1)
a = [s_datetime1,s_datetime2,s_datetime1,s_datetime2,s_datetime1,s_datetime2]
b = [400, 401, 402, 403, 404, 405]
c = [400, 401, 402, 411, 412]
d = [['kadıköy', 'maltepe', 'ataşehir'], ['kadıköy', 'üsküdar', 'beykoz'],
     ['kadıköy', 'üsküdar', 'beykoz'], ['kadıköy', 'üsküdar', 'beykoz'], ['kadıköy', 'sancaktepe', 'tuzla'],
     ['kadıköy', 'kartal', 'pendik']]
# print(d[5][2])
e = [0, 0, 0, 0, 0, 0]
for i in range(0,7):

    f = datetime.now()
    print(f)
    print(type(f))
    queue = []
    e[i] = f - a[i]
    g = e[i].days + 10
    print(g)

    # hizmet talep edilen bölge
    k = 'kadıköy'
    print(type(e[i]))

    # timedelta olduğu için days kullanılıyor
    print(e[i].days)

    # datetime olduğu için day kullanılıyor
    print(s_datetime1.day)

    if b[i] in c:
        e[i] = e[i].days + 10
    m = 0
    n = 0
    print(len(d))

    for m in range(0, 6):
        for n in range(0, 3):
            if k == d[m][n]:
                print(True)
                e[i] = e[i] + 5
            else:
                print(False)

    # while j < 3:
    # if k in d:
    # print(True)

    queue.append(e[i])

    print(e)
    print('first commit')