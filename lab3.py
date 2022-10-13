lab3.1
a_list =[]
print("enter 10 numbers")
for i in range(10):
    list_i =float(input("enter a number"))
    a_list.append(list_i)
    print(sum(a_list))
    
    
    lab3.2
numbers =int(input("enter the numbers"))
count =0
count = count +numbers.count(0)
print('count of 0 :',count)


lab3.3
   numb =int(input("enter a number"))
n = int(input("enter another number"))
x =0
if(numb <=n):
    for x in range(1, numb+1):
        for i in range(1, x+1):
          print(i, end=" ")
        print(" ") 
        
        
        lab3.4
        a= int(input('enter a :'))
for i in range(1, a+1):
    spaces =" " * (a-1)
    for x in range(1, i+1):
        spaces += str(x)
        for k in range(i-1, 0, -1):
            spaces += str(k)
print(spaces )
