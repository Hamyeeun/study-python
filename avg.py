a=int(input("숫자1:"))
b=int(input("숫자2:"))
c=str(input("어떤 연산을 할까요?"))

if c=="+" :
    print("a+b:%d"%(a+b))

elif c=="-" :
    print("a-b:%d"%(a-b))

elif c=="*" :
    print("a*b:%d"%(a*b))

elif c=="/" :
    print("a/b:%d"%(a//b))

elif c=="%" :
    print("a%b:%d"%(a%b))

else :
    print('잘못입력하였습니다')
