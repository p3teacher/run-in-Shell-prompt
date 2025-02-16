# factorial-recursive
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
def factorial_recursive(n) :
    if n == 1 :
        print(str(n)+'! <-- 值是1')
        return 1
    else :
        print(str(n)+'*('+str(n-1)+')!')
        return n*factorial_recursive(n-1)
    # end if
# end def
#
n = 7
value = factorial_recursive(n)
print('Answer:')
print('階乘'+str(n)+' =', value)
print('')
n = 6
value = factorial_recursive(n)
print('Answer:')
print('階乘'+str(n)+' =', value)
print('')
print('done')