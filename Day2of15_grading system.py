dash="__"
print(dash*3,"welcome to day 2 coding grade cheker" ,dash*3)
print()

grade=int(input("enter your grade: "))

if grade>=80:
    print(f"A" )
    
elif grade>=60 and grade<=79:
    print("B")
    
elif grade>=40 and grade<=59:
    print("C")
    
else:
    print("fail")    