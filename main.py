name = input("학생의 이름을 입력해 주세요: ")
circle = input("동그라미 갯수를 입력해 주세요: ")
triangle = input("세모 갯수를 입력해 주세요: ")
x = input("X 갯수를 입력해 주세요: ")

circle = int(circle)
triangle = int(triangle)
x = int(x)

if circle == 2:
    print("A+")
elif triangle == 1:
    if x == 0:
        print("A")
    else:
        print("C+")
elif triangle == 2:
    print("B+")
elif x == 1:
    print("B")
elif x == 2:
    print("C")