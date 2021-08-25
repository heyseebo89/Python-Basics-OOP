#type of data type in python it is already defined so no need to.
print("haseeb")
type("haseeb")
#assignment opertor
a=100 #here the value 100 is given to a
b=100 #here the value 200 is given to b
a = 100  
b = a  
print(id(a)) 
print(id(b))
m = 100000000000000000
m = m+10000000000
print(type(m))
print(m)
#naming a variable 
name = "haseeb"
NaMe = "haseeb"
n_a_m_e = "haseeb"
#should not start with numbers
#local variaable
def Myadd():  
    m = 5  
    n = 4 
    p = m * n 
    print("The product  is:", p)    
Myadd()
print(m)
#global variable
# here we globally declare the value 
x = 100
def nfunction():
    global x
    print(x)
    del(x)
    print(x)