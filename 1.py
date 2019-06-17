try:
    import abc1
except Exception as ob:
    print(ob)

a=int(input("enter a number"))
b=int(input("enter a number"))
try:
    res=a/b
except Exception as ob:
    print("Division by zero not allowed")

else:
    print(a,"/",b,'=',res)

print("thank you")
