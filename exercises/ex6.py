#Check if the number is prime 

def is_prime(num):
    if num < 2:
        return False
    for i in range (2, num):
        if num%i ==0:
            return False      
    return True 

user_input = input ("Enter a number : ")
num = (user_input)
if is_prime(num):
    print(num , "is prime")
else: 
    print(num ,"isn't prime")


   
    
     
    
   
    