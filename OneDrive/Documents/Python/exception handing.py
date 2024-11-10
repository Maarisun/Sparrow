try:
    a=int(input("a:"))
    b=int(input("b:"))
    c=input()
    print(b/c)

except ValueError:
    print("Value Error")
except TypeError:
    print("TypeError")
    
except Exception:
    print("Invalid input")

finally:
    print("Done")
    
