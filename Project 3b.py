# Author: Faith Elledge
# Grithub username: Elledgef
# Date: 4/13
# Description: This code finds the numbers that divides into the integer evenly
num = int(input("Please enter a positive integer"))
print("The factors of " +str(num)+" are:")
#Added 1 to include one in the factors
for i in range(1,num+1):
    if num % i ==0:
        print(i)