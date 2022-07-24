#code to check numbers that are divisible by 7 and multiples of 5 in the range (1500-2700)

r = range(1500,2700,1)
for i in r:
    i = i
    while i % 7 == 0 and i % 5 == 0:
        print(i)
        i+=1
        
#code to convert temperature in to or from either celsius or fahrenheit

def c_to_f():
	c = float(input("Enter temperature to convert to fahrenheit: "))
	f = (9/5*(c)+32)
	print("Temperature in fahrenheit is ", f)
def f_to_c ():
	f = float(input('Enter temperature to convert to celsius: '))
	c = (f-32)/9*5
	print('Temperature in celsius is ',c)

c_to_f()
f_to_c()
