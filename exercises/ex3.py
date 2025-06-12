# Objective : Convert hours to minutes

def hours_to_minute(x):
    minute = x * 60
    return minute

user_input =input("Enter the hours : ")
hours = int(user_input)

the_minute_is = hours_to_minute(hours) 
print (hours, "hours is" , the_minute_is, "minutes")
