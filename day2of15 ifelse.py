dash="__"
print(dash*3,"welcome to day 2 coding python if els" ,dash*3)
print()

name=input("enter your name: ")
age=int(input("enter youre age: "))
print()
test =""
if age>=18:
    test="adult"
    
else :
    test="minor"

print(f"my name is {name} and am {age} years old ")
if test=="adult":
    print(f"am an {test}")
else:
    
    print(f"am a {test}")   
