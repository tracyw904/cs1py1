# cs1py1
# cs1py1

# 9/25/2023-- using print for math
pi = 3.141
r = float(input("Please enter value: ")) 
print(r)

area = pi*r*r 

print(area)


# 9/27/2023 LOOPS- process that we use to do repeated work. example: 

x = input()
for r in range(len(x)):  
    print(x[r])

0/2 booleans, comparison operators 
x = 5
print(x==5)
print(x!=4)
print(x==6)
print(x!=6)
'''
# else and if statements

x=5
if x==100:
    print("yes this is true")
else:
    print("slay")
print("completed")

# print values -- range for all numbers, elseif, conditions
for x in range(10):
    #print(x)    
    if x%2== 1:
        print(x, " is an odd number")
    else:
        print(x, " is an even number")
        '''

# NESTED conditions!: conditions that have conditions have conditions 
for x in range(10):
    #print(x)    
    if x%2== 1:
        if x>5:
            print("x, this is larger than 5")
    print(x, " is an odd number")
else:
    print(x, " is an even number") 
