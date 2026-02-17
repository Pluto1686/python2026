import random
def apple_1():
    price_str=input("input the price of apple: ")
    weight_str=input("input the weight of apple: ")
    price=float(price_str)*float(weight_str)
    print(price)
def apple_2():
    price=float(input("input the price of apple: "))
    weight=float(input("input the weight of apple: "))
    price=price*weight
    print(price)
def personal_card():
    price=float(input())
    weight=float(input())
    money=price*weight
    print("my name is %s" %input("input your name"))
    print("my student_no is %06d"%input("input your student no"))
    print("the price of apple is %.02f yuan,buy %.02f ,pay %.02yuan"%(price,weight,money))
def Rock_Paper_Scissor():
    choice=input("input your chioce:1/2/3 ")
    computer=random.randint(1,3)
    print("the computer is%d"%computer)
    if choice==computer:
        print("draw")
    elif (choice==1 and computer==2)or (choice==2 and computer==3):
        print("tie")
    else:
        print("fail")
name_list=['mike ','max','hande']
del name_list[0]
info_tuple=(50,)
class Cat:
    "its a class of cat"
    def __init__(self,new_name,age):
        self.name=new_name
        self.age=age
        print("%s is coming"%self.name)
        print("age is %d"%self.age)
    def __del__(self):
        print("%s: im leaving"%self.name)
tom=Cat("X",10)

