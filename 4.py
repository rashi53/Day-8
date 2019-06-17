try:
    fh=open(r"c:\python\abc.txt","r")
    fh.write("This is my test file for exception handling!!")
except Exception as ob:
    print(ob)
finally:
    print("Error: can\'t file or read data")
    try:
      fh.close()
    except Exception as ob:
       print(ob)
print("Thanks")
