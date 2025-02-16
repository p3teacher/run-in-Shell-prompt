# Check-if-N-is-multiple-of-2-3-6
# 2024-02-19
#
# try this repl in Shell
# keyboard input : 
# python Check-if-N-is-multiple-of-2-3-6.py
#
N1 = range(1,51,1)
print("N1 is", type(N1))  # Class 類別
print(N1)
print('')
print(*N1)
print('')
# 
N2 = list(range(1,51,1))
print("N2 is", type(N2))  # Class 類別
print(N2)
print('-----------------------------------')
print('')
#
multiple_of_2 = []  # 空串列
for j in N2 :
    if j%2 == 0 :
        multiple_of_2.append(j)
    # end if 
# end for 
#
print(multiple_of_2)
print('')
n2 = list(range(2,51,2))
print(n2)
print('-----------------------------------')
print('')
#
multiple_of_3 = []
for j in N2 :
    if j%3 == 0 :
        multiple_of_3.append(j)
    # end if 
# end for 
#
print(multiple_of_3)
print('')
multiple_of_6 = list(range(6,51,6))
print(multiple_of_6)
print('')
#
m2 = []
m3 = []
m6 = []
N3 = list(range(51,201,1))
#
for j in N3 :
    if j%2 == 0 :
        m2.append(j)
    # end if 
    if j%3 == 0 :
        m3.append(j)
    # end if
    if j%6 == 0 :
        m6.append(j)
    # end if        
# end for 
#
print('-----------------------------------')
print(len(m2))
print(len(m3))
print(len(m6))
print('')
print(m6)
print('')
print('-----------------------------------')
print('')
#
m6_a = list(set(m2) & set(m3))
m6_b = sorted(m6_a)
print("m6_a is")
print(m6_a)
print('')
print("m6_b is")
print(m6_b)
print('')
print('-----------------------------------')
print('')
#
m3 = []
m5 = []
m8 = []
N3 = list(range(51,301,1))
#
for j in N3 :
    if j%3 == 0 :
        m3.append(j)
    # end if 
    if j%5 == 0 :
        m5.append(j)
    # end if
    if j%8 == 0 :
        m8.append(j)
    # end if        
# end for 
#
print(len(m3))
print(len(m5))
print(len(m8))
print('')
print('+++++')
print('')
#
m_35   = list(set(m3) & set(m5))
m_35_a = sorted(m_35)
print(m_35_a)
print('')
#
m_358_a   = list(set(m_35_a) & set(m8))
m_358_b = sorted(m_358_a)
print("m_358_a is")
print(m_358_a)
print('')
print("m_358_b is")
print(m_358_b)
print('')