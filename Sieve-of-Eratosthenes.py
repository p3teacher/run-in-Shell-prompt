# Sieve of Eratosthenes
# 埃拉托斯特尼篩法 (sieve of Eratosthenes)
# 這是一種簡單且歷史悠久的篩法，用來找出一定範圍內所有的質數。
#
# 2024-02-16
"""
範例出處 :「STEAM 教育學習網」
=============================
昌爸工作坊
http://www.mathland.idv.tw/fun/primetable.html
=============================
"""
# 產生 2～100 的串列
a = range(2, 200)
print('')
#
"""
b = []
for i in a:
    if (i == a[0]) or ( i%a[0]>0) :
        b.append(i)
    #
#
print('')
print(b)
"""
# 找出第一個質數，並將串列裡該質數的倍數剔除
b = [i for i in a if i==a[0] or i%a[0]>0]
print(type(b))
#print(*b)
print('')
#
# 找出第二個質數，並將串列裡該質數的倍數剔除
c = [i for i in b if i==b[1] or i%b[1]>0]   
#print(*c)
print('')
#

# 找出第三個質數，並將串列裡該質數的倍數剔除
d = [i for i in c if i==c[2] or i%c[2]>0]
#print(d)
print('')
#

# 找出第四個質數，並將串列裡該質數的倍數剔除
e = [i for i in d if i==d[3] or i%d[3]>0]
print(e)
print('')