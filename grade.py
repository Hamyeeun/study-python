stu=int(input("시험점수를 입력하세요"))
if stu>=0 and stu<101:
    if stu>89 and stu<101:
        print('A입니다.')
    elif stu>79 and stu<90:
        print('B입니다.')
    elif stu>69 and stu<80:
        print('C입니다.')
    elif stu>59 and stu<70:
        print("D입니다.")
    else:
        print("F")
else:
    print("점수를 잘못 입력하셨습니다")
