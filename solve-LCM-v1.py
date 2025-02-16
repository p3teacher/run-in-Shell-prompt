# solve-LCM-v1
# 最小公倍數 (Least Common Multiple)
# 2024-02-16
#
# This repl modify the python code from [STEAM 教育學習網]
"""
[STEAM 教育學習網]
「公倍數」是指不同數字間共同的倍數，而最小公倍數，就是這些倍數裡最小的那個數字。
"""
# 
# test data1 : 20,5,10
# test data2 : 15,9,30
#
nums = [int(i) for i in input('輸入數字(逗號分隔): ').split(',')]
nums.sort(reverse=True)  # 將串列從大到小排序
print(nums)
print()
# ----------------------------------------------
LCM = nums[0]   # 設定「暫定的最小公倍數」為最大的數字
while True:     
    r = 0
    for i in nums:     # 依序取出串列中的每個數字
        r = LCM % i    # 用「暫定的最小公倍數」除以每個數字，求出餘數
        if r != 0:     # 如果餘數不為0，跳出for迴圈
            print('when LCM =', LCM)
            print('---> '+str(LCM)+' % '+str(i)+ ' , 餘數不為0')
            break
        # end if
        print('when LCM =', LCM)
        print('---> '+str(LCM)+' % '+str(i)+ ' , 餘數為0')
    # end for
    #
    if r == 0: 
        # 跳出 while 迴圈
        break
    else:
        # 將「暫定的最小公倍數」加上最大的數字
        LCM = LCM + nums[0] 
        print('')
    # end if
# end while
#
print('')
print('exit while ...')
print('LCM is', LCM)
