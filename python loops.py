#loops are used to perform a task by iterating to numerous no of times
#if statements
num = 50
if num >10:
    print("the number is geater than 10")
else:
    print("the number is less than 10")
#if elif else 
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

#here is how to find the sum of all nubers in a list
numbers = [1,2,3,4,5]
#first we will take a variable sum and assign 0 vaue to it 
sum = 0
for val in numbers :
    sum = sum+val
print("the sum is ,sum")
#printing nmbers in range
print(range(20))
print(list(range(2,10)))

#while loop in python
sum = 0
i = 1
n = 10
while i<=n:
    sum = sum + i
    i = i+1
    print("the sum is ,sum")
for val in "haseeb":
    if val == "s":
        break
    print(val)
