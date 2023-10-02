'''
10/2 booleans, comparison operators 
x = 5
print(x==5)
print(x!=4)
print(x==6)
print(x!=6)
'''
#else and if statements
'''
x=5
if x==100:
    print("yes this is true")
else:
    print("slay")
print("completed")

#print values -- range for all numbers, elseif, conditions
for x in range(10):
    #print(x)    
    if x%2== 1:
        print(x, " is an odd number")
    else:
        print(x, " is an even number")
        '''

# NESTED condition!
for x in range(10):
    #print(x)    
    if x%2== 1:
            if x>5:
                print("x, this is larger than 5")
    print(x, " is an odd number")
else:
    print(x, " is an even number")