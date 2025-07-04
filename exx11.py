def add_nums (num1,num2):
    sum= num1 +num2 
    return sum
first_num = input("Enter your first num : " )
second_num = input ("Enter your second num : ")

first_num=int (first_num)
second_num= int(second_num)
sum= add_nums(first_num,second_num)
print (f"Sum of {first_num} and {second_num} is {sum}")