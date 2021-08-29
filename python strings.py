#strings in python
s = 'haseeb'
print(s[:],"\n")
first_three_chars = s[:3]
second_to_third_char =s[1:3]
print("second to third :",second_to_third_char ,"\n")
print("irst_three_chars" ,first_three_chars,"\n")
#REVERSE STRING
s="haseeb"
reverse_str= s[::-1]
print(reverse_str)
s1 = s[1:5:2]
print(s1)
s= 'thisisoopclass'
s1=s[-10:-5]
print(s1)
py_string = 'Python book'
slice_object = slice(3) 
print("substring is : ", py_string[slice_object])