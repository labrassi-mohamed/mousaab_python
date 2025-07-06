num= 266
str_num =str (num)
len_num = len(str_num)

arm_strongnum =  sum(int(digit)**len_num for digit in str_num)
if num == arm_strongnum :
    print (f"{num} is an armstorong number ")
else :
    print (f"{num} is not an armstorong number ")