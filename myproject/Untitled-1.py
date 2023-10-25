#1. 
#a) definite loop vs. indefinite loop: both these are the same they go through loops but defintie loops has a number of times it goes through loops unlike indefinite loops 
#b) for loop vs. while loop: both these are the same they go through loops but for loops has a range of times it goes through. unlike while loops goes through until its false 
#c) interactive loop vs. sentinel loop: interactive loops interact with the user, taking input and providing output during the loop's execution. Sentinel loops rely on a specific value to terminate the loop. Both are indefinite loops
#d) sentinel loop vs. end-of-file loop: Both are indefinite loop but end of file loops reads a file while loops thats what makes them both different 
#2 
#a)
v = [True, False]
for P in v:
    for Q in v:
      pr=not(P and Q) 
print(pr) 
#b 
for P in v:
    for Q in v:
     pr1=(not P) and Q  
print(pr1) 
#c 
for P in v:
    for Q in v:
     pr2=(not P) or (not Q) 
print(pr2) 
#d 
for P in v:
    for Q in v:
     for R in v:
      pr3=(P and Q)or R   
print(pr3)    
#e 
for P in v:
    for Q in v:
     for R in v:
      pr4=(P or R) and (Q or R) 
print(pr4) 
#3 
#a. 
num = int(input("Enter a number: ")) 
lot = 0  
now = 1  

if num <= 0:
    print("Please enter a positive integer.")
else:
    while now <= num:
        lot += now  # Add the current number to the sum
        now += 1  # Move to the next number

    print(f"The sum of the first {num} counting numbers is: {lot}") 
#c 
x=0
while x <999: 
 t=eval(input('enter numbers until it reaches 999: ')) 
 x += t 

#4 
n = eval(input('enter a positive integer:')) 
prev = 1
fib = 1 
for i in range(2,n): 
  temp = prev 
  prev=fib 
  fib = temp + fib 

print(f"the value of fibonacci {n} is {fib}") 

#5
z=eval(input('enter a number:')) 
sequence = [z]
while z != 1:
        if z % 2 == 0:
            z = z // 2  
        else:
            z = 3 * z + 1 
        sequence.append(z)  
print(sequence)      
git --clone