
a=(input("enter a number"))
b=(input("enter a number"))  
try:
    res=int(a)/int(b)
except (ZeroDivisionError,ValueError) as ob:
    print("Division by zero not allowed or strings are not allowed.\
           Please input only integer")
except Exception as ob:
      print(ob)
else:
    print(a,"/",b,'=',res)
finally:
      print("resource deallocated")
print("thank you")

