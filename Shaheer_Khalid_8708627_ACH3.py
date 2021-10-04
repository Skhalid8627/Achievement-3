#Get user input 
print("Please enter a even number")
num = int(input())
#Variable to store my calculatuon  
a = 0
#This will be my iterator 
i = 0

while i <= num:
    a = a + (i*i)
#as we need to get every other number for the 'even number requirement' which requires double incrementation
    i += 2         

print(a)

