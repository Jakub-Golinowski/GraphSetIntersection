
a = [
    (1, 1071.38),
    (2, 1166.93),
    (3, 1114.43),
    (4, 1108.32),
    (5, 1113.55),
    (6, 1213.98)
]

b = [
    (1, 2554.25),
    (2, 2787.00),
    (3, 5993.86),
    (4, 8984.40),
    (5, 14027.83),
    (6, 17556.73) ,
]

for i in xrange(0, 6):
    ta = a[i][1]
    tb = b[i][1]
    rel_sp = tb / ta
    print("(%d, %.3f)"% (i + 1, rel_sp))