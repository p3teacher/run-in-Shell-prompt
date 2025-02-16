# Check-if-N-is-multiple-of-2-3-6
# 2024-06-15
#
N2 = list(range(1001,2001,1))
"""
print(N2)
#
print('-------------------')
N3 = list(range(1008,2001,42))
print(N3)
#
"""
m2 = []
m3 = []
m7 = []
#
for j in N2 :
    if j%2 == 0 :
        m2.append(j)
    # end if 
    if j%3 == 0 :
        m3.append(j)
    # end if
    if j%7 == 0 :
        m7.append(j)
    # end if        
# end for 
#
m23_a = list(set(m2) & set(m3))
m23_b = sorted(m23_a)
print(m23_b)
#
m237_a = list(set(m23_b) & set(m7))
m237_b = sorted(m237_a)
print(m237_b)
print('OK')