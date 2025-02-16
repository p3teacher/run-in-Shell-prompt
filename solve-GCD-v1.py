# solve-GCD-v1
# 最大公因數 Greatest Common Divisor
# 2024-02-16
# This repl modify the python code from [STEAM 教育學習網]
# https://steam.oxxostudio.tw/category/python/example/hcf.html
#
# test data 1 : 45,90,180,360
# test data 2 : 27,90,180,360
# test data 3 : 33,96,360,180
#
"""
[STEAM 教育學習網]
什麼是輾轉相除法？
例如求 50 和 80 的最大公因數，
先以   80 除以 50，得到餘數為30;
接著以 50 除以 30，得到餘數為20;
接著以 30 除以 20，得到餘數為10;
最後以 20 除以 10，得到餘數為 0;
10 就是最大公因數。

[50, 80]
80 % 50 , r=30
50 % 30 , r=20
30 % 20 , r=10
20 % 10 , r= 0
got GCD, break ...
GCD is 10
"""
# ex: 60,200,400,600
print('please input 4 numbers separate by ,')
nums = [int(i) for i in input().split(',')]
nums.sort()
divisor = nums[0]                    
while divisor !=1 :
    print(nums)
    now_range = range(1,len(nums))
    print('range is',*now_range,', diversor is',divisor)
    print('')
    for i in range(1,len(nums)):
        print('when i =', i)
        r = nums[i]%divisor     # 取得相除後的餘數
        print('--->', str(nums[i])+' % '+str(divisor)+' , r='+str(r))
        if r !=0:              # 如果相除後餘數不為 0
            nums.insert(0, r)  # 將餘數插入為串列的第一個項目
            break  # 跳出迴圈
        # end if 
    # end for
    # -------------------
    print('')
    #
    if divisor != nums[0]: # 如果divisor不等於串列第一個項目(餘數)
        divisor = nums[0]  # 將result改為第一個項目(餘數)
        print('now nums[0] =', nums[0])
        print('now divisor =', divisor)
    else:
        print('got GCD, break ...')
        break             # 得到最大公因數
    # end if
# end while
#
print('GCD is', divisor)
