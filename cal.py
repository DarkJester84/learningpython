
def cal(x,y):
    cal_function = str(input("What Function Would You Like To Call? (+,-,*,/): " ))
    
    if (cal_function == "+" ):
        z=x+y
        print(f"{x} + {y} =")
    elif (cal_function == "-"):
        z=x-y
        print(f"{x} - {y} =")
    elif (cal_function == "*"):
        z=x*y
        print(f"{x} * {y} =")
    elif (cal_function == "/"):
        z=x/y
        print(f"{x} / {y} =")
    
    return z



while True:    
  
    x=float(input("Please Enter You First Number: "))
    y=float(input("Please Enter Your Second Number: "))

    ans=cal(x,y)
    print(ans)
    print("")
    