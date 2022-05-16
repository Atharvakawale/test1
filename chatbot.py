def greet(botname,age):
    print(" hello! my name is {0}.".format(botname))
    print("i was created in {0}.".format(age))
 
def remind_name():
    print('please, remind me your name.')
    name=input()
    print("what a great name you have ".format(name))
    print('god bye!!!have a nice day!!!!')
 
def guess_age():
    print("let me guess your age")
    print("enter the remaiders of dividing you age by 3,5,7")
    rem3=int(input())
    rem5=int(input())
    rem7=int(input())
    age=(rem3*70+rem5*21+rem7*15)%105
    print("your age")
    print(age)
def count():
    print("now i will prove that i can count to any number you want.")
    num=int(input())
    for i in range(1,num):
        if(i<=num):
            print(i)
    
 
def test():
    print("lets test your programming knowledge")
    print("why do we use methods?")
    print("1. to repeat statement")
    print("2. to decompose program")
    print("3. to determine execution time of program")
    print("4. to interupt exucution of priogram")
    answer=2
    guess=int(input())
    while guess !=answer:
        print("please try again")
        guess=int(input())
    print("corect answer! have a nice day ")
 
def end():
    greet('chatbot','2021')
    remind_name()
 
guess_age()
count()
test()
end()
