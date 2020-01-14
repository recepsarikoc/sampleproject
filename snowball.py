from datetime import datetime

a = [1,20,30,4,3,2]  # medic i nin son görülme tarihi ile içinde bulunduğumuz günün farkının değeridir
b = [400, 401, 402, 403, 404, 405]
c = [400, 401, 402, 411, 412]  # öne çıkarılacak medic listesi
d = [['kadıköy', 'maltepe', 'ataşehir'], ['kadıköy', 'üsküdar', 'beykoz'],
     ['kadıköy', 'üsküdar', 'beykoz'], ['kadıköy', 'üsküdar', 'beykoz'], ['kadıköy', 'sancaktepe', 'tuzla'],
     ['kadıköy', 'kartal', 'pendik']]
# print(d[5][2])
e = [0, 0, 0, 0, 0, 0]
for i in range(0,6):

    f = 0 #içinde bulunduğumuz günü temsil eder
    e[i] = f - a[i]
    k = 'kadıköy'

    if b[i] in c:
        e[i] = e[i] + 10
    m = 0
    n = 0
    print(len(d))
#d iki boyutlu bir dizidir m ve n indisleri ve for döngüsüyle bu dizide dolaşıyor ve kontrollerimi yapıyorum
    for m in range(0, 6):
        for n in range(0, 3):
            if k == d[m][n]:
                print(True)
                e[i] = e[i] + 5
            else:
                print(False)

    print('puanlar')
    print(e)
