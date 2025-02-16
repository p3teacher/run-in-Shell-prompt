# Check-if-N-is-multiple-of-11-v1
# 2024-02-16
#
N4 = list(range(11,1112,1))
m11 = []
#
for j in N4 :
    if j%11 == 0 :
        m11.append(j)
    # end if    
# end for 
#
print(m11)
print(len(m11))
print('')
#
m11 = range(11,1112, 11)
m11_list = list(m11)
print(m11_list)
#
print('Enter number between 11 ~ 1111:')
num = input()
print(num, 'is', type(num))
#
if int(num) in m11_list :
    print(num, "is multiple of 11")
else :
    print(num, "is not multiple of 11")
# end if