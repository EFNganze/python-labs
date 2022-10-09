print('Hello World!')

LAB 2.1
a = int(input("write a number"))
b = int(input("write another number"))
if (a < b) :
     print(a)
elif (b < a) :
      print(b)
else :
      print("the numbers are equal")
    
    LAB 2.2
    
a = float(input("enter first number"))
b = float(input("enter second number"))
c = float(input("enter third number"))
if (a >= b) and (a >= c) :
    print(a)
elif (b >= a) and (b >= c) :
    print(b)
else :
    print(c)
    
    LAB 2.3



a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
numbers = [a,b,c]
unique_elements = []
for i in numbers:
    if i not in unique_elements:
        unique_elements.append(i)
print(f'существует {len(unique_elements)} уникальные элэменты ')

     
     

    
    
       
