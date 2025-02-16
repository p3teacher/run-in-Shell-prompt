# Fibonacci Sequence
# 2024-02-16
#
"""
Q:
un-sortted /unformated imports error!!!
---------------------------------------
A:
go to pyproject.toml and remove the 
'I' from the select variable list
"""
# 
import math
#
def fib(n) :
    if n==0 :
        return 0
    # end if
    if n==1 or n==2 :
        return 1
    # end if
    return (fib(n-1)+fib(n-2))
# end def
#
def factorial_recursive(n) :
    if n == 1 :
        return 1
    else :
        return n*factorial_recursive(n-1)
    # end if
# end def
#
n = int(input('請輸入費氏數列項數N: '))
print('')
range_n = range(n)
print(*range_n)
print('')
#
for i in range(n+1) :
    print('fib(%d)=%d' %(i,fib(i)))
# end for
#
# pow(x,y) 方法返回 xy（x的y次方）的值。
print('')
for i in range(1,n+1) :
    print('power(2,%d) = %d' %(i,math.pow(2,i)))
# end for
#
print('')
for i in range(1,n+1) :
    print('%d! = %d' %(i,factorial_recursive(i)))
# end for
#
print('')
print('done')