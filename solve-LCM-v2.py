# solve-LCM-v2
# 最小公倍數 (Least Common Multiple)
# 2024-02-16
#
"""
「公倍數」是指不同數字間共同的倍數，
而最小公倍數，就是這些倍數裡最小的那個數字。
"""
# 
import math  #type:ignore
from platform import python_version
print('the python version is',python_version())
#
# for Python 3.9 and after version
# math.lcm() can accept more than 3 parameter
#
# a*b = math.gcd(a,b) * LCM
# LCM = a*b / math.gcd(a,b)
#
n_list = [6,15,30]
n_list = [9,18,72]
n_list = [18,72,90]
n_list = [18,72,90,108]
n_list = [18,63,90,27]
n_list = [18,72,90,9]
#
n = len(n_list)
i_range = range(0,n-1,1)
#
print(n_list)
print('')
lcm_list = [n_list[0]]
for i in i_range :
    print('i=', i)
    print('--->', lcm_list[i], n_list[i+1])
    LCM = int(lcm_list[i]*n_list[i+1] / 
               math.gcd(lcm_list[i], n_list[i+1])
              )
    print('---> LCM is', LCM)
    lcm_list.append(LCM)
# end for
#
print('')
print(lcm_list)
print('LCM is', lcm_list[-1])
