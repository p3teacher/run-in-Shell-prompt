# solve-GCD-v2
# 最大公因數 Greatest Common Divisor
# 2024-02-16
#
# test data 1 : 45,90,180,360
# test data 2 : 27,90,180,360
# test data 3 : 33,96,360,180
#
# This version is focus on log.txt file
#
import os
from datetime import datetime
#
path = os.getcwd()
script_path = os.path.realpath(__file__)
script_dir  = os.path.dirname(script_path)
#
class FileLogger:
    def __init__(self, filePath): 
        try:
            open(filePath, 'w').close()
            self.filePath = filePath
        except:
            raise Exception("Could not open/create file = " + filePath)
    # end def
    #
    def print(self, text):
        with open(self.filePath, 'a') as txtFile:
            txtFile.writelines(text + '\r\n')
    # end def
# end class
#
dt_start = datetime.now()
logger = FileLogger("./log.txt")
logger.print('replit.com Python Script')
logger.print('start running at ' + str(dt_start))
logger.print('當前工作目錄 ==> ' + path)
logger.print('script dir ==> ' + script_dir)
logger.print('')
logger.print('[輾轉相除法求最大公因數]')
#
"""
[STEAM 教育學習網]
什麼是輾轉相除法？例如要求 50 和 80 的最大公因數，先以 80 除以 50，得到餘數為30；再以 50 除以 30得到餘數為20；接著以 30 除以 20 得到餘數 10，最後 20 除以 10 的餘數為 0，10 就是最大公因數。
[50, 80]
80 % 50 , r=30
50 % 30 , r=20
30 % 20 , r=10
20 % 10 , r= 0
got GCD, break ...
GCD is 10
"""
print('please input 4 numbers separate by ,')
nums = [int(i) for i in input().split(',')]
nums.sort()
divisor = nums[0]                    
while divisor !=1 :
    now_range = range(1,len(nums))
    my_range = str(now_range)
    logger.print(str(nums))
    logger.print('for i in '+my_range)
    logger.print('')
    for i in range(1,len(nums)):
        logger.print('when i ='+str(i))
        r = nums[i]%divisor     # 取得相除後的餘數
        logger.print('--->'+str(nums[i])+' % '+str(divisor)+' , r='+str(r))
        if r !=0:              # 如果相除後餘數不為 0
            nums.insert(0, r)  # 將餘數插入為串列的第一個項目
            break  # 跳出迴圈
        # end if 
    # end for
    # -------------------
    logger.print('')
    #
    if divisor != nums[0]: # 如果divisor不等於串列第一個項目(餘數)
        divisor = nums[0]  # 將result改為第一個項目(餘數)
        logger.print('now nums[0] ='+str(nums[0]))
        logger.print('now divisor ='+str(divisor))
    else:
        logger.print('got GCD, break ...')
        break  # 得到最大公因數
    # end if
# end while
#
logger.print('GCD is '+str(divisor))
print('')
print('GCD is', divisor)
