# prime-factorization-2
#
# prime factorization (質因數分解)
# 質因數分解：
# 將一個整數表示成其質因數的乘積，稱為此整數的質因數分解。
# 2024-02-16
# 
import math  #type:ignore
from platform import python_version
print('the python version is',python_version())
#
# nani 7up, page 155, Question 1
# 4891 = 67x73
# 7387 = 83x89
#
# print(101*4999)
a = b = int(input('請輸入一個正整數：')) 
# 新增a和b變數，等於使用者輸入的數字
output = ''                           
# 新增 output 變數，作為輸出的文字
while True:
    for i in range(2,(a+1)):
        if i==b: # 如果 i等於b，表示是質數，跳出 for 迴圈
            break
        # end if
        if a%i==0: # 如果可以被 i 整除，表示不是質數
            output += f'{i}' # 設定 output 輸出的內容
            a = int(a/i)     # 重新將 a 設定為商
            print(i)
            break    # 跳出 for 迴圈
        # end if
    # end for
    if a==1 or a==b: # 如果商等於 1 或是質數，跳出 while 迴圈
        break
    else:
        output += '*'# 否則在 output 後方加上 * 號，繼續 while 迴圈
    # end if
# end while
#
# while 迴圈結束後
if a == b:  # 如果 a 等於 b
    print(f'{b} 是質數')     # 印出質數的文字
else:
    print(f'{b}={output}')  # 印出質因數分解的結果
    print(f'{b} 不是質數')
# end if
#
