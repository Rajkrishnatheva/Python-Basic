#BMI CALCULATOR
Height=float(input("enter your height in centimeter:"))
Weight=float(input("enter your weight in kg:"))
Height=Height/100
BMI=Weight/(Height*Height)
print("your body mass index is:", BMI)
if (BMI>0):
    if(BMI<=16):
        print("you are severely under weight")
    elif(BMI<=18.5):
        print("you are under weight")
    elif(BMI<=25):
        print("you are healthy")
    elif(BMI<=30):
        print("you are over weight")
    else:
        print("you are severely over weight")
#TEXT BASED ADVENTURE GAME WITH PYTHON
name=str(input("enter the name:"))
print(f"{name} you are stuck at work")
print("you are still working and suddenly you saw a ghost,Now you have 2 option")
print("1.run. 2.Jump from the window")
user =int(input("choose 1 or 2:"))
if user==1:
    print("you did it")
elif user==2:
    print("you are not that smart")
else:
    print("please check your input")

#RANGE
for i in range(6):
    for j in range(i):
        print("*", end="")
    print("")

for i in range(6,0,-1):
    for j in range(i):
        print("*",  end="")
    print("")

#TO GET EVEN NUMBER
print(list(range(0,20,2)))
for i in range(0,20,2):
    print(i)
num=int(input("enter the no.:"))
def func(x):
    if x==0:
        return 1
    else:
        return x
    print(func(5))
