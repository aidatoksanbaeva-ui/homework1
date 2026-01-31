import math

def main():
    print(math.pow(2,8))
    #бул 2нин 8 дарежеси
if __name__ == "__main__":
    main()

    L = int(input("Enter a number: "))
    m= L//100
    #// деген калдыксыз шгарады (метр)
    с= L%100
    # % калдыгын шгарады (см)
    print(m)

    a=int(input("Enter a number: "))
    x= a>0
    print(x)
    #

    a = int(input("Enter a number: "))
    x = a%2 != 0
    print(x)
    #!= деген тен болмау керек дегенд
    y= a%2==1
    print(y)
    #== бул тен болу керек деген

    a = int(input("Enter a number: "))
    if a>0:
    #егер а улкен 0 болса
        a=a-10
        print(a)
    elif a==3    #тексеру ифтан киын
    else:
    #иначе
        a=a+10
        print(a)

i = 0
while i < 5:
    print(i)
    i += 1


