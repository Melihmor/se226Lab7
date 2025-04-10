import math_utils as mathu

def calculatorpr():
    print("Please give me x value")
    x=int(input())

    print("Please give me y value")
    y=int(input())

    print("Please give me a operator")
    op=input()

    functiondict={"+":mathu.add,"-":mathu.subtract,"*":mathu.multiply,"/":mathu.divide,"**":mathu.power,"mod":mathu.mod}

if __name__=='__main__':
    main()
