exercise 1

def even(list):
    my_list =[ ]
    even = my_list[: : 2]
    print(even)
return even

exercise 2

def greatest(list):
    my_list =[ ]
    i=0
    k = int(input("enter a number"))
    for i in range(len(my_list)):
        if my_list[i] > k:
           greatest = my_list[i]
        else:
            print("greatest does not exist")
    return greatest
  
  exercise 3
  
  def swap_min_max(a):
    max_index =a.index(max(a))
    min_index =a.index(min(a))
    ma=max(a)
    mi=min(a)
    a[max_index]=mi
    a[min_index]=ma
    a=[ ]
    print(a)
    return swap_min_max(a)
  
  exercise 4
  
   def value(dict,key):
        dict ={}
        print(dict["key"])
        return value
      
      exercise 5
