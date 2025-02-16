# # prime-factorization-1
#
# prime factorization (質因數分解)
# 質因數分解：將一個整數表示成其質因數的乘積，稱為此整數的質因數分解。
# 2024-02-16
#
"""
文章範例出處 :「STEAM 教育學習網」
=============================
當使用者輸入數字後，判斷數字是否為質數，如果不是質數，就將其做質因數分解。

[基本原理]
質因數分解的原理，就是透過迴圈的方式，
將使用者輸入的數字，
依序除以 2、3、4...一直到數字本身，
如果可以被整除，表示這個數字不是質數，
整除後再將商依序除以 2、3、4...，
不斷重複這個步驟，就能進行直因數分解。
"""
# prime number
# 97, 101, 997, 3331, 3533,
# 4999, 9001, 9901, 9973
#
# 4891 = 67*73
a = b = int(input('請輸入一個正整數：')) 
# 新增a和b變數，等於使用者輸入的數字
output = ''                           
# 新增 output 變數，作為輸出的文字
while True:
    for i in range(2,(a+1)):
        print('a is',a,', i is', i)
        if i==b: # 如果 i等於b，表示是質數，跳出 for 迴圈
            print('i = b')
            break
        # end if
        if a%i==0: # 如果可以被 i 整除，表示不是質數
            # print(a, ' can be divide by', i, ', 不是質數')
            output += f'{i}' # 設定 output 輸出的內容
            if i < a :
                print(a, ' can be divide by', i, ', 不是質數')
                print('')
            else :
                print(a, ' can be divide by', i)
                print('')
            # end if
            a = int(a/i)   # 重新將 a 設定為商
            break    # 跳出 for 迴圈
        # end if
    # end for
    #
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
# end if
#
