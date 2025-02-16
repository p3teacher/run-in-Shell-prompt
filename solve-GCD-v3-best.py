# solve-GCD-v3-best
# 最大公因數 Greatest Common Divisor
# 2024-02-16
#
import math #type:ignore
from platform import python_version
print('the python version is',python_version())
#
# for Python 3.9 and after version
# math.gcd() can accept more than 3 parameter
#
"""
什麼是輾轉相除法？
例如求 50 和 80 的最大公因數，
先以   80 除以 50，得到餘數為30;
接著以 50 除以 30，得到餘數為20;
接著以 30 除以 20，得到餘數為10;
最後以 20 除以 10，得到餘數為 0;
10 就是最大公因數。
"""
#
n_list = [6,15,30]
n_list = [9,18,72]
n_list = [18,72,90]
n_list = [18,72,90,9]
n_list = [18,72,90,108]
#
n = len(n_list)
i_range = range(0,n-1,1)
#
print(n_list)
print('')
gcd_list = [n_list[0]]
for i in i_range :
    print('i=', i)
    print('--->', gcd_list[i], n_list[i+1])
    GCD = math.gcd(gcd_list[i], n_list[i+1])
    gcd_list.append(GCD)
    print('---> GCD is', GCD)
# end for
#
print('')
print(gcd_list)
print('GCD is', gcd_list[-1])