#n1 = 6
n1 = 21

if n1 % 3 == 0 and n1 % 7 == 0:
    print("3의 배수, 7의 배수")
elif n1 % 3 == 0:
    print("3의 배수")
elif n1 % 7 == 0:
    print("7의 배수")
else:
    print("3,7 의 배수가 아님")

